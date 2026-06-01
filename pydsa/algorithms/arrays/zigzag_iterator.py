METADATA = {
    "id": 281,
    "name": "Zigzag Iterator",
    "slug": "zigzag_iterator",
    "category": "Design",
    "aliases": [],
    "tags": ["iterator", "design", "queue"],
    "difficulty": "medium",
    "time_complexity": "O(1) per next() call, O(k) space where k is number of vectors",
    "space_complexity": "O(k)",
    "description": "Design an iterator that returns elements from a list of lists in a zigzag manner.",
}

from collections import deque


class ZigzagIterator:
    """
    An iterator that traverses multiple lists in a zigzag fashion.
    
    Example:
        Input: vectors = [[1, 2], [3], [4, 5, 6]]
        Output: 1 -> 3 -> 4 -> 2 -> 5 -> 6
    """

    def __init__(self, vectors: list[list[int]]):
        """
        Initializes the iterator with a list of lists.

        Args:
            vectors: A list of integer lists.
        """
        # We use a queue to store iterators of the non-empty lists.
        # This allows us to cycle through the lists in O(1) per element.
        self.queue: deque[int] = deque()
        
        # We store the current index for each list to track progress.
        # Alternatively, we can store (list_index, element_index) pairs.
        # To keep it clean, we store (list_ref, current_index) in the queue.
        self.active_iterators: deque[tuple[list[int], int]] = deque()
        
        for vec in vectors:
            if vec:
                self.active_iterators.append((vec, 0))

    def next(self) -> int:
        """
        Returns the next element in the zigzag sequence.

        Returns:
            The next integer in the zigzag order.

        Raises:
            StopIteration: If there are no more elements.
        """
        if not self.active_iterators:
            raise StopIteration()

        # Get the first list in the queue
        current_vec, current_idx = self.active_iterators.popleft()
        
        # Retrieve the value to return
        value = current_vec[current_idx]
        
        # If the current list has more elements, put it back at the end of the queue
        next_idx = current_idx + 1
        if next_idx < len(current_vec):
            self.active_iterators.append((current_vec, next_idx))
            
        return value

    def hasNext(self) -> bool:
        """
        Checks if there are more elements in the zigzag sequence.

        Returns:
            True if an element exists, False otherwise.
        """
        return len(self.active_iterators) > 0


def solve():
    """
    Example usage of the ZigzagIterator.
    """
    vectors = [[1, 2], [3], [4, 5, 6]]
    iterator = ZigzagIterator(vectors)
    result = []
    while iterator.hasNext():
        result.append(iterator.next())
    
    print(f"Input: {vectors}")
    print(f"Output: {result}")
    assert result == [1, 3, 4, 2, 5, 6]
