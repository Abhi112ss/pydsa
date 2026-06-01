METADATA = {
    "id": 3010,
    "name": "Divide an Array Into Subarrays With Minimum Cost I",
    "slug": "divide_an_array_into_subarrays_with_minimum_cost_i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Partition an array into contiguous subarrays such that the sum of the costs of each subarray is minimized.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum cost to divide the array into subarrays.
    
    The cost of a subarray is defined as the sum of the absolute differences 
    between adjacent elements within that subarray. If a subarray has only 
    one element, its cost is 0.

    Args:
        nums: A list of integers representing the array.
        k: The number of subarrays the array must be divided into.

    Returns:
        The minimum total cost to partition the array.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 2)
        4
        >>> solve([1, 10, 1, 10], 2)
        18
    """
    n = len(nums)
    
    # Precompute subarray costs to avoid redundant calculations.
    # cost[i][j] is the cost of subarray nums[i...j]
    # cost[i][j] = sum(|nums[m] - nums[m-1]| for m from i+1 to j)
    # This can be simplified: cost[i][j] = cost[i][j-1] + abs(nums[j] - nums[j-1])
    subarray_costs = [[0] * n for _ in range(n)]
    for i in range(n):
        current_cost = 0
        for j in range(i + 1, n):
            current_cost += abs(nums[j] - nums[j - 1])
            subarray_costs[i][j] = current_cost

    # dp[i][j] represents the minimum cost to divide the first 'j' elements 
    # into 'i' subarrays.
    # We use float('inf') to represent impossible states.
    dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
    
    # Base case: 0 subarrays for 0 elements costs 0.
    dp[0][0] = 0

    # Fill the DP table
    for i in range(1, k + 1):
        # A partition into 'i' subarrays requires at least 'i' elements.
        for j in range(i, n + 1):
            # Try all possible split points 'p' for the last (i-th) subarray.
            # The last subarray will be nums[p...j-1].
            # The previous i-1 subarrays cover nums[0...p-1].
            for p in range(i - 1, j):
                # cost of the last subarray is subarray_costs[p][j-1]
                current_partition_cost = dp[i - 1][p] + subarray_costs[p][j - 1]
                if current_partition_cost < dp[i][j]:
                    dp[i][j] = current_partition_cost

    return int(dp[k][n])
