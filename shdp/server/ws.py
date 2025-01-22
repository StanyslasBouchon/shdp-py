import asyncio
import logging
from typing import Dict, Optional, Set

import websockets
from websockets.server import WebSocketServerProtocol, serve

from ..lib import IShdpServer
from ..protocol.errors import Error, ErrorKind
from ..protocol.managers.bits.decoder import BitDecoder, FrameDecoder
from ..protocol.managers.bits.encoder import FrameEncoder
from ..protocol.managers.registry import EVENT_REGISTRY_MSB
from ..protocol.server.versions.v1.c0x0002 import ErrorResponse
from ..utils.bitvec import BitVec
from ..utils.result import Result


class ShdpWsServer(IShdpServer[WebSocketServerProtocol, None]):
    """WebSocket implementation of the SHDP server protocol.

    This class implements a WebSocket server that handles SHDP protocol connections.
    It manages client connections and provides methods for server operations.

    Attributes:
        _server (Optional[websockets.server.WebSocketServer]): The WebSocket server instance
        _clients (Dict[str, WebSocketServerProtocol]): Dictionary of connected clients
    """

    def __init__(self):
        """Initialize a new SHDP WebSocket server instance."""
        self._server: Optional[websockets.server.WebSocketServer] = None
        self._clients: Dict[str, WebSocketServerProtocol] = {}
        self._active_connections: Set[WebSocketServerProtocol] = set()

    @staticmethod
    async def listen(
        port: int = 15150,
    ) -> Result[IShdpServer[WebSocketServerProtocol, None], Error]:
        """Start listening for WebSocket connections on the specified port.

        Args:
            port: Port number to listen on, defaults to 15150

        Returns:
            Result[IShdpServer[WebSocketServerProtocol], Error]: Ok with server instance if successful,
                                          Err with error details if failed
        """
        try:
            ws_server = ShdpWsServer()

            server = await serve(
                ws_server._accept,
                host="0.0.0.0",
                port=port,
                ping_interval=20,
                ping_timeout=20,
            )

            ws_server._server = server
            logging.info(f"SHDP WebSocket server listening on port {port}")
            return Result[IShdpServer[WebSocketServerProtocol, None], Error].Ok(
                ws_server
            )

        except Exception as e:
            return Result[IShdpServer[WebSocketServerProtocol, None], Error].Err(
                Error.new(ErrorKind.USER_DEFINED, str(e))
            )

    async def stop(self) -> Result[None, Error]:
        """Close the server and all client connections.

        Returns:
            Result[None, Error]: Ok(None) if closed successfully, Err if failed
        """
        try:
            if self._server is None:
                return Result[None, Error].Err(
                    Error.new(ErrorKind.SERVICE_UNAVAILABLE, "Server not listening")
                )

            # Fermer toutes les connexions clients actives
            close_tasks = [client.close() for client in self._active_connections]
            if close_tasks:
                await asyncio.gather(*close_tasks, return_exceptions=True)

            self._active_connections.clear()
            self._clients.clear()

            self._server.close()
            await self._server.wait_closed()
            self._server = None

            logging.info("SHDP WebSocket server closed")
            return Result[None, Error].Ok(None)

        except Exception as e:
            return Result[None, Error].Err(Error.new(ErrorKind.USER_DEFINED, str(e)))

    def get_clients(self) -> Result[Dict[str, WebSocketServerProtocol], Error]:
        """Get a dictionary of all connected clients.

        Returns:
            Result[Dict[str, WebSocketServerProtocol], Error]: Ok with clients dict if successful,
                                                             Err if failed
        """
        return Result[Dict[str, WebSocketServerProtocol], Error].Ok(self._clients)

    async def _accept(self, websocket: WebSocketServerProtocol) -> None:
        """Handle incoming WebSocket connection.

        Args:
            websocket: The WebSocket connection to handle
        """
        client_addr = f"{websocket.remote_address[0]}:{websocket.remote_address[1]}"
        self._clients[client_addr] = websocket
        self._active_connections.add(websocket)
        logging.info(f"Accepted connection from {client_addr}")

        try:
            async for message in websocket:
                if not message:
                    continue

                decoder = BitDecoder(BitVec.from_bytes(message))
                frame_decoder = FrameDecoder(decoder)
                data = frame_decoder.decode().unwrap()
                decoder = frame_decoder.get_decoder()

                factories = EVENT_REGISTRY_MSB.get_event((data.version, data.event))

                if factories is None:
                    await websocket.send(
                        await self._answer_error(
                            data.version,
                            Error.new(ErrorKind.NOT_FOUND, "Event not found"),
                        )
                    )
                    continue

                for factory in factories:
                    event = factory(decoder)
                    event.decode(data)

                    responses = event.get_responses().unwrap()
                    for response in responses:
                        encoder = FrameEncoder(data.version)
                        frame = encoder.encode(response)
                        await websocket.send(frame.unwrap().to_bytes())

        except websockets.exceptions.ConnectionClosed:
            logging.debug(f"[SHDP:WS::S] Connection closed by client {client_addr}")
        except Exception as e:
            logging.error(f"Error handling connection from {client_addr}: {e}")
        finally:
            if client_addr in self._clients:
                del self._clients[client_addr]
            self._active_connections.discard(websocket)

    async def _answer_error(self, version: int, error: Error) -> bytes:
        """Generate error response frame.

        Args:
            version: Protocol version
            error: Error to send

        Returns:
            bytes: Encoded error frame
        """
        encoder = FrameEncoder(version)
        return encoder.encode(ErrorResponse(error)).unwrap().to_bytes()
