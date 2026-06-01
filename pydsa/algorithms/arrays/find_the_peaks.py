METADATA = {
    "id": 2951,
    "name": "Find the Peaks",
    "slug": "find-the-peaks",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "two pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the indices of all peak elements in an array where a peak is strictly greater than its neighbors.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds the indices of all peak elements in the given list.
    
    A peak element is defined as an element that is strictly greater than 
    its immediate neighbors. For the first and last elements, they are 
    considered peaks if they are strictly greater than their only neighbor.

    Args:
        nums: A list of integers.

    Returns:
        A list of indices where each index represents a peak element.

    Examples:
        >>> solve([1, 2, 3, 1])
        [2]
        >>> solve([1, 2, 1, 3, 5, 6, 4])
        [1, 5]
        >>> solve([5, 4, 3, 2, 1])
        [0]
    """
    n = len(nums)
    peaks = []

    if n == 0:
        return peaks
    
    # A single element is technically a peak as it has no neighbors to be smaller than
    if n == 1:
        return [0]

    for i in range(n):
        # Check left neighbor condition
        # If i is 0, there is no left neighbor, so it satisfies the condition
        is_greater_than_left = (i == 0) or (nums[i] > nums[i - 1])
        
        # Check right neighbor condition
        # If i is n-1, there is no right neighbor, so it satisfies the condition
        is_greater_than_right = (i == n - 1) or (nums[i] > nums[i + 1])

        # If both conditions are met, the current index is a peak
        if is_greater_than_left and is_greater_than_right:
            peaks.append(i)

    return peaks
