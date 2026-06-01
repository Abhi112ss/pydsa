METADATA = {
    "id": 3500,
    "name": "Minimum Cost to Divide Array Into Subarrays",
    "slug": "minimum-cost-to-divide-array-into-subarrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to divide an array into contiguous subarrays based on a given cost function.",
}

def solve(nums: list[int], costs: list[list[int]]) -> int:
    """
    Calculates the minimum cost to divide the array into contiguous subarrays.
    
    The cost of a subarray from index i to j is provided in the costs matrix,
    where costs[i][j] represents the cost of the subarray nums[i...j].
    
    Args:
        nums: A list of integers representing the array elements.
        costs: A 2D list where costs[i][j] is the cost of subarray nums[i...j].
        
    Returns:
        The minimum total cost to partition the array.
        
    Examples:
        >>> solve([1, 2, 3], [[0, 10, 20], [0, 0, 5], [0, 0, 0]])
        15
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the minimum cost to partition the prefix nums[0...i-1]
    # Initialize with infinity, dp[0] = 0 as the base case (empty prefix)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        # Try every possible starting position 'j' for the last subarray
        # The last subarray would be nums[j-1...i-1]
        for j in range(1, i + 1):
            # The cost to reach index i is the cost to reach index j-1 
            # plus the cost of the subarray from j-1 to i-1
            current_subarray_cost = costs[j - 1][i - 1]
            
            # Update dp[i] if a cheaper partition is found
            if dp[j - 1] + current_subarray_cost < dp[i]:
                dp[i] = dp[j - 1] + current_subarray_cost

    return int(dp[n])
