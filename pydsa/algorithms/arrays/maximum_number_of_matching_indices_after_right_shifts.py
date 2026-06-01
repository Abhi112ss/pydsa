METADATA = {
    "id": 3400,
    "name": "Maximum Number of Matching Indices After Right Shifts",
    "slug": "maximum-number-of-matching-indices-after-right-shifts",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of indices i such that nums1[i] == nums2[i] after any number of right cyclic shifts on nums2.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the maximum number of matching indices after any number of right cyclic shifts on nums2.

    The key insight is that for any pair of elements (nums1[i], nums2[j]) where nums1[i] == nums2[j],
    there exists a specific shift amount that aligns them. By calculating the required shift
    for every possible matching pair and counting the frequency of each shift, we can find
    the shift that maximizes the number of matches.

    Args:
        nums1: A list of integers.
        nums2: A list of integers of the same length as nums1.

    Returns:
        The maximum number of matching indices possible.

    Examples:
        >>> solve([1, 2, 3, 4], [4, 3, 2, 1])
        2
        >>> solve([1, 1, 1], [1, 1, 1])
        3
    """
    n = len(nums1)
    if n == 0:
        return 0

    # Map each value in nums2 to its indices to allow fast lookup
    # This helps us find all possible j such that nums2[j] == nums1[i]
    val_to_indices_in_nums2: dict[int, list[int]] = {}
    for index, value in enumerate(nums2):
        if value not in val_to_indices_in_nums2:
            val_to_indices_in_nums2[value] = []
        val_to_indices_in_nums2[value].append(index)

    # shift_counts[s] will store how many indices i satisfy nums1[i] == nums2[(i + s) % n]
    # However, the problem asks for right shifts of nums2. 
    # A right shift of nums2 by 's' positions moves nums2[j] to index (j + s) % n.
    # We want nums1[i] == nums2_shifted[i], which means nums1[i] == nums2[j] 
    # where (j + s) % n == i.
    # This implies s % n == (i - j) % n.
    shift_counts: dict[int, int] = {}

    for i, val in enumerate(nums1):
        if val in val_to_indices_in_nums2:
            for j in val_to_indices_in_nums2[val]:
                # Calculate the required right shift 's' to align nums2[j] with nums1[i]
                # (j + s) % n = i  =>  s % n = (i - j) % n
                shift = (i - j) % n
                shift_counts[shift] = shift_counts.get(shift, 0) + 1

    # The answer is the maximum frequency found in our shift counts
    if not shift_counts:
        return 0
        
    return max(shift_counts.values())
