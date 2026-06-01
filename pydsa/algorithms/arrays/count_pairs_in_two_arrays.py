METADATA = {
    "id": 1885,
    "name": "Count Pairs in Two Arrays",
    "slug": "count-pairs-in-two-arrays",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Count pairs (nums1[i], nums2[j]) such that (nums1[i] - nums2[j]) % k == 0.",
}

def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    """
    Counts the number of pairs (nums1[i], nums2[j]) such that 
    (nums1[i] - nums2[j]) is divisible by k.

    The condition (nums1[i] - nums2[j]) % k == 0 is equivalent to 
    nums1[i] % k == nums2[j] % k.

    Args:
        nums1: A list of integers.
        nums2: A list of integers.
        k: A positive integer divisor.

    Returns:
        The total number of pairs satisfying the condition.

    Examples:
        >>> solve([1, 2, 3], [1, 2, 3], 2)
        3
        >>> solve([1, 2, 3], [4, 5, 6], 3)
        2
    """
    # Frequency map to store counts of remainders found in nums2
    remainder_counts: dict[int, int] = {}

    # Populate the frequency map with remainders of elements in nums2
    for value in nums2:
        remainder = value % k
        remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1

    total_pairs = 0

    # For each element in nums1, find how many elements in nums2 
    # share the same remainder when divided by k
    for value in nums1:
        target_remainder = value % k
        if target_remainder in remainder_counts:
            total_pairs += remainder_counts[target_remainder]

    return total_pairs
