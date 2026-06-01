METADATA = {
    "id": 284,
    "name": "Peeking Iterator",
    "slug": "peeking_iterator",
    "category": "Design",
    "aliases": [],
    "tags": ["iterator", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design an iterator that supports peeking at the next element without advancing the iterator.",
}

class PeekingIterator:
    """
    A wrapper for an iterator that allows peeking at the next element.
    """

    def __init__(self, iterator: iter):
        """
        Initializes the PeekingIterator with an underlying iterator.

        Args:
            iterator: The original iterator to wrap.
        """
        self.iterator = iterator
        self.next_element = None
        self.has_next_val = False
        
        # Pre-fetch the first element to prepare for peek/next operations
        self._advance()

    def _advance(self) -> None:
        """
        Internal helper to fetch the next element from the underlying iterator.
        """
        try:
            self.next_element = next(self.iterator)
            self.has_next_val = True
        except StopIteration:
            self.next_element = None
            self.has_next_val = False

    def next(self) -> int:
        """
        Returns the next element in the iterator.

        Returns:
            int: The next element.

        Raises:
            StopIteration: If there are no more elements.
        """
        if not self.has_next_val:
            raise StopIteration()

        # Capture current value to return, then advance the buffer
        current_val = self.next_element
        self._advance()
        return current_val

    def peek(self) -> int:
        """
        Returns the next element in the iterator without advancing it.

        Returns:
            int: The next element.

        Raises:
            StopIteration: If there are no more elements.
        """
        if not self.has_next_val:
            raise StopIteration()
        
        # Simply return the cached value without calling _advance()
        return self.next_element

    def hasNext(self) -> bool:
        """
        Checks if there are more elements in the iterator.

        Returns:
            bool: True if there are more elements, False otherwise.
        """
        return self.has_next_val

def solve(input_list: list[int]) -> None:
    """
    Example usage of the PeekingIterator.

    Args:
        input_list: A list of integers to be converted into an iterator.
    """
    it = iter(input_list)
    peeking_it = PeekingIterator(it)

    while peeking_it.hasNext():
        print(f"Peek: {peeking_it.peek()}")
        print(f"Next: {peeking_it.next()}")
