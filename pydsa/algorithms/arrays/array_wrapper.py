METADATA = {
    "id": 2695,
    "name": "Array Wrapper",
    "slug": "array-wrapper",
    "category": "Design",
    "aliases": [],
    "tags": ["design_patterns", "array"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design a class that wraps an array and provides methods to access elements and the array length.",
}

class ArrayWrapper:
    """
    A class that encapsulates an array and provides methods to interact with it.

    Attributes:
        array (list[int]): The internal list being wrapped.
    """

    def __init__(self, array: list[int]) -> None:
        """
        Initializes the ArrayWrapper with a given array.

        Args:
            array (list[int]): The list of integers to wrap.
        """
        self.array = array

    def length(self) -> int:
        """
        Returns the length of the wrapped array.

        Returns:
            int: The number of elements in the array.
        """
        # Return the length of the internal list in O(1) time
        return len(self.array)

    def isEmpty(self) -> bool:
        """
        Checks if the wrapped array is empty.

        Returns:
            bool: True if the array has no elements, False otherwise.
        """
        # Check if the length is zero
        return self.length() == 0

    def at(self, index: int) -> int:
        """
        Returns the element at the specified index.

        Args:
            index (int): The zero-based index of the element to retrieve.

        Returns:
            int: The value at the given index.

        Raises:
            IndexError: If the index is out of the array's bounds.
        """
        # Access the element directly via the internal list reference
        return self.array[index]

def solve() -> None:
    """
    Example usage of the ArrayWrapper class.
    """
    # Example 1
    wrapper1 = ArrayWrapper([1, 2, 3])
    print(f"Length: {wrapper1.length()}")  # Expected: 3
    print(f"Is Empty: {wrapper1.isEmpty()}")  # Expected: False
    print(f"At index 1: {wrapper1.at(1)}")  # Expected: 2

    # Example 2
    wrapper2 = ArrayWrapper([])
    print(f"Length: {wrapper2.length()}")  # Expected: 0
    print(f"Is Empty: {wrapper2.isEmpty()}")  # Expected: True
