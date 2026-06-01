METADATA = {
    "id": 2016,
    "name": "Maximum Difference Between Increasing Elements",
    "slug": "maximum-difference-between-increasing-elements",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum difference between two elements in an array such that the second element is strictly greater than the first and appears after it.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum difference between two elements nums[j] - nums[i] 
    such that i < j and nums[i] < nums[j].

    Args:
        nums: A list of integers.

    Returns:
        The maximum difference found. Returns -1 if no such pair exists.

    Examples:
        >>> solve([7, 1, 5, 4])
        4
        >>> solve([9, 4, 3, 2])
        -1
        >>> solve([1, 2, 3, 4])
        3
    """
    n = len(nums)
    if n < 2:
        return -1

    # dp[i] will store the minimum value encountered in the prefix nums[0...i]
    # This allows us to find the best 'i' for a given 'j' in O(1) after preprocessing
    min_prefix_values = [0] * n
    min_prefix_values[0] = nums[0]
    
    for i in range(1, n):
        min_prefix_values[i] = min(min_prefix_values[i - 1], nums[i])

    max_diff = -1

    # Iterate through each element as a potential 'j' (the larger element)
    for j in range(1, n):
        # The best 'i' for this 'j' is the index that provides the minimum value 
        # seen before index j.
        # We check if the current element is greater than the minimum seen so far.
        if nums[j] > min_prefix_values[j - 1]:
            current_diff = nums[j] - min_prefix_values[j - 1]
            if current_diff > max_diff:
                max_diff = current_diff

    return max_diff
