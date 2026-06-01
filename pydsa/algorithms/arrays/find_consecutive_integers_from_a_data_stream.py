METADATA = {
    "id": 2526,
    "name": "Find Consecutive Integers from a Data Stream",
    "slug": "find-consecutive-integers-from-a-data-stream",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_set", "design", "data_stream"],
    "difficulty": "medium",
    "time_complexity": "O(1) average for add, O(k) for check where k is window size",
    "space_complexity": "O(n) where n is the number of elements added",
    "description": "Design a class that tracks a stream of integers and checks if a consecutive sequence of a given length exists.",
}

class ConsecutiveIntegerFinder:
    """
    A class to track integers from a stream and check for consecutive sequences.
    """

    def __init__(self, window_size: int):
        """
        Initializes the finder with a specific window size.

        Args:
            window_size (int): The length of the consecutive sequence to look for.
        """
        self.window_size = window_size
        self.seen_numbers: set[int] = set()

    def add(self, num: int) -> None:
        """
        Adds a number from the stream to the set of seen numbers.

        Args:
            num (int): The integer to add.
        """
        self.seen_numbers.add(num)

    def check(self, start: int, end: int) -> bool:
        """
        Checks if all integers in the range [start, end] exist in the stream.

        Args:
            start (int): The starting integer of the range.
            end (int): The ending integer of the range.

        Returns:
            bool: True if all integers in [start, end] are present, False otherwise.

        Examples:
            >>> finder = ConsecutiveIntegerFinder(3)
            >>> finder.add(4)
            >>> finder.add(2)
            >>> finder.add(3)
            >>> finder.check(2, 4)
            True
            >>> finder.check(1, 3)
            False
        """
        # The problem defines the check as whether the range [start, end] 
        # is fully contained within the set of seen numbers.
        # Since we only care about the specific range provided, 
        # we iterate through the range and check existence in the hash set.
        for current_val in range(start, end + 1):
            if current_val not in self.seen_numbers:
                return False
        return True

def solve():
    """
    Example usage of the ConsecutiveIntegerFinder class.
    """
    # Example 1
    finder = ConsecutiveIntegerFinder(3)
    finder.add(4)
    finder.add(2)
    finder.add(3)
    print(f"Check [2, 4]: {finder.check(2, 4)}")  # Expected: True
    print(f"Check [1, 3]: {finder.check(1, 3)}")  # Expected: False

    # Example 2
    finder2 = ConsecutiveIntegerFinder(3)
    finder2.add(1)
    finder2.add(2)
    print(f"Check [1, 3]: {finder2.check(1, 3)}")  # Expected: False
    finder2.add(3)
    print(f"Check [1, 3]: {finder2.check(1, 3)}")  # Expected: True
