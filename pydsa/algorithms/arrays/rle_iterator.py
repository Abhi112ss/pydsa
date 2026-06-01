METADATA = {
    "id": 900,
    "name": "RLE Iterator",
    "slug": "rle-iterator",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "simulation", "two-pointers"],
    "difficulty": "medium",
    "time_complexity": "O(1) amortized per next() call, O(1) for integer()",
    "space_complexity": "O(1)",
    "description": "Implement an iterator that processes a run-length encoded array by skipping elements.",
}

class RLEIterator:
    def __init__(self, encodedArray: list[int]):
        """
        Initializes the iterator with the encoded array.

        Args:
            encodedArray (list[int]): A list of integers where even indices represent 
                                     counts and odd indices represent values.
        """
        self.encoded_array = encodedArray
        self.current_index = 0  # Points to the current count index (even index)
        self.remaining_count = 0 if not encodedArray else encodedArray[0]

    def next(self, n: int) -> bool:
        """
        Skips n elements in the decoded array.

        Args:
            n (int): The number of elements to skip.

        Returns:
            bool: True if there are at least n elements left, False otherwise.

        Examples:
            >>> it = RLEIterator([3, 2, 2, 1])
            >>> it.next(1)
            True
            >>> it.next(3)
            False
        """
        # While we still need to skip elements and we haven't exhausted the array
        while n > 0 and self.current_index < len(self.encoded_array):
            if self.remaining_count >= n:
                # If the current run has enough elements to satisfy the skip
                self.remaining_count -= n
                n = 0
            else:
                # If the current run is exhausted, move to the next run
                n -= self.remaining_count
                self.current_index += 2
                if self.current_index < len(self.encoded_array):
                    self.remaining_count = self.encoded_array[self.current_index]
                else:
                    self.remaining_count = 0
        
        # If n is 0, it means we successfully skipped n elements
        return n == 0

def solve():
    """
    Example usage of the RLEIterator.
    """
    # Test Case 1
    it1 = RLEIterator([3, 2, 2, 1])
    print(it1.next(1))  # Expected: True
    print(it1.next(3))  # Expected: False

    # Test Case 2
    it2 = RLEIterator([1, 1, 1, 1, 1, 1])
    print(it2.next(2))  # Expected: True
    print(it2.next(3))  # Expected: True
    print(it2.next(1))  # Expected: False
