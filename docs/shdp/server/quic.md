Module shdp.server.quic
=======================

Classes
-------

`ShdpQuicServer(cert_path: pathlib.Path, key_path: pathlib.Path)`
:   QUIC implementation of the SHDP server protocol.
    
    This class implements a QUIC server that handles SHDP protocol connections.
    It manages client connections and provides methods for server operations.
    
    Attributes:
        _server (Optional[QuicConnectionProtocol]): The QUIC server instance
        _clients (Dict[str, QuicConnectionProtocol]): Dictionary of connected clients
        
    Example:
        >>> result = await ShdpQuicServer.listen(15150)
        >>> if result.is_ok():
        ...     server = result.unwrap()
        ...     # Server is now listening
    
    Initialize a new SHDP QUIC server instance.

    ### Ancestors (in MRO)

    * shdp.lib.IShdpServer
    * typing.Generic
    * abc.ABC

    ### Static methods

    `listen(cert_path: pathlib.Path, key_path: pathlib.Path, port: int = 15150) ‑> shdp.utils.result.Result[shdp.server.quic.ShdpQuicServer, shdp.protocol.errors.Error]`
    :   Start listening for QUIC connections on the specified port.
        
        Args:
            port: Port number to listen on, defaults to 15150
            
        Returns:
            Result['ShdpQuicServer', Error]: Ok with server instance if successful,
                                           Err with error details if failed
                                           
        Example:
            >>> result = await ShdpQuicServer.listen(8080)
            >>> if result.is_ok():
            ...     server = result.unwrap()

    ### Methods

    `close(self) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Close the server and all client connections.
        
        Returns:
            Result[None, Error]: Ok(None) if closed successfully, Err if failed
            
        Example:
            >>> await server.close()

    `get_clients(self) ‑> shdp.utils.result.Result[typing.Dict[str, aioquic.asyncio.protocol.QuicConnectionProtocol], shdp.protocol.errors.Error]`
    :   Get a dictionary of all connected clients.
        
        Returns:
            Result[Dict[str, QuicConnectionProtocol], Error]: Ok with clients dict if successful,
                                                            Err if failed
                                                            
        Example:
            >>> result = server.get_clients()
            >>> if result.is_ok():
            ...     clients = result.unwrap()
            ...     for addr, client in clients.items():
            ...         print(f"Client connected from {addr}")