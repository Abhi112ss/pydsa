METADATA = {
    "id": 2903,
    "name": "Find Indices With Index and Value Difference I",
    "slug": "find-indices-with-index-and-value-difference-i",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "brute_force"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the first pair of indices (i, j) such that the difference between indices is at most k and the difference between values is at most k.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Finds the first pair of indices (i, j) such that i < j, 
    j - i <= k, and abs(nums[i] - nums[j]) <= k.

    Args:
        nums: A list of integers.
        k: An integer representing the maximum allowed difference for both indices and values.

    Returns:
        A list containing the two indices [i, j] if found, otherwise an empty list [].

    Examples:
        >>> solve([4, 2, 1, 4, 5], 3)
        [0, 1]
        >>> solve([1, 2, 3, 4, 5], 1)
        [0, 1]
        >>> solve([1, 5, 9, 13], 2)
        []
    """
    n = len(nums)

    # Iterate through each starting index i
    for i in range(n):
        # Iterate through each possible second index j, ensuring j > i
        # and the distance between indices does not exceed k
        for j in range(i + 1, min(i + k + 1, n)):
            # Check if the absolute difference between values is within k
            if abs(nums[i] - nums[j]) <= k:
                return [i, j]

    return []
