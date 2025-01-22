Module shdp.lib
===============

Classes
-------

`IShdpClient()`
:   Abstract base class for SHDP protocol clients.
    
    This class defines the interface for SHDP clients that can connect
    to servers and send events.
    
    Examples:
        >>> class MyClient(IShdpClient[MyClientType]):
        ...     @staticmethod
        ...     def connect(addr):
        ...         # Implementation
        ...         return Result.Ok(client)

    ### Ancestors (in MRO)

    * typing.Generic
    * abc.ABC

    ### Descendants

    * shdp.client.quic.ShdpQuicClient
    * shdp.client.tls.ShdpTlsClient

    ### Static methods

    `connect(self, to: tuple[str, int]) ‑> shdp.utils.result.Result[shdp.lib.IShdpClient[~CT], shdp.protocol.errors.Error]`
    :   Connect to a server at the specified address.
        
        Args:
            to: Tuple of (host, port) to connect to
            
        Returns:
            Result containing connected client if successful
            
        Example:
            >>> result = Client.connect(('localhost', 8080))
            >>> if result.is_ok():
            ...     client = result.unwrap()

    ### Methods

    `disconnect(self) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Disconnect from the server.
        
        Returns:
            Result indicating success or failure of disconnecting
            
        Example:
            >>> client.disconnect()

    `get_address(self) ‑> shdp.utils.result.Result[tuple[str, int], shdp.protocol.errors.Error]`
    :   Get this client's address.
        
        Returns:
            Result containing (host, port) tuple if successful
            
        Example:
            >>> addr = client.get_address().unwrap()
            >>> host, port = addr

    `send(self, event: shdp.protocol.managers.event.EventEncoder[shdp.protocol.managers.bits.lib.Lsb]) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Send an encoded event to the server.
        
        Args:
            event: The encoded event to send
            
        Returns:
            Result indicating success or failure of sending
            
        Example:
            >>> event = MyEvent()
            >>> client.send(event)

`IShdpServer()`
:   Abstract base class for SHDP protocol servers.
    
    This class defines the interface for SHDP servers that can handle
    connections from multiple clients of type CT.
    
    Examples:
        >>> class MyServer(IShdpServer[MyClient]):
        ...     @staticmethod
        ...     def listen(port=15150):
        ...         # Implementation
        ...         return Result.Ok(client)

    ### Ancestors (in MRO)

    * typing.Generic
    * abc.ABC

    ### Descendants

    * shdp.server.quic.ShdpQuicServer
    * shdp.server.tls.ShdpTlsServer

    ### Static methods

    `listen(self, port: int = 15150) ‑> shdp.utils.result.Result[shdp.lib.IShdpClient[~CT], shdp.protocol.errors.Error]`
    :   Start listening for client connections on the specified port.
        
        Args:
            port: Port number to listen on, defaults to 15150
            
        Returns:
            Result containing the connected client if successful, Error if failed
            
        Example:
            >>> result = server.listen(8080)
            >>> if result.is_ok():
            ...     client = result.unwrap()

    ### Methods

    `get_clients(self) ‑> shdp.utils.result.Result[dict[str, ~CT], shdp.protocol.errors.Error]`
    :   Get a dictionary of all connected clients.
        
        Returns:
            Result containing dict mapping 'IP:PORT' strings to client objects
            
        Example:
            >>> clients = server.get_clients().unwrap()
            >>> for addr, client in clients.items():
            ...     print(f"Client at {addr}")

    `stop(self) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Stop the server and close all client connections.
        
        Returns:
            Result indicating success or failure of stopping server
            
        Example:
            >>> server.stop()