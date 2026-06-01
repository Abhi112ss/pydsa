METADATA = {
    "id": 698,
    "name": "Partition to K Equal Sum Subsets",
    "slug": "partition_to_k_equal_sum_subsets",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["backtracking", "bitmask", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(k * 2^n)",
    "space_complexity": "O(2^n)",
    "description": "Determine if an array can be partitioned into k subsets with equal sums.",
}

def solve(nums: list[int], k: int) -> bool:
    """
    Determines if the given array can be partitioned into k subsets with equal sums.

    Args:
        nums: A list of integers to be partitioned.
        k: The number of subsets to create.

    Returns:
        True if partitioning is possible, False otherwise.

    Examples:
        >>> solve([4, 3, 2, 3, 5, 2, 1], 4)
        True
        >>> solve([1, 2, 3, 4], 3)
        False
    """
    total_sum = sum(nums)
    n = len(nums)

    # Basic feasibility checks
    if total_sum % k != 0:
        return False
    
    target_sum = total_sum // k
    nums.sort(reverse=True)  # Sorting descending helps prune faster in backtracking

    if nums[0] > target_sum:
        return False

    # memo stores whether a specific bitmask state (subset of elements used) is valid
    memo: dict[int, bool] = {}

    def can_partition(mask: int, current_sum: int) -> bool:
        """
        Uses bitmask DP with memoization to find if remaining elements can form subsets.

        Args:
            mask: Bitmask representing the set of indices used.
            current_sum: The sum accumulated in the current subset being built.

        Returns:
            True if the remaining elements can satisfy the partition requirement.
        """
        # If all elements are used, we successfully partitioned into k subsets
        if mask == (1 << n) - 1:
            return True

        if mask in memo:
            return memo[mask]

        # If current subset is full, start building the next subset from sum 0
        if current_sum == target_sum:
            res = can_partition(mask, 0)
            memo[mask] = res
            return res

        # Try adding each unused element to the current subset
        for i in range(n):
            # Check if the i-th element is already used
            if not (mask & (1 << i)):
                # Pruning: if adding this element exceeds target, skip it
                # Since nums is sorted descending, we could potentially break, 
                # but for bitmask DP, we just continue.
                if current_sum + nums[i] <= target_sum:
                    # Recurse with the i-th element marked as used
                    if can_partition(mask | (1 << i), current_sum + nums[i]):
                        memo[mask] = True
                        return True
                
                # Optimization: If current_sum is 0 and we couldn't place nums[i],
                # then nums[i] can never be part of any valid subset in this branch.
                if current_sum == 0:
                    break

        memo[mask] = False
        return False

    return can_partition(0, 0)
