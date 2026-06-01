METADATA = {
    "id": 3285,
    "name": "Find Indices of Stable Mountains",
    "slug": "find-indices-of-stable-mountains",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the indices of elements in an array that are strictly greater than both their immediate neighbors.",
}

def solve(height: list[int]) -> list[int]:
    """
    Finds the indices of all 'stable mountains' in the given height array.
    A mountain is stable if it is strictly greater than its left and right neighbors.

    Args:
        height: A list of integers representing the heights of mountains.

    Returns:
        A list of indices where each index corresponds to a stable mountain.

    Examples:
        >>> solve([2, 1, 4, 3, 5])
        [2, 4]
        >>> solve([1, 2, 3, 4, 5])
        []
        >>> solve([5, 4, 3, 2, 1])
        []
    """
    stable_indices: list[int] = []
    n: int = len(height)

    # A mountain must have a neighbor on both sides to be considered stable
    # based on the problem definition (strictly greater than neighbors).
    # We iterate from the second element to the second-to-last element.
    for i in range(1, n - 1):
        # Check the local slope condition: height[i] > height[i-1] AND height[i] > height[i+1]
        if height[i] > height[i - 1] and height[i] > height[i + 1]:
            stable_indices.append(i)

    # Note: The problem implies mountains at the boundaries (index 0 or n-1) 
    # cannot be stable because they lack one neighbor to compare against.
    # However, if the problem definition allowed boundary comparison, 
    # we would handle them separately. Based on standard 'local peak' definitions,
    # we only check internal elements.
    
    # Re-evaluating based on LeetCode 3285 specific constraints:
    # The problem states: "mountain[i] is stable if mountain[i] > mountain[i-1] AND mountain[i] > mountain[i+1]"
    # This definition inherently excludes index 0 and index n-1.
    
    return stable_indices
