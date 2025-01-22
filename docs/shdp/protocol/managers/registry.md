Module shdp.protocol.managers.registry
======================================

Classes
-------

`EventRegistry()`
:   Registry for managing protocol events and their listeners.
    
    This class maintains two registries:
    - events: Maps event IDs to their handler functions
    - listeners: Maps event IDs to their listener functions
    
    Examples:
        >>> registry = EventRegistry()
        >>> event_id = (1, 0)  # v1.0
        
        # Register an event handler
        >>> def handle_login(decoder: BitDecoder[R]) -> Type[LoginEvent]:
        ...     return LoginEvent
        >>> registry.add_event(event_id, handle_login)
        
        # Register an event listener
        >>> def on_login(event: Type[LoginEvent]) -> list[Arg]:
        ...     return [Arg(Arg.TEXT, "user123")]
        >>> registry.add_listener(event_id, on_login)
    
    Initialize a new event registry.

    ### Ancestors (in MRO)

    * shdp.protocol.managers.bits.lib.BitReversible
    * abc.ABC
    * typing.Generic

    ### Class variables

    `events: dict[tuple[int, int], list[typing.Callable[[shdp.protocol.managers.bits.decoder.BitDecoder[~R]], typing.Type[~E]]]]`
    :

    `listeners: dict[tuple[int, int], list[typing.Callable[[typing.Type[~E]], list[shdp.protocol.args.Arg]]]]`
    :

    ### Methods

    `add_event(self, event_id: tuple[int, int], event_fn: Callable[[shdp.protocol.managers.bits.decoder.BitDecoder[~R]], Type[~E]]) ‑> None`
    :   Register a new event handler for a specific event ID.
        
        Args:
            event_id (EventId): The event identifier (major, minor)
            event_fn (EventFn): The event handler function
        
        Example:
            >>> def handle_message(decoder: BitDecoder[R]) -> Type[MessageEvent]:
            ...     return MessageEvent
            >>> registry.add_event((1, 0), handle_message)

    `add_listener(self, event_id: tuple[int, int], listener_fn: Callable[[Type[~E]], list[shdp.protocol.args.Arg]]) ‑> None`
    :   Register a new event listener for a specific event ID.
        
        Args:
            event_id (EventId): The event identifier (major, minor)
            listener_fn (ListenerFn): The listener function
        
        Example:
            >>> def on_message(event: Type[MessageEvent]) -> list[Arg]:
            ...     return [Arg(Arg.TEXT, "Hello!")]
            >>> registry.add_listener((1, 0), on_message)

    `get_event(self, event_id: tuple[int, int]) ‑> list[typing.Callable[[shdp.protocol.managers.bits.decoder.BitDecoder[~R]], typing.Type[~E]]] | None`
    :   Get all event handlers for a specific event ID.
        
        Args:
            event_id (EventId): The event identifier (major, minor)
        
        Returns:
            list[EventFn] | None: List of event handlers or None if not found
        
        Example:
            >>> handlers = registry.get_event((1, 0))
            >>> if handlers:
            ...     for handler in handlers:
            ...         event = handler(decoder)

    `get_listeners(self, event_id: tuple[int, int]) ‑> list[typing.Callable[[typing.Type[~E]], list[shdp.protocol.args.Arg]]] | None`
    :   Get all listeners for a specific event ID.
        
        Args:
            event_id (EventId): The event identifier (major, minor)
        
        Returns:
            list[ListenerFn] | None: List of event listeners or None if not found
        
        Example:
            >>> listeners = registry.get_listeners((1, 0))
            >>> if listeners:
            ...     for listener in listeners:
            ...         args = listener(event)