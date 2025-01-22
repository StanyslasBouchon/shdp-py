Module shdp.protocol.args
=========================

Classes
-------

`Arg(arg_type: int, value: Any = None)`
:   Class representing a typed argument with its associated value.
    
    Attributes:
        type (int): The argument type
        value (Any): The argument value
    
    Examples:
        >>> text_arg = Arg(Arg.TEXT, "Hello")
        >>> int_arg = Arg(Arg.INT, 42)
        >>> bool_arg = Arg(Arg.BOOL, True)
        >>> vec_arg = Arg(Arg.VEC_TEXT, ["a", "b", "c"])
        >>> opt_text_arg = Arg(Arg.OPT_TEXT, "optional")
        >>> opt_value_arg = Arg(Arg.OPT_VALUE, {"key": "value"})
    
    Initialize a new argument with its type and value.
    
    Args:
        arg_type (int): The argument type
        value (Any, optional): The argument value. Defaults to None.
    
    Examples:
        >>> text_arg = Arg(Arg.TEXT, "Hello")
        >>> int_arg = Arg(Arg.INT, 42)

    ### Class variables

    `BOOL`
    :

    `INT`
    :

    `OPT_TEXT`
    :

    `OPT_VALUE`
    :

    `TEXT`
    :

    `VEC_TEXT`
    :

    `type: int`
    :

    `value: Any`
    :

    ### Static methods

    `from_str(s: str) ‑> Self`
    :   Create an argument from a string by automatically determining its type.
        
        Args:
            s (str): The string to convert
        
        Returns:
            Self: A new Arg instance
        
        Examples:
            >>> Arg.from_str("42")        # Arg(INT, 42)
            >>> Arg.from_str("0xFF")      # Arg(INT, 255)
            >>> Arg.from_str("true")      # Arg(BOOL, True)
            >>> Arg.from_str("hello")     # Arg(TEXT, "hello")

    ### Methods

    `to_bool(self) ‑> shdp.utils.result.Result[bool, shdp.protocol.errors.Error]`
    :   Convert the argument to a boolean if its type is BOOL.
        
        Returns:
            bool: The boolean value
        
        Raises:
            ValueError: If the type is not BOOL
        
        Example:
            >>> Arg(Arg.BOOL, True).to_bool()  # True

    `to_int(self) ‑> shdp.utils.result.Result[int, shdp.protocol.errors.Error]`
    :   Convert the argument to an integer if its type is INT.
        
        Returns:
            int: The integer value
        
        Raises:
            ValueError: If the type is not INT
        
        Example:
            >>> Arg(Arg.INT, 42).to_int()  # 42

    `to_opt_text(self) ‑> shdp.utils.result.Result[str, shdp.protocol.errors.Error]`
    :   Convert the argument to an optional string if its type is OPT_TEXT.
        
        Returns:
            str | None: The string or None
        
        Raises:
            ValueError: If the type is not OPT_TEXT
        
        Examples:
            >>> Arg(Arg.OPT_TEXT, "hello").to_opt_text()  # "hello"
            >>> Arg(Arg.OPT_TEXT, None).to_opt_text()     # None

    `to_opt_value(self) ‑> shdp.utils.result.Result[dict | list, shdp.protocol.errors.Error]`
    :   Convert the argument to an optional complex value if its type is OPT_VALUE.
        
        Returns:
            Union[dict, list, None]: The complex value or None
        
        Raises:
            ValueError: If the type is not OPT_VALUE
        
        Examples:
            >>> Arg(Arg.OPT_VALUE, {"x": 1}).to_opt_value()  # {"x": 1}
            >>> Arg(Arg.OPT_VALUE, [1, 2]).to_opt_value()    # [1, 2]
            >>> Arg(Arg.OPT_VALUE, None).to_opt_value()      # None

    `to_string(self) ‑> shdp.utils.result.Result[str, shdp.protocol.errors.Error]`
    :   Convert the argument to a string.
        
        Returns:
            str: String representation of the argument
        
        Examples:
            >>> Arg(Arg.TEXT, "hello").to_string()           # "hello"
            >>> Arg(Arg.INT, 42).to_string()                 # "42"
            >>> Arg(Arg.BOOL, True).to_string()              # "true"
            >>> Arg(Arg.VEC_TEXT, ["a","b"]).to_string()     # "a,b"
            >>> Arg(Arg.OPT_VALUE, {"x":1}).to_string()      # '{"x":1}'

    `to_vec_text(self) ‑> shdp.utils.result.Result[list[str], shdp.protocol.errors.Error]`
    :   Convert the argument to a list of strings if its type is VEC_TEXT.
        
        Returns:
            list[str]: The list of strings
        
        Raises:
            ValueError: If the type is not VEC_TEXT
        
        Example:
            >>> Arg(Arg.VEC_TEXT, ["a", "b"]).to_vec_text()  # ["a", "b"]