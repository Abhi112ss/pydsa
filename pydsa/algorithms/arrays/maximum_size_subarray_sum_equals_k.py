METADATA = {
    "id": 325,
    "name": "Maximum Size Subarray Sum Equals k",
    "slug": "maximum-size-subarray-sum-equals-k",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum length of a subarray that sums to a given value k using prefix sums and a hash map.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the maximum length of a contiguous subarray that sums to k.

    Args:
        nums: A list of integers.
        k: The target sum.

    Returns:
        The maximum length of a subarray that sums to k. Returns 0 if no such subarray exists.

    Examples:
        >>> solve([1, -1, 5, -2, 3], 3)
        4
        >>> solve([-2, -1, 2, 1], 1)
        2
    """
    # prefix_sum_map stores the first occurrence of a prefix sum: {sum: index}
    # We initialize with {0: -1} to handle cases where the subarray starts from index 0
    prefix_sum_map: dict[int, int] = {0: -1}
    current_running_sum = 0
    max_length = 0

    for current_index, num in enumerate(nums):
        current_running_sum += num

        # We want to find if there exists a previous prefix sum such that:
        # current_running_sum - previous_prefix_sum = k
        # Therefore: previous_prefix_sum = current_running_sum - k
        target_prefix_sum = current_running_sum - k

        if target_prefix_sum in prefix_sum_map:
            # Calculate the length of the subarray ending at current_index
            subarray_length = current_index - prefix_sum_map[target_prefix_sum]
            if subarray_length > max_length:
                max_length = subarray_length

        # Only store the index if the sum has not been seen before.
        # This ensures we keep the leftmost index to maximize the subarray length.
        if current_running_sum not in prefix_sum_map:
            prefix_sum_map[current_running_sum] = current_index

    return max_length
