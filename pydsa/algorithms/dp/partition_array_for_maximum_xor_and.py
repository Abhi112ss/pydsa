METADATA = {
    "id": 3630,
    "name": "Partition Array for Maximum XOR and AND",
    "slug": "partition_array_for_maximum_xor_and",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Partition an array into contiguous subarrays to maximize the sum of (XOR of subarray) and (AND of subarray) for each partition.",
}

def solve(nums: list[int]) -> int:
    """
    Partitions the array into contiguous subarrays such that the sum of 
    (XOR of elements in subarray + AND of elements in subarray) is maximized.

    Args:
        nums: A list of integers to be partitioned.

    Returns:
        The maximum possible sum of (XOR + AND) for all partitions.

    Examples:
        >>> solve([1, 2, 3])
        # Possible partitions:
        # [1], [2, 3] -> (1^1 + 1&1) + (2^3 + 2&3) = (1+1) + (1+2) = 5
        # [1, 2], [3] -> (1^2 + 1&2) + (3^3 + 3&3) = (3+0) + (3+3) = 9
        # [1, 2, 3]   -> (1^2^3 + 1&2&3) = (0 + 0) = 0
        # Max is 9.
        9
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the maximum sum achievable using the first i elements.
    # We use a 1-indexed DP array for convenience.
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        current_xor = 0
        current_and = nums[i - 1]
        
        # Try all possible starting points 'j' for the last subarray [j...i-1]
        # We iterate backwards from the current element to build the subarray.
        for j in range(i, 0, -1):
            val = nums[j - 1]
            
            # Update XOR and AND for the subarray nums[j-1...i-1]
            # Note: For the first element in the inner loop (j=i), 
            # current_xor is just nums[i-1] and current_and is nums[i-1].
            if j == i:
                current_xor = val
                current_and = val
            else:
                current_xor ^= val
                current_and &= val
            
            # The recurrence relation:
            # dp[i] = max(dp[i], dp[j-1] + (XOR_of_subarray + AND_of_subarray))
            score = current_xor + current_and
            if dp[j - 1] + score > dp[i]:
                dp[i] = dp[j - 1] + score

    return dp[n]
