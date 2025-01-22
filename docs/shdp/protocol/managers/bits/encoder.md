Module shdp.protocol.managers.bits.encoder
==========================================

Classes
-------

`BitEncoder()`
:   An encoder that processes bits according to a specified bit order.
    
    This class provides functionality for building frames of bits and encoding them
    according to a specified bit order (MSB or LSB).
    
    Attributes:
        frame (BitVec): The current frame being built
        
    Examples:
        >>> encoder = BitEncoder()
        >>> encoder.add_data(42, 8)  # Add number 42 using 8 bits
        >>> encoder.add_bytes([0xA0, 0xFF])  # Add two bytes
        >>> encoder.encode()  # Get the final encoded bytes
    
    Initialize a new empty bit encoder.

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

    ### Class variables

    `frame: shdp.utils.bitvec.BitVec`
    :

    ### Methods

    `add_bytes(self, data: bytes) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Add a sequence of bytes to the frame.
        
        Args:
            data (bytes): List of bytes to add
            
        Example:
            >>> encoder = BitEncoder()
            >>> encoder.add_bytes([0xA0, 0x0F])  # Add two bytes

    `add_data(self, data: int, n: int) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Add n bits from an integer to the frame.
        
        Args:
            data (int): The integer containing the bits to add
            n (int): Number of bits to extract from data
            
        Raises:
            ValueError: If adding the bits would exceed the frame size limit
            
        Example:
            >>> encoder = BitEncoder()
            >>> encoder.add_data(0b1010, 4)  # Add 4 bits: 1010
            >>> encoder.frame
            [0, 1, 0, 1]  # LSB first

    `add_vec(self, bitvec: shdp.utils.bitvec.BitVec) ‑> shdp.utils.result.Result[None, shdp.protocol.errors.Error]`
    :   Add a bit vector directly to the frame.
        
        Args:
            bitvec (BitVec): The bit vector to add
            
        Example:
            >>> encoder = BitEncoder()
            >>> encoder.add_vec([1, 0, 1])  # Add three bits

    `append_data_from(self, other: BitEncoder[R]) ‑> None`
    :   Append all bits from another encoder's frame.
        
        Args:
            other (BitEncoder[R]): Another encoder whose frame to append
            
        Example:
            >>> encoder1 = BitEncoder()
            >>> encoder1.add_data(0b101, 3)
            >>> encoder2 = BitEncoder()
            >>> encoder2.append_data_from(encoder1)

    `encode(self) ‑> shdp.utils.bitvec.BitVec`
    :   Encode the frame according to the bit order.
        
        Returns:
            BitVec: The encoded frame with bits arranged according to the bit order
            
        Example:
            >>> encoder = BitEncoder()
            >>> encoder.add_data(0b10100000, 8)
            >>> encoder.encode()  # Returns bytes with correct bit order

    `reverse_bits_in_bytes(self, input: shdp.utils.bitvec.BitVec) ‑> shdp.utils.bitvec.BitVec`
    :   Reverse the bits in each byte of the input.
        
        Args:
            input (BitVec): The input bit vector
            
        Returns:
            BitVec: New bit vector with reversed bits in each byte
            
        Example:
            >>> encoder = BitEncoder()
            >>> encoder.reverse_bits_in_bytes([0b10100000])
            [0b00000101]  # Bits reversed within the byte

`FrameEncoder(version: shdp.protocol.versions.Version)`
:   Encoder for complete protocol frames.
    
    This class handles the encoding of complete protocol frames, including
    version, event ID, and data size headers.
    
    Attributes:
        encoder (BitEncoder[R]): The underlying bit encoder
        version (Version): The protocol version to use
        
    Example:
        >>> frame_encoder = FrameEncoder(Version.V1_0)
        >>> frame_encoder.encode(MyEvent)  # Encode a complete frame
    
    Initialize a new frame encoder.
    
    Args:
        encoder (BitEncoder[R]): The bit encoder to use
        version (Version): The protocol version

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

    ### Methods

    `encode(self, frame: Type[~E]) ‑> shdp.utils.result.Result[shdp.utils.bitvec.BitVec | None, shdp.protocol.errors.Error]`
    :   Encode a complete protocol frame.
        
        Args:
            frame (Type[E]): The event frame to encode
            
        Returns:
            bytes: The complete encoded frame
            
        Raises:
            ValueError: If the frame size is invalid
            
        Example:
            >>> class MyEvent(EventEncoder):
            ...     def encode(self):
            ...         self.encoder.add_data(42, 8)
            >>> encoder = BitEncoder()
            >>> frame_encoder = FrameEncoder(encoder, Version.V1_0)
            >>> frame_encoder.encode(MyEvent)