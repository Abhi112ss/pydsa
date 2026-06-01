METADATA = {
    "id": 251,
    "name": "Flatten 2D Vector",
    "slug": "flatten-2d-vector",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "iterator", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(1) average for hasNext and next",
    "space_complexity": "O(1)",
    "description": "Implement an iterator to flatten a 2D vector.",
}

class Flatten2DVector:
    """
    An iterator that flattens a 2D vector into a 1D stream.
    """

    def __init__(self, vec: list[list[int]]):
        """
        Initializes the iterator with a 2D vector.

        Args:
            vec: A list of lists of integers.
        """
        self.vector = vec
        self.outer_index = 0
        self.inner_index = 0

    def next(self) -> int:
        """
        Returns the next element in the flattened vector.

        Returns:
            The next integer in the sequence.

        Raises:
            StopIteration: If there are no more elements.
        """
        # hasNext() is called before next() in standard iterator usage,
        # but we ensure the pointers are valid here as a safety measure.
        if not self.hasNext():
            raise StopIteration()
        
        value = self.vector[self.outer_index][self.inner_index]
        self.inner_index += 1
        return value

    def hasNext(self) -> bool:
        """
        Checks if there are more elements in the flattened vector.

        Returns:
            True if there is at least one more element, False otherwise.
        """
        # Advance the outer_index if the current inner list is exhausted
        # or if the current inner list is empty.
        while self.outer_index < len(self.vector):
            if self.inner_index < len(self.vector[self.outer_index]):
                return True
            
            # Move to the next list in the 2D vector and reset inner index
            self.outer_index += 1
            self.inner_index = 0
            
        return False

def solve():
    """
    Example usage of the Flatten2DVector class.
    """
    vec = [[1, 2], [], [3], [4, 5, 6]]
    iterator = Flatten2DVector(vec)
    
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    
    print(f"Input: {vec}")
    print(f"Flattened: {result}")
    assert result == [1, 2, 3, 4, 5, 6]
