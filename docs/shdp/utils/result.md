Module shdp.utils.result
========================
Result type implementation for handling success and error cases.

This module provides a generic Result type that can be used to handle operations
that might fail, similar to Rust's Result type.

Classes
-------

`Result(value: ~T | ~E, is_ok: bool)`
:   A generic Result type that represents either a success value of type T or an error value of type E.
    
    This implementation includes a context manager-like system to collect errors from all Result instances,
    regardless of their success type T.
    
    Attributes:
        _hidden_results (list[Result[Any, E]]): Collects all Result instances when hiding is active
        _is_hiding (bool): Indicates if result collection is active
    
    Initialize a Result instance.

    ### Ancestors (in MRO)

    * typing.Generic

    ### Static methods

    `Err(value: ~E) ‑> shdp.utils.result.Result[~T, ~E]`
    :   Create an error Result with the given error value.

    `Ok(value: ~T) ‑> shdp.utils.result.Result[~T, ~E]`
    :   Create a success Result with the given value.

    `all(results: list['Result[Any, E]']) ‑> shdp.utils.result.Result[list[typing.Any], ~E]`
    :   Aggregate multiple Results into a single Result.

    `hide() ‑> None`
    :   Start collecting all Result instances silently.

    `reveal() ‑> shdp.utils.result.Result[None, ~E]`
    :   Check all collected results and return the final result.

    ### Methods

    `is_err(self) ‑> bool`
    :   Check if this Result contains an error value.

    `is_ok(self) ‑> bool`
    :   Check if this Result contains a success value.

    `unwrap(self) ‑> ~T`
    :   Extract the success value from this Result.

    `unwrap_err(self) ‑> ~E`
    :   Extract the error value from this Result.