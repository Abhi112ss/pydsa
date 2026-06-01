METADATA = {
    "id": 702,
    "name": "Search in a Sorted Array of Unknown Size",
    "slug": "search-in-a-sorted-array-of-unknown-size",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "exponential_search"],
    "difficulty": "medium",
    "time_complexity": "O(log T)",
    "space_complexity": "O(1)",
    "description": "Find the index of a target value in a sorted array where the size is unknown, using an interface that provides access to elements.",
}

class ArrayReader:
    """
    A mock interface provided by the problem description.
    In a real LeetCode environment, this class is pre-implemented.
    """
    def __init__(self, arr: list[int]):
        self.arr = arr

    def get(self, index: int) -> int:
        if index >= len(self.arr):
            return 2147483647  # Represents infinity as per problem constraints
        return self.arr[index]

def solve(reader: ArrayReader, target: int) -> int:
    """
    Searches for a target value in a sorted array of unknown size.

    Args:
        reader: An instance of ArrayReader providing access to the array elements.
        target: The integer value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Examples:
        >>> reader = ArrayReader([1, 2, 3, 4, 5])
        >>> solve(reader, 3)
        2
        >>> solve(reader, 6)
        -1
    """
    # Step 1: Find the search boundaries using exponential growth.
    # We double the index until the value at that index is greater than or equal to the target.
    # This ensures we find a range [left, right] containing the target in O(log T) time.
    left = 0
    right = 1
    
    while reader.get(right) < target:
        left = right
        right *= 2

    # Step 2: Perform a standard binary search within the identified range [left, right].
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = reader.get(mid)

        if mid_val == target:
            return mid
        elif mid_val > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
