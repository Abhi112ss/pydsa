METADATA = {
    "id": 3904,
    "name": "Smallest Stable Index II",
    "slug": "smallest_stable_index_ii",
    "category": "Array",
    "aliases": [],
    "tags": ["binary_search", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest index such that the stability condition is met using prefix sums.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the smallest index 'i' such that the stability condition is satisfied.
    The stability condition is defined as the sum of elements in the range [0, i] 
    being at least k times the sum of elements in the range [i+1, n-1].

    Args:
        nums: A list of non-negative integers.
        k: A positive integer multiplier.

    Returns:
        The smallest index 'i' that satisfies the condition, or -1 if no such index exists.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 1)
        3
        >>> solve([1, 1, 1], 10)
        -1
    """
    n = len(nums)
    if n == 0:
        return -1

    # Precompute prefix sums to allow O(1) range sum queries
    # prefix_sums[i] stores the sum of nums[0...i-1]
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    total_sum = prefix_sums[n]

    # Iterate through each possible split index i
    # The split is between index i and i+1
    # Condition: sum(nums[0...i]) >= k * sum(nums[i+1...n-1])
    for i in range(n):
        # sum_left is the sum of elements from index 0 to i
        sum_left = prefix_sums[i + 1]
        
        # sum_right is the sum of elements from index i+1 to n-1
        sum_right = total_sum - sum_left
        
        # Check the stability condition
        if sum_left >= k * sum_right:
            return i

    return -1
