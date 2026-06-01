METADATA = {
    "id": 3187,
    "name": "Peaks in Array",
    "slug": "peaks-in-array",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of elements in an array that are strictly greater than their immediate neighbors.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of peak elements in an array.
    
    A peak element is defined as an element that is strictly greater than 
    its immediate left and right neighbors. For elements at the boundaries, 
    they are only compared to their single existing neighbor.

    Args:
        nums: A list of integers.

    Returns:
        The total count of peak elements found in the array.

    Examples:
        >>> solve([1, 2, 3, 1])
        1
        >>> solve([1, 2, 1, 3, 4])
        2
        >>> solve([5, 4, 3, 2, 1])
        1
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 1

    peak_count = 0

    for i in range(n):
        # Check left neighbor condition
        # If i is 0, there is no left neighbor, so it satisfies the condition
        is_greater_than_left = (i == 0) or (nums[i] > nums[i - 1])

        # Check right neighbor condition
        # If i is the last index, there is no right neighbor, so it satisfies the condition
        is_greater_than_right = (i == n - 1) or (nums[i] > nums[i + 1])

        # An element is a peak if it satisfies both conditions
        if is_greater_than_left and is_greater_than_right:
            peak_count += 1

    return peak_count
