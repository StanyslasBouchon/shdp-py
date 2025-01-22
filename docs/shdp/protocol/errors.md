Module shdp.protocol.errors
===========================
Error handling for SHDP protocol.

This module provides error types and handling for the SHDP protocol,
including standard error kinds and custom error creation.

Classes
-------

`Error(code: int, kind: shdp.protocol.errors.ErrorKind, message: str)`
:   Represents an error in the SHDP protocol.
    
    This class combines an error code, kind, and message to provide detailed
    error information for protocol operations.
    
    Attributes:
        code (int): Numeric error code
        kind (ErrorKind): The category of error
        message (str): Detailed error message
        
    Examples:
        >>> # Create a not found error
        >>> error = Error(404, ErrorKind.NOT_FOUND, "User profile not found")
        >>> str(error)
        'Error: [NotFound]:404 -> User profile not found'
        
        >>> # Create a custom error
        >>> custom = Error(
        ...     500,
        ...     ErrorKind.USER_DEFINED,
        ...     "Database connection failed"
        ... )
        >>> str(custom)
        'Error: [UserDefined]:500 -> Database connection failed'
    
    Initialize a new Error instance.
    
    Args:
        code: Numeric error code
        kind: Category of the error
        message: Detailed error description

    ### Static methods

    `new(kind: shdp.protocol.errors.ErrorKind, message: str) ‑> shdp.protocol.errors.Error`
    :   Create a new Error instance with an automatically assigned code.
        
        Args:
            kind: The error kind
            message: Detailed error message
            
        Returns:
            Error: A new Error instance
            
        Examples:
            >>> error = Error.new(ErrorKind.NOT_FOUND, "User not found")
            >>> str(error)
            'Error: [NotFound]:404 -> User not found'
            
            >>> custom = Error.new(ErrorKind.USER_DEFINED, "Custom error")
            >>> str(custom)
            'Error: [UserDefined]:500 -> Custom error'

`ErrorKind(*args, **kwds)`
:   Enumeration of standard error types in the SHDP protocol.
    
    This enum defines standard error categories that can occur during protocol
    operations. Each error kind maps to a specific error scenario.
    
    Examples:
        >>> error = ErrorKind.NOT_FOUND
        >>> str(error)
        'NotFound'
        >>> custom_error = ErrorKind.USER_DEFINED("Custom error message")
        >>> str(custom_error)
        'Custom error message'

    ### Ancestors (in MRO)

    * enum.Enum

    ### Class variables

    `BAD_REQUEST`
    :

    `CANCELLED`
    :

    `CONFLICT`
    :

    `EXPECTATION_FAILED`
    :

    `EXPIRED`
    :

    `FORBIDDEN`
    :

    `GONE`
    :

    `LOCKED`
    :

    `METHOD_NOT_ALLOWED`
    :

    `NOT_FOUND`
    :

    `NOT_IMPLEMENTED`
    :

    `NO_RESPONSE`
    :

    `PAYMENT_REQUIRED`
    :

    `PROTOCOL_ERROR`
    :

    `REQUESTED_RANGE_NOT_SATISFIABLE`
    :

    `REQUEST_ENTITY_TOO_LARGE`
    :

    `REQUEST_TIMEOUT`
    :

    `SERVICE_UNAVAILABLE`
    :

    `SIZE_CONSTRAINT_VIOLATION`
    :

    `UNAUTHORIZED`
    :

    `UNKNOWN_VERSION`
    :

    `USER_DEFINED`
    :