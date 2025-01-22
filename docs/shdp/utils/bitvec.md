Module shdp.utils.bitvec
========================
BitVec implementation for handling bit vectors.

This module provides a specialized list type for handling bit vectors,
with utility methods for bit manipulation.

Classes
-------

`BitVec(*args, **kwargs)`
:   A specialized list for handling bit vectors.
    
    This class extends the built-in list to provide specialized handling
    of boolean values representing bits, along with utility methods for
    bit manipulation.
    
    Examples:
        >>> bits = BitVec([1, 0, 1])  # Create from list
        >>> bits.append(1)  # Add a bit
        >>> bits
        [1, 0, 1, 1]
        >>> bits.extend([0, 0])  # Add multiple bits
        >>> bits
        [1, 0, 1, 1, 0, 0]
    
    Initialize a new bit vector.
    
    Args:
        *args: Arguments passed to list constructor
        **kwargs: Keyword arguments passed to list constructor

    ### Ancestors (in MRO)

    * builtins.list

    ### Methods

    `append(self, value)`
    :   Append a new bit, ensuring boolean value.
        
        Args:
            value: The value to append (converted to bool)

    `extend(self, values)`
    :   Extend with multiple bits, ensuring boolean values.
        
        Args:
            values: Iterable of values to append (each converted to bool)

    `to_bytes(self) ‑> list[int]`
    :   Converts the list of bits to a list of bytes.
        
        Returns:
            list[int]: List of bytes (0-255)
            
        Example:
            >>> bits = BitVec([1,0,1,0, 0,0,0,0])  # 10100000 in binary
            >>> bits.to_bytes()
            [160]  # 0xA0 in hexadecimal
            >>> bits = BitVec([1,1,1,1, 0,0,0,0, 1,0,1,0])  # 3 bytes
            >>> bits.to_bytes()
            [240, 10]  # [0xF0, 0x0A]