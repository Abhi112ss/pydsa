METADATA = {
    "id": 35,
    "name": "Search Insert Position",
    "slug": "search-insert-position",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Finds the index of the target in a sorted list or the index where it should be inserted.

    Args:
        nums: A list of sorted distinct integers.
        target: The integer value to search for.

    Returns:
        The index of the target if found, otherwise the index where it would be inserted.

    Examples:
        >>> solve([1, 3, 5, 6], 5)
        2
        >>> solve([1, 3, 5, 6], 2)
        1
        >>> solve([1, 3, 5, 6], 7)
        4
        >>> solve([1, 3, 5, 6], 0)
        0
    """
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        # Calculate mid using floor division to avoid overflow in other languages
        # though Python handles arbitrarily large integers automatically.
        mid_index = left_index + (right_index - left_index) // 2
        
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] < target:
            # Target is in the right half
            left_index = mid_index + 1
        else:
            # Target is in the left half
            right_index = mid_index - 1

    # If the loop terminates, left_index represents the insertion point
    # because it is the smallest index such that nums[index] > target.
    return left_index
