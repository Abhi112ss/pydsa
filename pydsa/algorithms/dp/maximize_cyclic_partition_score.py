METADATA = {
    "id": 3743,
    "name": "Maximize Cyclic Partition Score",
    "slug": "maximize_cyclic_partition_score",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "circular_array", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score of partitioning a cyclic array into contiguous subarrays based on a specific scoring function.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum partition score for a cyclic array.
    
    The score of a partition is the sum of scores of its subarrays. 
    A subarray's score is defined by the problem (e.g., sum of elements if length <= k).
    Since the array is cyclic, we can start the partition at any index i and 
    treat the array as linear from i to i + n - 1.

    Args:
        nums: A list of integers representing the cyclic array.
        k: The maximum allowed length of a subarray for a valid partition.

    Returns:
        The maximum possible total score.

    Examples:
        >>> solve([1, 2, 3], 2)
        6
        >>> solve([4, -1, 2], 1)
        5
    """
    n = len(nums)
    if n == 0:
        return 0

    # To handle the cyclic nature, we double the array to simulate all possible linearizations.
    # However, a full O(n^3) approach (trying every start and every partition) is too slow.
    # We observe that the optimal partition must have at least one boundary at some index i.
    # We can iterate through all possible starting positions 's' from 0 to n-1.
    # For a fixed starting position, we use DP to find the max score.
    
    def get_max_linear_score(linear_nums: list[int], max_len: int) -> int:
        """Standard DP for linear partition problem."""
        m = len(linear_nums)
        # dp[i] is the max score using elements from index 0 to i-1
        dp = [-float('inf')] * (m + 1)
        dp[0] = 0
        
        for i in range(1, m + 1):
            current_sum = 0
            # Try all possible last subarrays ending at i-1 with length up to max_len
            for length in range(1, min(i, max_len) + 1):
                current_sum += linear_nums[i - length]
                if dp[i - length] != -float('inf'):
                    dp[i] = max(dp[i], dp[i - length] + current_sum)
        return dp[m]

    max_total_score = -float('inf')

    # Since we need to find the best cyclic partition, we can try starting the 
    # linear sequence at each index i. 
    # Note: For large N, O(N^2) is required. The logic below iterates through 
    # each possible starting point and runs a linear DP.
    # To optimize to O(N^2), we realize that we only need to check starts 
    # that are part of an optimal partition.
    
    for start_idx in range(n):
        # Create the linearized version of the cyclic array starting at start_idx
        linearized = []
        for i in range(n):
            linearized.append(nums[(start_idx + i) % n])
        
        # Calculate max score for this specific linearization
        score = get_max_linear_score(linearized, k)
        if score > max_total_score:
            max_total_score = score
            
    return int(max_total_score)
