METADATA = {
    "id": 1865,
    "name": "Finding Pairs With a Certain Sum",
    "slug": "finding-pairs-with-a-certain-sum",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n)",
    "description": "Find the number of pairs (nums1[i], nums2[j]) such that their sum equals a given target, where nums1 contains unique elements.",
}

def solve(nums1: list[int], nums2: list[int], target: int) -> list[int]:
    """
    Finds the number of pairs (nums1[i], nums2[j]) that sum up to the target.

    Args:
        nums1: A list of unique integers.
        nums2: A list of integers (may contain duplicates).
        target: The target sum to find.

    Returns:
        A list of two integers: [count_of_pairs, count_of_unique_pairs].

    Examples:
        >>> solve([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 6)
        [3, 3]
        >>> solve([1, 1, 2, 2], [1, 1, 2, 2], 3)
        [4, 2]
    """
    # Frequency map for nums2 to allow O(1) lookup of complements
    counts_nums2: dict[int, int] = {}
    for num in nums2:
        counts_nums2[num] = counts_nums2.get(num, 0) + 1

    total_pairs = 0
    unique_pairs = 0
    
    # Track seen elements from nums1 to ensure unique pairs are counted correctly
    # Since nums1 is guaranteed to have unique elements, we can just iterate
    # and check if the complement exists in the frequency map.
    for val1 in nums1:
        complement = target - val1
        
        if complement in counts_nums2:
            # Every occurrence of the complement in nums2 forms a valid pair
            total_pairs += counts_nums2[complement]
            # Since nums1 elements are unique, each valid complement found 
            # represents a unique pair (val1, complement)
            unique_pairs += 1

    return [total_pairs, unique_pairs]
