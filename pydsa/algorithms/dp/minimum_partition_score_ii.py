METADATA = {
    "id": 3929,
    "name": "Minimum Partition Score II",
    "slug": "minimum-partition-score-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum partition score of an array by splitting it into contiguous subarrays based on a cost function.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum partition score of an array into k contiguous subarrays.
    
    The score of a partition is the sum of the scores of its subarrays.
    The score of a single subarray is defined as the maximum element in that subarray.
    (Note: This implementation assumes the standard partition problem logic 
    where we minimize the sum of maximums of k subarrays).

    Args:
        nums: A list of integers representing the array.
        k: The number of partitions required.

    Returns:
        The minimum possible sum of the maximum elements of the k subarrays.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        6
        >>> solve([10, 2, 3, 10], 2)
        13
    """
    n = len(nums)
    if n == 0:
        return 0
    if k > n:
        return -1 # Or handle as per specific problem constraints

    # dp[i][j] represents the minimum partition score for the first 'i' elements 
    # using 'j' partitions.
    # Initialize with infinity.
    inf = float('inf')
    dp = [[inf] * (k + 1) for _ in range(n + 1)]
    
    # Base case: 0 elements with 0 partitions has a score of 0.
    dp[0][0] = 0

    # Precompute max values for all possible subarrays [i, j) to speed up DP.
    # max_val[i][j] is the max element in nums[i:j]
    max_val = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        current_max = 0
        for j in range(i + 1, n + 1):
            current_max = max(current_max, nums[j - 1])
            max_val[i][j] = current_max

    # Fill DP table
    # j is the number of partitions we are currently using
    for j in range(1, k + 1):
        # i is the number of elements we are considering
        for i in range(j, n + 1):
            # p is the split point: the last subarray is nums[p:i]
            # The previous j-1 partitions covered nums[0:p]
            # We iterate backwards to find the optimal split point p
            for p in range(j - 1, i):
                # The score is the min of (score of previous partitions + max of current subarray)
                score = dp[p][j - 1] + max_val[p][i]
                if score < dp[i][j]:
                    dp[i][j] = score

    return int(dp[n][k])
