METADATA = {
    "id": 2692,
    "name": "Make Object Immutable",
    "slug": "make-object-immutable",
    "category": "Design",
    "aliases": [],
    "tags": ["design_patterns", "recursion", "object-oriented"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Implement a class that makes a given object immutable by recursively freezing all nested objects.",
}

class Immutable:
    """
    A wrapper class that makes an object immutable.
    
    Attributes:
        obj: The original object being wrapped.
    """
    def __init__(self, obj: object):
        # Use object.__setattr__ to avoid triggering __setattr__ of the wrapped object
        # and to allow setting the internal 'obj' attribute during initialization.
        object.__setattr__(self, "obj", self._freeze(obj))

    def _freeze(self, value: object) -> object:
        """
        Recursively traverses the object and makes all nested objects immutable.
        
        Args:
            value: The object or value to be frozen.
            
        Returns:
            The frozen version of the object.
        """
        # If the value is a dictionary, create a new dictionary where all values are frozen
        if isinstance(value, dict):
            return {k: self._freeze(v) for k, v in value.items()}
        
        # If the value is a list, create a new list where all elements are frozen
        elif isinstance(value, list):
            return [self._freeze(item) for item in value]
        
        # If the value is a custom object (not a primitive), we wrap it in an Immutable instance
        # We check for __dict__ to identify user-defined objects vs primitives
        elif hasattr(value, "__dict__"):
            return Immutable(value)
        
        # For primitives (int, str, bool, None, etc.), they are already immutable in Python
        return value

    def __getattr__(self, name: str) -> object:
        """Redirects attribute access to the underlying frozen object."""
        return getattr(self.obj, name)

    def __getitem__(self, key: object) -> object:
        """Redirects item access (for dicts/lists) to the underlying frozen object."""
        return self.obj[key]

    def __setattr__(self, name: str, value: object) -> None:
        """Prevents any modification to the Immutable wrapper."""
        raise AttributeError("This object is immutable")

    def __delattr__(self, name: str) -> None:
        """Prevents deletion of attributes from the Immutable wrapper."""
        raise AttributeError("This object is immutable")

    def __setitem__(self, key: object, value: object) -> None:
        """Prevents modification of items in the underlying collection."""
        raise AttributeError("This object is immutable")

    def __delitem__(self, key: object) -> None:
        """Prevents deletion of items in the underlying collection."""
        raise AttributeError("This object is immutable")


def solve(obj: object) -> Immutable:
    """
    Creates an immutable version of the provided object.

    Args:
        obj: The object to make immutable.

    Returns:
        An Immutable instance wrapping the original object.

    Examples:
        >>> class Person:
        ...     def __init__(self, name): self.name = name
        >>> p = Person("Alice")
        >>> imm = solve(p)
        >>> imm.name
        'Alice'
        >>> imm.name = "Bob"
        Traceback (most recent call last):
            ...
        AttributeError: This object is immutable
    """
    return Immutable(obj)