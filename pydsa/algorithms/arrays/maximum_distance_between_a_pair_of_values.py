METADATA = {
    "id": 1855,
    "name": "Maximum Distance Between a Pair of Values",
    "slug": "maximum_distance_between_a_pair_of_values",
    "category": "array",
    "aliases": [],
    "tags": ["array", "two pointers", "binary search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum index distance i ≤ j with nums1[i] ≤ nums2[j] in two sorted arrays.",
}


def solve(nums1: list[int], nums2: list[int]) -> int:
    """Return the maximum distance between a pair of indices (i, j) such that
    i ≤ j and nums1[i] ≤ nums2[j].

    Args:
        nums1: A list of integers sorted in non‑decreasing order.
        nums2: A list of integers sorted in non‑decreasing order.

    Returns:
        The largest possible value of j - i satisfying the condition.
        Returns 0 if no such pair exists.

    Examples:
        >>> solve([1,4,5,8], [2,3,4,5,6])
        3
        >>> solve([1,2,3,4,5], [1,2,3,4,5])
        4
        >>> solve([5,6,7], [1,2,3])
        0
    """
    index_first = 0
    index_second = 0
    max_distance = 0

    # Iterate through both arrays with two pointers.
    while index_first < len(nums1) and index_second < len(nums2):
        if nums1[index_first] <= nums2[index_second]:
            # Valid pair found; update maximum distance.
            current_distance = index_second - index_first
            if current_distance > max_distance:
                max_distance = current_distance
            index_second += 1
        else:
            # nums1[index_first] is too large; move the first pointer forward.
            index_first += 1
            # Ensure the second pointer never lags behind the first.
            if index_second < index_first:
                index_second = index_first

    return max_distance