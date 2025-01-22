Module shdp.client.quic
=======================

Classes
-------

`ShdpQuicClient()`
:   QUIC implementation of the SHDP client protocol.
    
    This class implements a QUIC client that handles SHDP protocol connections.
    It manages the connection to a server and provides methods for client operations.
    
    Attributes:
        _connection (Optional[QuicConnectionProtocol]): The QUIC connection instance
        _address (Optional[Tuple[str, int]]): The (host, port) of the connected server
        
    Example:
        >>> result = await ShdpQuicClient.connect(('localhost', 15150))
        >>> if result.is_ok():
        ...     client = result.unwrap()
        ...     # Client is now connected
    
    Initialize a new SHDP QUIC client instance.

    ### Ancestors (in MRO)

    * shdp.lib.IShdpClient
    * typing.Generic
    * abc.ABC

    ### Static methods

    `connect(to: Tuple[str, int]) ‑> shdp.utils.result.Result[shdp.client.quic.ShdpQuicClient, shdp.protocol.errors.Error]`
    :   Connect to a server at the specified address.
        
        Args:
            to: Tuple of (host, port) to connect to
            
        Returns:
            Result[ShdpQuicClient, Error]: Ok with client instance if successful,
                                         Err with error details if failed

    ### Methods

    `disconnect(self) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Disconnect from the server.
        
        Returns:
            Result[None, Error]: Ok(None) if disconnected successfully, Err if failed

    `get_address(self) ‑> shdp.utils.result.Result[typing.Tuple[str, int], shdp.protocol.errors.Error]`
    :   Get this client's server connection address.
        
        Returns:
            Result[Tuple[str, int], Error]: Ok with (host, port) if connected,
                                          Err if not connected

    `send(self, event: shdp.protocol.managers.event.EventEncoder[shdp.protocol.managers.bits.lib.Lsb]) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Send an encoded event to the server.
        
        Args:
            event: The encoded event to send
            
        Returns:
            Result[None, Error]: Ok(None) if sent successfully, Err if failed