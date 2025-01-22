Module shdp.protocol.managers.bits.decoder
==========================================

Classes
-------

`BitDecoder(frame: shdp.utils.bitvec.BitVec)`
:   A generic decoder that processes bytes according to a specified bit order.
    
    This class implements a generic decoder that can work with both LSB and MSB
    bit orderings. The bit order is specified through the generic type parameter R,
    which must be a BitReversible type (either Lsb or Msb).
    
    The decoder provides iteration over its underlying bytes, making it easy to
    process data in the specified bit order.
    
    Type Parameters:
        R: The bit ordering type (must be BitReversible). Use Lsb for least
           significant bit first, or Msb for most significant bit first.
    
    Args:
        frame (BitVec): The binary data to be decoded
        
    Examples:
        >>> # Create an LSB decoder
        >>> lsb_decoder = BitDecoder[Lsb](b'\x0F\x42')
        >>> list(lsb_decoder.frame)  # Access raw bytes
        [15, 66]
        
        >>> # Create an MSB decoder
        >>> msb_decoder = BitDecoder[Msb](b'\x80\x01')
        >>> msb_decoder._bit_order_type == Msb
        True

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

    ### Methods

    `read_data(self, n: int) ‑> shdp.utils.result.Result[shdp.utils.bitvec.BitVec, shdp.protocol.errors.Error]`
    :   Reads n bytes from the frame at the current position.
        
        Args:
            n (int): The number of bytes to read
            
        Returns:
            Result[BitVec, Error]: The bytes read from the frame

    `read_vec(self, fp: int, tp: int) ‑> shdp.utils.result.Result[shdp.utils.bitvec.BitVec, shdp.protocol.errors.Error]`
    :   Reads a vector of bytes from the frame between two positions.
        
        Args:
            fp (int): The start position
            tp (int): The end position
            
        Returns:
            Result[BitVec, Error]: The bytes read from the frame

`Frame(version: int, event: int, data_size: int, data: shdp.utils.bitvec.BitVec)`
:   A frame of data that can be decoded according to a specified bit order.
    
    This class represents a frame of data that has been decoded according to a
    specified bit order. It contains the version, event, data size, and data fields.

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

`FrameDecoder(decoder: shdp.protocol.managers.bits.decoder.BitDecoder[~R])`
:   A decoder that processes frames of data according to a specified bit order.
    
    This class extends BitDecoder to provide additional functionality for processing
    frames of data. It allows for reading data in the specified bit order and provides
    a more convenient interface for accessing the underlying bytes.

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

    ### Methods

    `decode(self) ‑> shdp.utils.result.Result[shdp.protocol.managers.bits.decoder.Frame[~R], shdp.protocol.errors.Error]`
    :   Decodes the frame according to the specified bit order.
        
        Returns:
            Result[Frame[R], Error]: A Frame object containing the decoded version,
                                     event, data size, and data

    `get_decoder(self) ‑> shdp.protocol.managers.bits.decoder.BitDecoder[~R]`
    :   Returns the underlying decoder.
        
        Returns:
            BitDecoder[R]: The underlying decoder