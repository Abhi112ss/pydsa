METADATA = {
    "id": 1043,
    "name": "Partition Array for Maximum Sum",
    "slug": "partition_array_for_maximum_sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n)",
    "description": "Partition an array into subarrays of length at most k such that the sum of the maximum elements in each subarray is maximized.",
}

def solve(arr: list[int], k: int) -> int:
    """
    Partitions the array into subarrays of length at most k to maximize the sum 
    of the maximum elements of each subarray.

    Args:
        arr: A list of integers representing the input array.
        k: An integer representing the maximum length of a subarray.

    Returns:
        The maximum possible sum of the maximum elements of the partitioned subarrays.

    Examples:
        >>> solve([1, 15, 7, 9, 2, 5], 3)
        84
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
        30
    """
    n = len(arr)
    # dp[i] stores the maximum sum possible using the first i elements of the array.
    # We use n + 1 to handle the base case dp[0] = 0 easily.
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        current_max = 0
        # We look back at most k elements to form the last partition.
        # The partition ends at index i-1 (0-indexed) and starts at index j.
        for j in range(1, k + 1):
            if i - j < 0:
                break
            
            # Update the maximum element found in the current partition [i-j, i-1]
            current_max = max(current_max, arr[i - j])
            
            # The recurrence relation:
            # Max sum for i elements = max(current_max + max sum for remaining i-j elements)
            dp[i] = max(dp[i], current_max + dp[i - j])

    return dp[n]
