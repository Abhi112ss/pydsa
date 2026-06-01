METADATA = {
    "id": 1879,
    "name": "Minimum XOR Sum of Two Arrays",
    "slug": "minimum-xor-sum-of-two-arrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(n * 2^n)",
    "space_complexity": "O(2^n)",
    "description": "Find the minimum XOR sum of two arrays by pairing each element of the first array with a unique element from the second array.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the minimum XOR sum of two arrays by finding the optimal permutation.

    Args:
        nums1: A list of integers.
        nums2: A list of integers of the same length as nums1.

    Returns:
        The minimum possible sum of (nums1[i] ^ nums2[p[i]]) for all i, 
        where p is a permutation of indices of nums2.

    Examples:
        >>> solve([1, 2], [2, 3])
        2
        >>> solve([0, 0, 0], [0, 0, 0])
        0
        >>> solve([1, 2, 3], [2, 1, 3])
        0
    """
    n = len(nums1)
    # dp[mask] stores the minimum XOR sum using the first 'k' elements of nums1,
    # where 'mask' represents the set of indices used from nums2.
    # 'k' is implicitly the number of set bits in 'mask'.
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    # Iterate through all possible subsets of nums2 represented by the mask
    for mask in range(1 << n):
        # Determine which index in nums1 we are currently pairing
        # by counting how many elements from nums2 have already been used.
        current_idx_nums1 = bin(mask).count('1')
        
        if current_idx_nums1 == n:
            continue

        # Try pairing nums1[current_idx_nums1] with every available element in nums2
        for j in range(n):
            # If the j-th element of nums2 is not yet in the mask
            if not (mask & (1 << j)):
                new_mask = mask | (1 << j)
                # Calculate the XOR sum for the current pairing
                xor_val = nums1[current_idx_nums1] ^ nums2[j]
                # Update the DP state for the new mask
                if dp[mask] + xor_val < dp[new_mask]:
                    dp[new_mask] = dp[mask] + xor_val

    return int(dp[(1 << n) - 1])
