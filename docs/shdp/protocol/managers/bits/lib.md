Module shdp.protocol.managers.bits.lib
======================================

Classes
-------

`BitOrder(*args, **kwds)`
:   Represents the bit ordering in data processing.
    
    This enum defines the two possible bit orderings:
    - LSB (Least Significant Bit first): bits are processed from right to left
    - MSB (Most Significant Bit first): bits are processed from left to right
    
    Examples:
        >>> order = BitOrder.LSB
        >>> order == BitOrder.LSB
        True
        >>> str(order)
        'LSB'

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `LSB`
    :

    `MSB`
    :

`BitReversible()`
:   Abstract base class for types that can have their bit order reversed.
    
    This class defines the interface for types that can switch between LSB and MSB
    bit ordering. Implementing classes must provide:
    1. A bit_order property that returns the current BitOrder
    2. A get_opposite_type class method that returns the opposite ordering type
    
    Examples:
        >>> class MyLsb(BitReversible):
        ...     @property
        ...     def bit_order(self) -> BitOrder:
        ...         return BitOrder.LSB
        ...     @classmethod
        ...     def get_opposite_type(cls):
        ...         return MyMsb

    ### Ancestors (in MRO)

    * abc.ABC
    * typing.Generic

    ### Descendants

    * shdp.protocol.managers.bits.decoder.BitDecoder
    * shdp.protocol.managers.bits.decoder.Frame
    * shdp.protocol.managers.bits.decoder.FrameDecoder
    * shdp.protocol.managers.bits.encoder.BitEncoder
    * shdp.protocol.managers.bits.encoder.FrameEncoder
    * shdp.protocol.managers.bits.lib.Lsb
    * shdp.protocol.managers.bits.lib.Msb
    * shdp.protocol.managers.event.EventDecoder
    * shdp.protocol.managers.event.EventEncoder
    * shdp.protocol.managers.registry.EventRegistry

    ### Static methods

    `get_opposite_type() ‑> Type[shdp.protocol.managers.bits.lib.BitReversible]`
    :   Returns the class type with opposite bit ordering.
        
        Returns:
            Type[BitReversible]: The class representing the opposite bit order
            
        Examples:
            >>> Lsb.get_opposite_type() == Msb
            True
            >>> Msb.get_opposite_type() == Lsb
            True

    ### Instance variables

    `bit_order: shdp.protocol.managers.bits.lib.BitOrder`
    :   Returns the current bit order of this instance.
        
        Returns:
            BitOrder: The current bit ordering (LSB or MSB)
            
        Examples:
            >>> lsb = Lsb(b'\x00')
            >>> lsb.bit_order == BitOrder.LSB
            True

`Lsb(data)`
:   Represents data that should be processed in Least Significant Bit first order.
    
    In LSB mode, bits are processed from right to left. For example, the byte 0x01
    would be processed as 1 first, then seven 0s.
    
    Args:
        data: The binary data to be processed in LSB order
        
    Examples:
        >>> # Create an LSB processor for a single byte
        >>> lsb = Lsb(b'\x01')
        >>> lsb.bit_order == BitOrder.LSB
        True
        >>> # Get the opposite type (MSB)
        >>> opposite = lsb.get_opposite_type()
        >>> opposite == Msb
        True

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

`Msb(data)`
:   Represents data that should be processed in Most Significant Bit first order.
    
    In MSB mode, bits are processed from left to right. For example, the byte 0x80
    would be processed as 1 first, then seven 0s.
    
    Args:
        data: The binary data to be processed in MSB order
        
    Examples:
        >>> # Create an MSB processor for a single byte
        >>> msb = Msb(b'\x80')
        >>> msb.bit_order == BitOrder.MSB
        True
        >>> # Get the opposite type (LSB)
        >>> opposite = msb.get_opposite_type()
        >>> opposite == Lsb
        True

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic