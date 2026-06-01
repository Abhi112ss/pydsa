METADATA = {
    "id": 2811,
    "name": "Check if it is Possible to Split Array",
    "slug": "check-if-it-is-possible-to-split-array",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be split into two non-empty parts such that all elements in the first part are strictly increasing and all elements in the second part are strictly decreasing.",
}

def solve(nums: list[int]) -> bool:
    """
    Checks if the array can be split into two non-empty parts where the first 
    part is strictly increasing and the second part is strictly decreasing.

    Args:
        nums: A list of integers.

    Returns:
        True if such a split exists, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 3, 2, 1])
        True
        >>> solve([1, 2, 3, 4, 5])
        False
        >>> solve([5, 4, 3, 2, 1])
        False
    """
    n = len(nums)
    if n < 2:
        return False

    # is_increasing[i] will be True if nums[0...i] is strictly increasing
    is_increasing = [False] * n
    is_increasing[0] = True
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            is_increasing[i] = True
        else:
            # Once the increasing property is broken, all subsequent indices are False
            break

    # is_decreasing[i] will be True if nums[i...n-1] is strictly decreasing
    is_decreasing = [False] * n
    is_decreasing[n - 1] = True
    for i in range(n - 2, -1, -1):
        if nums[i] > nums[i + 1]:
            is_decreasing[i] = True
        else:
            # Once the decreasing property is broken (from right to left), all preceding are False
            break

    # Check every possible split point. 
    # A split at index 'i' means the first part is nums[0...i] 
    # and the second part is nums[i+1...n-1].
    # Both parts must be non-empty, so i ranges from 0 to n-2.
    for i in range(n - 1):
        if is_increasing[i] and is_decreasing[i + 1]:
            return True

    return False
