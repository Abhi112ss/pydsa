METADATA = {
    "id": 3599,
    "name": "Partition Array to Minimize XOR",
    "slug": "partition_array_to_minimize_xor",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Partition an array into contiguous subarrays such that the sum of the XOR sums of each subarray is minimized.",
}

def solve(nums: list[int]) -> int:
    """
    Partitions the array into contiguous subarrays to minimize the sum of their XOR sums.

    Args:
        nums: A list of integers representing the array to be partitioned.

    Returns:
        The minimum possible sum of XOR sums of the partitioned subarrays.

    Examples:
        >>> solve([1, 2, 3])
        0
        >>> solve([1, 1, 1])
        1
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i] stores the minimum XOR sum for the prefix nums[0...i-1]
    # Initialize with a large value (infinity)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Precompute prefix XORs to calculate range XOR in O(1)
    # prefix_xor[i] = nums[0] ^ nums[1] ^ ... ^ nums[i-1]
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ nums[i]

    for i in range(1, n + 1):
        # Try all possible split points j where the last subarray is nums[j...i-1]
        for j in range(i):
            # Calculate XOR sum of subarray nums[j...i-1] using prefix XORs
            # XOR(j, i-1) = prefix_xor[i] ^ prefix_xor[j]
            current_subarray_xor = prefix_xor[i] ^ prefix_xor[j]
            
            # Update dp[i] if a smaller sum is found
            # dp[i] = min(dp[i], dp[j] + current_subarray_xor)
            if dp[j] + current_subarray_xor < dp[i]:
                dp[i] = dp[j] + current_subarray_xor

    return int(dp[n])
