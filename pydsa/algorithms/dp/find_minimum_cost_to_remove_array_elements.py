METADATA = {
    "id": 3469,
    "name": "Find Minimum Cost to Remove Array Elements",
    "slug": "find-minimum-cost-to-remove-array-elements",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to remove all elements from an array where removing a subarray costs the sum of its elements plus a constant factor.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum cost to remove all elements from the array.
    
    The problem can be modeled as finding the optimal way to partition the array 
    into subarrays, where each subarray removal incurs a cost. 
    The cost of removing a subarray [i, j] is sum(nums[i...j]) + k.

    Args:
        nums: A list of integers representing the elements in the array.
        k: A constant cost added to each subarray removal operation.

    Returns:
        The minimum total cost to remove all elements.

    Examples:
        >>> solve([1, 2, 3], 1)
        7
        # (1+2+3) + 1 = 7 (one subarray)
        # (1+1) + (2+1) + (3+1) = 9 (three subarrays)
        
        >>> solve([1, 1, 1], 10)
        13
        # (1+1+1) + 10 = 13
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] represents the minimum cost to remove the first i elements.
    # We initialize with infinity.
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Precompute prefix sums to calculate subarray sums in O(1)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    # Iterate through each position in the array to build the DP table
    for i in range(1, n + 1):
        # Try all possible previous split points j to form a subarray [j, i-1]
        for j in range(i):
            # The cost to remove subarray nums[j...i-1] is:
            # (sum of elements in subarray) + k
            current_subarray_sum = prefix_sums[i] - prefix_sums[j]
            cost_of_this_removal = current_subarray_sum + k
            
            # Update dp[i] if the current split results in a lower total cost
            if dp[j] + cost_of_this_removal < dp[i]:
                dp[i] = dp[j] + cost_of_this_removal

    return int(dp[n])
