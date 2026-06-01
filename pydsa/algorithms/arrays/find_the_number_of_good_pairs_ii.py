METADATA = {
    "id": 3164,
    "name": "Find the Number of Good Pairs II",
    "slug": "find-the-number-of-good-pairs-ii",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n)",
    "description": "Count pairs (nums1[i], nums2[j]) such that nums1[i] == nums2[j] and i != j.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Counts the number of pairs (i, j) such that nums1[i] == nums2[j] and i != j.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        The total number of valid pairs.

    Examples:
        >>> solve([1, 2, 3, 4], [1, 2, 3, 4])
        12
        >>> solve([1, 1, 2], [1, 2, 2])
        3
    """
    # Frequency map to store counts of each number in the first array
    counts_in_nums1: dict[int, int] = {}
    for num in nums1:
        counts_in_nums1[num] = counts_in_nums1.get(num, 0) + 1

    total_good_pairs: int = 0
    
    # Iterate through the second array to find matches
    for j, val in enumerate(nums2):
        if val in counts_in_nums1:
            # Add the number of times 'val' appeared in nums1 to the total
            total_good_pairs += counts_in_nums1[val]
            
            # If the current element in nums2 is the same as an element in nums1
            # at the same index, we must subtract it because the problem 
            # requires i != j.
            if j < len(nums1) and nums1[j] == val:
                total_good_pairs -= 1

    return total_good_pairs
