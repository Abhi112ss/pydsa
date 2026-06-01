METADATA = {
    "id": 380,
    "name": "Insert Delete GetRandom O(1)",
    "slug": "insert-delete-getrandom-o1",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a data structure that supports insert, delete, and get_random operations in average O(1) time complexity.",
}

class RandomizedSet:
    """
    A data structure that supports insert, delete, and get_random operations in O(1) time.
    
    Uses a combination of a list (for O(1) random access) and a dictionary 
    (for O(1) lookup and index tracking).
    """

    def __init__(self) -> None:
        """Initializes the data structure."""
        self.data_list: list[int] = []
        self.val_to_index: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set if not present.

        Args:
            val: The integer to insert.

        Returns:
            True if the item was not present, False otherwise.
        """
        if val in self.val_to_index:
            return False
        
        # Store the index where the value will be placed
        self.val_to_index[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set if present.

        Args:
            val: The integer to remove.

        Returns:
            True if the item was present, False otherwise.
        """
        if val not in self.val_to_index:
            return False

        # To achieve O(1) removal in a list, swap the element to be deleted 
        # with the last element in the list, then pop the last element.
        index_to_remove = self.val_to_index[val]
        last_element = self.data_list[-1]

        # Move the last element to the position of the element we want to remove
        self.data_list[index_to_remove] = last_element
        self.val_to_index[last_element] = index_to_remove

        # Remove the last element from both structures
        self.data_list.pop()
        del self.val_to_index[val]
        
        return True

    def get_random(self) -> int:
        """
        Returns a random element from the current set.

        Returns:
            A random integer from the set.
        """
        import random
        # Since data_list contains all elements, we can pick a random index in O(1)
        return random.choice(self.data_list)

def solve() -> None:
    """
    Example usage of the RandomizedSet class.
    """
    import random
    
    # Test Case 1
    rs = RandomizedSet()
    print(f"Insert 1: {rs.insert(1)}")  # True
    print(f"Insert 2: {rs.insert(2)}")  # True
    print(f"Get Random: {rs.get_random()}") # 1 or 2
    print(f"Remove 1: {rs.remove(1)}")  # True
    print(f"Get Random: {rs.get_random()}") # 2
    print(f"Insert 1: {rs.insert(1)}")  # True
    print(f"Get Random: {rs.get_random()}") # 1 or 2
    print(f"Remove 2: {rs.remove(2)}")  # True
    print(f"Remove 2: {rs.remove(2)}")  # False
