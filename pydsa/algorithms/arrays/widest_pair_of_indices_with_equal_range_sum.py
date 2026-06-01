METADATA = {
    "id": 1983,
    "name": "Widest Pair of Indices With Equal Range Sum",
    "slug": "widest-pair-of-indices-with-equal-range-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum distance between two indices such that the sum of elements in both ranges is equal.",
}

def solve(nums: list[int], left: int, right: int) -> int:
    """
    Finds the maximum distance between two indices (i, j) such that 
    the sum of elements in the range [left, i] equals the sum in [j, right].

    Args:
        nums: A list of integers.
        left: The starting index of the left range.
        right: The ending index of the right range.

    Returns:
        The maximum distance (i - j) if such indices exist, otherwise -1.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 0, 4)
        2
        >>> solve([1, 1, 1, 1, 1], 0, 4)
        4
        >>> solve([1, 2, 3], 0, 2)
        -1
    """
    # The problem asks for sum(nums[left...i]) == sum(nums[j...right])
    # Let P[k] be the prefix sum up to index k.
    # sum(nums[left...i]) = P[i] - P[left-1]
    # sum(nums[j...right]) = P[right] - P[j-1]
    # We want: P[i] - P[left-1] = P[right] - P[j-1]
    # Rearranging: P[i] + P[j-1] = P[right] + P[left-1]
    
    # However, a simpler way to view this is:
    # Let L_sum(i) = sum of nums from left to i.
    # Let R_sum(j) = sum of nums from j to right.
    # We want L_sum(i) == R_sum(j) and maximize (i - j).

    # Precompute prefix sums to allow O(1) range sum calculation
    n = len(nums)
    prefix_sums = [0] * (n + 1)
    for k in range(n):
        prefix_sums[k + 1] = prefix_sums[k] + nums[k]

    def get_sum(start: int, end: int) -> int:
        # Returns sum of nums[start...end] inclusive
        return prefix_sums[end + 1] - prefix_sums[start]

    # Map to store the first occurrence of a specific R_sum(j)
    # Key: sum value, Value: the index j
    # We want to maximize i - j, so for a fixed i, we want the smallest j.
    right_sums_map = {}

    # Iterate from right to left to populate the map with the smallest j for each sum
    # We iterate j from right down to left to ensure we capture the smallest j 
    # for a specific sum value. Actually, to maximize i - j, we want the smallest j.
    # So we iterate j from right to left and update the map only if the sum is new.
    for j in range(right, left - 1, -1):
        current_r_sum = get_sum(j, right)
        if current_r_sum not in right_sums_map:
            right_sums_map[current_r_sum] = j

    max_dist = -1

    # Iterate i from left to right to find the maximum i - j
    for i in range(left, right + 1):
        current_l_sum = get_sum(left, i)
        
        # Check if this left sum exists in our right sums map
        if current_l_sum in right_sums_map:
            j = right_sums_map[current_l_sum]
            # The condition is i >= j for a valid pair of indices (i, j)
            # where the ranges [left, i] and [j, right] are valid.
            # Note: the problem implies i and j are indices such that 
            # the ranges are [left, i] and [j, right].
            if i >= j:
                max_dist = max(max_dist, i - j)

    return max_dist
