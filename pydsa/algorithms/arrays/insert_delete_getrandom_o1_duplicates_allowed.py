METADATA = {
    "id": 381,
    "name": "Insert Delete GetRandom O(1) - Duplicates allowed",
    "slug": "insert-delete-getrandom-o1-duplicates-allowed",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "randomized", "design"],
    "difficulty": "hard",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a data structure that supports insert, remove, and getrandom elements in constant time, allowing duplicate values.",
}

import random

class RandomizedSet:
    """
    A data structure that supports insert, remove, and getrandom elements in O(1) time.
    This implementation handles duplicate values by mapping each value to a set of 
    indices where it resides in the internal list.
    """

    def __init__(self) -> None:
        """Initializes the data structure."""
        # Stores the actual elements to allow O(1) random access by index
        self.values_list: list[int] = []
        # Maps each value to a set of indices in values_list to allow O(1) lookup/removal
        self.value_to_indices: dict[int, set[int]] = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value into the set.

        Args:
            val: The integer value to insert.

        Returns:
            True if the value was not present, False otherwise.
        """
        if val in self.value_to_indices and self.value_to_indices[val]:
            return False
        
        # Add the value to the end of the list and record its index
        self.value_to_indices[val] = {len(self.values_list)}
        self.values_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. If duplicates were allowed via multiple 
        inserts, this removes one instance.

        Args:
            val: The integer value to remove.

        Returns:
            True if the value was present, False otherwise.
        """
        if val not in self.value_to_indices or not self.value_to_indices[val]:
            return False

        # Get an arbitrary index of the value to remove
        # pop() on a set is O(1)
        index_to_remove = self.value_to_indices[val].pop()
        
        # If the set for this value is now empty, remove the key from the dict
        if not self.value_to_indices[val]:
            del self.value_to_indices[val]

        last_element = self.values_list[-1]
        last_index = len(self.values_list) - 1

        # If the element to remove is not the last element, swap it with the last element
        if index_to_remove != last_index:
            # Move the last element to the position of the element being removed
            self.values_list[index_to_remove] = last_element
            
            # Update the index mapping for the moved element
            self.value_to_indices[last_element].remove(last_index)
            self.value_to_indices[last_element].add(index_to_remove)

        # Remove the last element from the list
        self.values_list.pop()
        return True

    def get_random(self) -> int:
        """
        Returns a random element from the set.

        Returns:
            A random integer from the set.
        """
        # random.choice on a list is O(1)
        return random.choice(self.values_list)

def solve() -> None:
    """
    Example usage of the RandomizedSet class.
    """
    rs = RandomizedSet()
    print(f"Insert 1: {rs.insert(1)}")  # True
    print(f"Insert 2: {rs.insert(2)}")  # True
    print(f"Get Random: {rs.get_random()}")
    print(f"Remove 1: {rs.remove(1)}")  # True
    print(f"Remove 1: {rs.remove(1)}")  # False
    print(f"Get Random: {rs.get_random()}")
