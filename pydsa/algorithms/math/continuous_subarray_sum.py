METADATA = {
    "id": 523,
    "name": "Continuous Subarray Sum",
    "slug": "continuous-subarray-sum",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(min(n, k))",
    "description": "Check if the array has a continuous subarray of size at least two that sums up to a multiple of k.",
}

def solve(nums: list[int], k: int) -> bool:
    """
    Determines if there is a continuous subarray of size at least two that sums to a multiple of k.

    Args:
        nums: A list of integers.
        k: The target divisor.

    Returns:
        True if such a subarray exists, False otherwise.

    Examples:
        >>> solve([23, 2, 4, 6, 7], 6)
        True
        >>> solve([23, 2, 6, 4, 7], 13)
        False
    """
    # If k is 0, the problem definition usually implies we look for sum 0.
    # However, per LeetCode constraints, k >= 1.
    if k == 0:
        # This case is technically not possible per constraints, but for robustness:
        # A sum of 0 is a multiple of 0 only if the sum is 0.
        # But standard math says k is non-zero in this problem.
        return False

    # remainder_map stores {remainder: first_index_where_this_remainder_occurred}
    # We initialize with {0: -1} to handle cases where the prefix sum itself is a multiple of k
    # starting from index 0.
    remainder_map: dict[int, int] = {0: -1}
    current_running_sum = 0

    for index, value in enumerate(nums):
        current_running_sum += value
        
        # Calculate remainder. We use modulo k.
        # In Python, % operator handles negative numbers correctly for this logic.
        remainder = current_running_sum % k

        if remainder in remainder_map:
            # If we have seen this remainder before, the sum of elements between 
            # the previous occurrence and the current index is a multiple of k.
            # We must ensure the subarray length is at least 2.
            if index - remainder_map[remainder] >= 2:
                return True
        else:
            # Only store the first occurrence to maximize the potential subarray length.
            remainder_map[remainder] = index

    return False
