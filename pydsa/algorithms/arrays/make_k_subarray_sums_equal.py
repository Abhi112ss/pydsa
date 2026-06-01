METADATA = {
    "id": 2607,
    "name": "Make K-Subarray Sums Equal",
    "slug": "make_k_subarray_sums_equal",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to make all subarrays of length k have the same sum.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the minimum number of operations to make all subarrays of length k 
    have the same sum. An operation consists of incrementing or decrementing an element.

    To make all subarrays of length k equal, the array must satisfy nums[i] == nums[i + k] 
    for all valid i. This effectively partitions the array into k independent groups 
    based on index modulo k. For each group, we find the median to minimize the 
    sum of absolute differences.

    Args:
        nums: A list of integers.
        k: The length of the subarrays.

    Returns:
        The minimum number of operations required.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6], 3)
        3
        >>> solve([1, 1, 1], 2)
        1
    """
    n = len(nums)
    # Each element at index i must eventually equal the element at index i % k
    # to ensure all subarrays of length k have the same sum.
    # We group elements by their index modulo k.
    groups: list[list[int]] = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(nums[i])

    total_operations = 0

    for group in groups:
        if not group:
            continue
        
        # To minimize sum(|x_i - target|), the optimal target is the median.
        group.sort()
        median = group[len(group) // 2]
        
        # Calculate the sum of absolute differences from the median.
        for val in group:
            total_operations += abs(val - median)

    return total_operations
