Module shdp.protocol.managers.event
===================================

Classes
-------

`EventDecoder()`
:   Abstract base class for decoding protocol events.
    
    This class defines the interface for decoding events in the protocol.
    Each event type should implement this interface to specify how it should
    be decoded from bits and what responses it can generate.
    
    Example:
        >>> class LoginDecoder(EventDecoder[Lsb]):
        ...     def decode(self, frame: Frame[Lsb]):
        ...         user_id = frame.read_int(8)  # Read event data
        ...     
        ...     def get_responses(self) -> list[Type[EventEncoder[Msb]]]:
        ...         return [LoginSuccessEvent, LoginFailedEvent]

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

    ### Descendants

    * shdp.protocol.client.versions.v1.r0x0001.HtmlFileResponse
    * shdp.protocol.client.versions.v1.r0x0002.ErrorResponse
    * shdp.protocol.client.versions.v1.r0x0003.ComponentNeedsResponse
    * shdp.protocol.client.versions.v1.r0x0004.FullFyveResponse
    * shdp.protocol.client.versions.v1.r0x0006.InteractionResponse
    * shdp.protocol.server.versions.v1.r0x0000.ComponentNeedsRequest
    * shdp.protocol.server.versions.v1.r0x0005.InteractionRequest

    ### Methods

    `decode(self, frame: shdp.protocol.managers.bits.decoder.Frame[~R]) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Decode event data from a frame.
        
        Args:
            frame (Frame[R]): The frame containing the event data

    `get_responses(self) ‑> shdp.utils.result.Result[list[typing.Type[shdp.protocol.managers.event.EventEncoder[shdp.protocol.managers.bits.lib.BitReversible]]], shdp.protocol.errors.Error]`
    :   Get list of possible response types for this event.
        
        Returns:
            Result containing list of event encoder types that can respond to this event

`EventEncoder()`
:   Abstract base class for encoding protocol events.
    
    This class defines the interface for encoding events in the protocol.
    Each event type should implement this interface to specify how it should
    be encoded into bits.
    
    Example:
        >>> class LoginEvent(EventEncoder[Lsb]):
        ...     def encode(self):
        ...         self.encoder.add_data(0x01, 8)  # Add event data
        ...     
        ...     def get_encoder(self) -> BitEncoder[Lsb]:
        ...         return self.encoder
        ...     
        ...     def get_event(self) -> int:
        ...         return 0x0001  # Event ID for login

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

    ### Descendants

    * shdp.protocol.client.versions.v1.c0x0000.ComponentNeedsRequest
    * shdp.protocol.client.versions.v1.c0x0005.InteractionRequest
    * shdp.protocol.server.versions.v1.c0x0001.HtmlFileResponse
    * shdp.protocol.server.versions.v1.c0x0002.ErrorResponse
    * shdp.protocol.server.versions.v1.c0x0003.ComponentNeedsResponse
    * shdp.protocol.server.versions.v1.c0x0004.FullFyveResponse
    * shdp.protocol.server.versions.v1.c0x0006.InteractionResponse

    ### Methods

    `encode(self) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Encode the event data into bits.
        
        This method should use the encoder to add the event's data
        to the bit frame.

    `get_encoder(self) ‑> shdp.protocol.managers.bits.encoder.BitEncoder[~R]`
    :   Get the bit encoder used by this event.
        
        Returns:
            BitEncoder[R]: The encoder instance for this event

    `get_event(self) ‑> int`
    :   Get the event identifier.
        
        Returns:
            int: The unique 16-bit identifier for this event type