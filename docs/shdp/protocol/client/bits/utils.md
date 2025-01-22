Module shdp.protocol.client.bits.utils
======================================

Classes
-------

`FyveImpl()`
:   Implementation of 5-bit (fyve) operations for the SHDP protocol.
    
    Provides static methods for reading and processing fyve sequences.
    
    Examples:
        >>> decoder = BitDecoder()
        >>> fyve = FyveImpl.read_fyve(decoder)  # Reads next 5 bits
        >>> operation = FyveImpl.get_op(decoder)  # Gets complete operation

    ### Static methods

    `get_op(decoder: shdp.protocol.managers.bits.decoder.BitDecoder[shdp.protocol.managers.bits.lib.Msb]) ‑> shdp.utils.result.Result[shdp.protocol.client.bits.utils.Operation, shdp.protocol.errors.Error]`
    :   Read and construct a complete Operation from the bit stream.
        
        Args:
            decoder: Bit decoder for reading 5-bit sequences
            
        Returns:
            Result[Operation, Error]: Constructed Operation instance
            
        Example:
            >>> decoder = BitDecoder(bytes([0x00, 0x10]))  # START_OF_TAG
            >>> op = FyveImpl.get_op(decoder)
            >>> op.kind == OperatingCode.SYSTEM
            True
            >>> op.code == OperationCode.START_OF_TAG
            True

    `read_fyve(decoder: shdp.protocol.managers.bits.decoder.BitDecoder[shdp.protocol.managers.bits.lib.Msb]) ‑> shdp.utils.result.Result[int, shdp.protocol.errors.Error]`
    :   Read a single 5-bit value from the decoder.
        
        Args:
            decoder: Bit decoder for reading values
            
        Returns:
            Result[int, Error]: 5-bit integer value (0-31)
            
        Example:
            >>> decoder = BitDecoder(bytes([0x1f]))
            >>> FyveImpl.read_fyve(decoder)
            Result.Ok(31)  # 0x1f

`OperatingCode(*args, **kwds)`
:   Operating code for the SHDP protocol.
    
    Used to distinguish between system operations and character data.
    
    Examples:
        >>> op = OperatingCode.from_fyve(0x00)
        >>> op == OperatingCode.SYSTEM
        True
        
        >>> op = OperatingCode.from_fyve(0x1f)
        >>> op == OperatingCode.CHARACTER
        True

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `CHARACTER`
    :

    `SYSTEM`
    :

    ### Static methods

    `from_fyve(fyve: int) ‑> Self`
    :   Convert a 5-bit value (fyve) to an OperatingCode.
        
        Args:
            fyve: 5-bit integer value (0x00 or other)
            
        Returns:
            OperatingCode.SYSTEM for 0x00, OperatingCode.CHARACTER otherwise
            
        Example:
            >>> OperatingCode.from_fyve(0x00)
            OperatingCode.SYSTEM
            >>> OperatingCode.from_fyve(0x1f)
            OperatingCode.CHARACTER

    ### Methods

    `to_fyve(self) ‑> int`
    :   Convert the OperatingCode to its 5-bit representation.
        
        Returns:
            Integer value (0x00 for SYSTEM, 0x1f for CHARACTER)
            
        Example:
            >>> OperatingCode.SYSTEM.to_fyve()
            0x00
            >>> OperatingCode.CHARACTER.to_fyve()
            0x1f

`Operation()`
:   Represents a complete SHDP protocol operation.
    
    Handles both system operations and character data by decoding 5-bit sequences (fyves).
    
    Examples:
        # Decoding a character operation
        >>> decoder = BitDecoder()
        >>> op = Operation.from_fyve(0x1f, decoder)  # For multi-fyve character
        >>> char = op.get_char()  # Returns the decoded character
        
        # Decoding a system operation
        >>> op = Operation.from_fyve(0x00, decoder)
        >>> op.kind == OperatingCode.SYSTEM
        True
        >>> op.code == OperationCode.START_OF_TAG  # If next fyve was 0x10
        True

    ### Class variables

    `code: shdp.protocol.client.bits.utils.OperationCode | None`
    :

    `kind: shdp.protocol.client.bits.utils.OperatingCode`
    :

    `values: list[int]`
    :

    ### Static methods

    `from_fyve(fyve: int, decoder: shdp.protocol.managers.bits.decoder.BitDecoder[shdp.protocol.managers.bits.lib.Msb]) ‑> shdp.utils.result.Result[typing.Self, shdp.protocol.errors.Error]`
    :   Create an Operation from an initial fyve and subsequent bits.
        
        Args:
            fyve: Initial 5-bit value determining operation type
            decoder: Bit decoder for reading additional values
            
        Returns:
            Result[Operation, Error]: New Operation instance
            
        Example:
            >>> decoder = BitDecoder(bytes([0x1f, 0x03]))  # Character 'a'
            >>> op = Operation.from_fyve(0x1f, decoder)
            >>> op.kind == OperatingCode.CHARACTER
            True
            >>> op.get_char()
            Result.Ok('a')

    ### Methods

    `get_char(self) ‑> shdp.utils.result.Result[str, shdp.protocol.errors.Error]`
    :   Convert stored fyve values to a character using CHARS mapping.
        
        The method combines multiple 5-bit values into a single integer
        and looks up the corresponding character in the CHARS dictionary.
        
        Returns:
            Result[str, Error]: Decoded character string
            
        Raises:
            Error: If the computed value isn't in CHARS dictionary
            
        Example:
            >>> op = Operation(kind=OperatingCode.CHARACTER, 
            ...              code=None, 
            ...              values=[0x1f, 0x03])
            >>> op.get_char()
            Result.Ok('a')

`OperationCode(*args, **kwds)`
:   Operation codes for different SHDP protocol actions.
    
    Defines the specific operations that can be performed in SYSTEM mode:
    - UTF8_CHAIN: Handle UTF-8 encoded character sequences
    - START_OF_TAG: Begin a new XML/HTML tag
    - START_OF_ATTRIBUTE: Begin a tag attribute
    - START_OF_DATA: Begin data content
    - END_OF_DATA: End data content
    
    Examples:
        >>> op = OperationCode.from_fyve(0x10)
        >>> op == OperationCode.START_OF_TAG
        True

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `END_OF_DATA`
    :

    `START_OF_ATTRIBUTES`
    :

    `START_OF_DATA`
    :

    `START_OF_TAG`
    :

    `UNKNOWN`
    :

    `UTF8_CHAIN`
    :

    ### Static methods

    `from_fyve(fyve: int) ‑> Self`
    :   Convert a 5-bit value to an OperationCode.
        
        Args:
            fyve: 5-bit integer value representing the operation
            
        Returns:
            Corresponding OperationCode or UNKNOWN if value not recognized
            
        Example:
            >>> OperationCode.from_fyve(0x10)
            OperationCode.START_OF_TAG
            >>> OperationCode.from_fyve(0x18)
            OperationCode.START_OF_DATA

    ### Methods

    `to_fyve(self) ‑> int`
    :   Convert the OperationCode to its 5-bit representation.
        
        Returns:
            Integer value corresponding to the operation code
            
        Example:
            >>> OperationCode.START_OF_TAG.to_fyve()
            0x10
            >>> OperationCode.END_OF_DATA.to_fyve()
            0x19