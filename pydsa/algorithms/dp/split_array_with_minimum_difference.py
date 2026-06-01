METADATA = {
    "id": 3698,
    "name": "Split Array With Minimum Difference",
    "slug": "split_array_with_minimum_difference",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "subset_sum", "partition"],
    "difficulty": "medium",
    "time_complexity": "O(n * sum)",
    "space_complexity": "O(sum)",
    "description": "Partition an array into two subsets such that the absolute difference between their sums is minimized.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum absolute difference between the sums of two subsets 
    formed by partitioning the input array.

    Args:
        nums: A list of integers to be partitioned.

    Returns:
        The minimum possible absolute difference between the sums of the two subsets.

    Examples:
        >>> solve([1, 6, 11, 5])
        1
        >>> solve([3, 9, 7, 3])
        2
    """
    total_sum = sum(nums)
    # We want to find a subset sum as close to total_sum / 2 as possible.
    # target is the maximum possible sum of one subset to minimize difference.
    target = total_sum // 2

    # dp[i] will be True if a subset with sum 'i' can be formed.
    # Using a bitset approach (via a large integer) is highly efficient in Python.
    # Alternatively, a boolean array can be used.
    dp = 1  # Represents the bitset where bit 0 is set (sum 0 is always possible)

    for num in nums:
        # For every number, we update the bitset. 
        # Shifting left by 'num' is equivalent to adding 'num' to all existing sums.
        # The OR operation combines the old possible sums with the new ones.
        dp |= (dp << num)

    # We iterate backwards from the target to find the largest achievable sum <= target.
    # This sum 's' will result in a difference of: (total_sum - s) - s = total_sum - 2*s.
    for s in range(target, -1, -1):
        if (dp >> s) & 1:
            return total_sum - 2 * s

    return total_sum
