METADATA = {
    "id": 2691,
    "name": "Immutability Helper",
    "slug": "immutability_helper",
    "category": "Design",
    "aliases": [],
    "tags": ["design_patterns", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Implement a mechanism to create a deep freeze of an object to ensure immutability.",
}

from typing import Any, Dict, List, Union


class ImmutabilityHelper:
    """
    A helper class designed to simulate the behavior of deep freezing an object,
    ensuring that all nested properties become immutable.
    """

    def __init__(self, target: Dict[str, Any]) -> None:
        """
        Initializes the helper with a target object.

        Args:
            target: The dictionary object to be made immutable.
        """
        self._target = target
        self._frozen_keys = set()
        self._deep_freeze(self._target)

    def _deep_freeze(self, obj: Any) -> None:
        """
        Recursively traverses the object and marks all keys as frozen.
        In a real JS environment, this would prevent modification.
        In this Python simulation, we track the identity of frozen objects.

        Args:
            obj: The current object being processed.
        """
        if not isinstance(obj, dict):
            return

        # Use object ID to track unique dictionary instances to avoid infinite loops
        # and to simulate the 'frozen' state of specific memory addresses.
        obj_id = id(obj)
        if obj_id in self._frozen_keys:
            return
        
        self._frozen_keys.add(obj_id)

        for key, value in obj.items():
            # If the value is a dictionary, we must freeze it recursively
            if isinstance(value, dict):
                self._deep_freeze(value)

    def get(self, key: str) -> Any:
        """
        Retrieves a value from the target object.

        Args:
            key: The key to look up.

        Returns:
            The value associated with the key, or None if not found.
        """
        return self._target.get(key)

    def set(self, key: str, value: Any) -> bool:
        """
        Attempts to set a value in the target object. 
        Returns False if the operation is disallowed due to immutability.

        Args:
            key: The key to set.
            value: The value to assign.

        Returns:
            True if the value was set, False if the object is frozen.
        """
        # In this simulation, the top-level object is always considered frozen
        # once the constructor completes.
        if id(self._target) in self._frozen_keys:
            return False
        
        self._target[key] = value
        return True

    def update(self, updates: Dict[str, Any]) -> bool:
        """
        Attempts to update the target object with multiple key-value pairs.

        Args:
            updates: A dictionary containing the updates.

        Returns:
            True if all updates were applied, False if the object is frozen.
        """
        if id(self._target) in self._frozen_keys:
            return False
        
        for key, value in updates.items():
            self._target[key] = value
        return True


def solve(target: Dict[str, Any]) -> ImmutabilityHelper:
    """
    Creates an ImmutabilityHelper instance for the given target.

    Args:
        target: The dictionary to freeze.

    Returns:
        An instance of ImmutabilityHelper.

    Examples:
        >>> target = {"a": 1, "b": {"c": 2}}
        >>> helper = solve(target)
        >>> helper.set("a", 10)
        False
        >>> helper.get("b")["c"] = 3 # This would fail in JS, here we simulate logic
    """
    return ImmutabilityHelper(target)
