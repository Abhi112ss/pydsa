METADATA = {
    "id": 1095,
    "name": "Find in Mountain Array",
    "slug": "find-in-mountain-array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "array"],
    "difficulty": "hard",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the index of a target value in a mountain array using a limited number of calls to the auto-complete search interface.",
}

class MountainArray:
    """
    This class is provided by LeetCode. 
    It is included here for type hinting and structural completeness.
    """
    def get(self, index: int) -> int:
        raise NotImplementedError

    def length(self) -> int:
        raise NotImplementedError

def solve(mountain_arr: MountainArray, target: int) -> int:
    """
    Finds the index of the target in a mountain array.

    Args:
        mountain_arr: An instance of MountainArray providing get() and length().
        target: The integer value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Examples:
        >>> # Assuming mountain_arr is [1, 3, 5, 4, 2] and target is 4
        >>> solve(mountain_arr, 4)
        3
    """
    n = mountain_arr.length()
    
    # 1. Find the peak index using binary search
    # The peak is the index i where mountain_arr[i] > mountain_arr[i+1]
    low = 0
    high = n - 1
    peak_index = 0
    
    while low <= high:
        mid = (low + high) // 2
        # Check if mid is not the last element to avoid index out of bounds
        if mid < n - 1 and mountain_arr.get(mid) < mountain_arr.get(mid + 1):
            # We are in the ascending part, peak is to the right
            low = mid + 1
        else:
            # We are in the descending part or at the peak
            peak_index = mid
            high = mid - 1

    # 2. Binary search on the ascending part [0, peak_index]
    low = 0
    high = peak_index
    while low <= high:
        mid = (low + high) // 2
        val = mountain_arr.get(mid)
        if val == target:
            return mid
        elif val < target:
            low = mid + 1
        else:
            high = mid - 1

    # 3. Binary search on the descending part [peak_index + 1, n - 1]
    low = peak_index + 1
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        val = mountain_arr.get(mid)
        if val == target:
            return mid
        elif val > target:
            # In descending part, if val is larger than target, target is to the right
            low = mid + 1
        else:
            # If val is smaller than target, target is to the left
            high = mid - 1

    return -1