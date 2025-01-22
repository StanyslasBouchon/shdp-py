Module shdp.server.tls
======================

Classes
-------

`ShdpTlsServer(cert_path: pathlib.Path, key_path: pathlib.Path)`
:   TLS implementation of the SHDP server protocol.
    
    This class implements a TLS server that handles SHDP protocol connections.
    It manages client connections and provides methods for server operations.
    
    Attributes:
        _server (Optional[asyncio.Server]): The TLS server instance
        _clients (Dict[str, StreamWriter]): Dictionary of connected clients
    
    Initialize a new SHDP TLS server instance.

    ### Ancestors (in MRO)

    * shdp.lib.IShdpServer
    * typing.Generic
    * abc.ABC

    ### Static methods

    `listen(cert_path: pathlib.Path, key_path: pathlib.Path, port: int = 15150) ‑> shdp.utils.result.Result[shdp.server.tls.ShdpTlsServer, shdp.protocol.errors.Error]`
    :   Start listening for TLS connections on the specified port.
        
        Args:
            cert_path: Path to the certificate file
            key_path: Path to the private key file
            port: Port number to listen on, defaults to 15150
            
        Returns:
            Result['ShdpTlsServer', Error]: Ok with server instance if successful,
                                          Err with error details if failed

    ### Methods

    `close(self) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Close the server and all client connections.
        
        Returns:
            Result[None, Error]: Ok(None) if closed successfully, Err if failed

    `get_clients(self) ‑> shdp.utils.result.Result[typing.Dict[str, asyncio.streams.StreamWriter], shdp.protocol.errors.Error]`
    :   Get a dictionary of all connected clients.
        
        Returns:
            Result[Dict[str, StreamWriter], Error]: Ok with clients dict if successful,
                                                  Err if failed