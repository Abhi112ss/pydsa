METADATA = {
    "id": 454,
    "name": "4Sum II",
    "slug": "4sum-ii",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash table", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Given four integer arrays nums1, nums2, nums3, and nums4, return the number of tuples (i, j, k, l) such that nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.",
}

def solve(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    """
    Calculates the number of tuples (i, j, k, l) such that the sum of elements
    from the four arrays equals zero.

    Args:
        nums1: First list of integers.
        nums2: Second list of integers.
        nums3: Third list of integers.
        nums4: Fourth list of integers.

    Returns:
        The total count of tuples that sum to zero.

    Examples:
        >>> solve([1, 2], [-2, -1], [-1, 2], [0, 2])
        2
        >>> solve([0, 1, 2], [-1, -2, -3], [1, 2, 3], [-1, -2, -3])
        0
    """
    # Map to store the frequency of sums from the first two arrays
    # Key: sum (nums1[i] + nums2[j]), Value: count of occurrences
    sum_counts: dict[int, int] = {}

    # Step 1: Populate the hash map with all possible sums of pairs from nums1 and nums2
    for val1 in nums1:
        for val2 in nums2:
            current_sum = val1 + val2
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1

    total_tuples = 0

    # Step 2: Iterate through all possible sums of pairs from nums3 and nums4
    # If the negative of the current sum exists in our map, it means 
    # (val1 + val2) + (val3 + val4) == 0
    for val3 in nums3:
        for val4 in nums4:
            target = -(val3 + val4)
            if target in sum_counts:
                total_tuples += sum_counts[target]

    return total_tuples
