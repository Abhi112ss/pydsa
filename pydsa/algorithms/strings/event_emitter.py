METADATA = {
    "id": 2694,
    "name": "Event Emitter",
    "slug": "event_emitter",
    "category": "Design",
    "aliases": [],
    "tags": ["design_patterns", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(1) for emit/on/off, O(k) for emit where k is number of listeners",
    "space_complexity": "O(n) where n is the number of registered listeners",
    "description": "Design an EventEmitter class that supports on, emit, and off methods.",
}

class EventEmitter:
    """
    A class that implements a simple event emitter pattern.
    
    Attributes:
        listeners (dict[str, list[callable]]): A mapping of event names to lists of callback functions.
    """

    def __init__(self) -> None:
        """Initializes the EventEmitter with an empty listener map."""
        self.listeners: dict[str, list[callable]] = {}

    def on(self, event_name: str, listener: callable) -> None:
        """
        Registers a callback function for a specific event.

        Args:
            event_name (str): The name of the event to listen for.
            listener (callable): The function to be called when the event is emitted.
        """
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def emit(self, event_name: str, *args: any) -> any:
        """
        Triggers all callbacks registered for the given event name.

        Args:
            event_name (str): The name of the event to emit.
            *args: Variable length argument list to pass to the listeners.

        Returns:
            any: The result of the last listener's execution, or None if no listeners exist.
        """
        if event_name not in self.listeners:
            return None
        
        last_result = None
        # Iterate through a copy of the list to prevent issues if a listener 
        # unregisters itself during the emission process.
        for listener in self.listeners[event_name][:]:
            last_result = listener(*args)
        
        return last_result

    def off(self, event_name: str, listener: callable) -> None:
        """
        Removes a specific callback function from an event.

        Args:
            event_name (str): The name of the event.
            listener (callable): The specific function to remove.
        """
        if event_name in self.listeners:
            # Remove the listener if it exists in the list
            try:
                self.listeners[event_name].remove(listener)
            except ValueError:
                # Listener not found in the list, ignore
                pass
            
            # Clean up the dictionary key if no listeners remain
            if not self.listeners[event_name]:
                del self.listeners[event_name]

def solve() -> None:
    """
    Example usage of the EventEmitter class.
    """
    emitter = EventEmitter()

    def fn1(x: int, y: int) -> int:
        return x + y

    def fn2(x: int, y: int) -> int:
        return x * y

    # Test 'on' and 'emit'
    emitter.on("add", fn1)
    emitter.on("add", fn2)
    # Should return the result of the last listener (fn2): 3 * 4 = 12
    print(f"Emit 'add' with (3, 4): {emitter.emit('add', 3, 4)}") 

    # Test 'off'
    emitter.off("add", fn1)
    # Should return the result of the remaining listener (fn2): 3 * 4 = 12
    print(f"Emit 'add' after removing fn1: {emitter.emit('add', 3, 4)}")

    # Test 'off' non-existent
    emitter.off("add", fn1) 
    
    # Test empty event
    print(f"Emit non-existent event: {emitter.emit('none')}")
