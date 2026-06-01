METADATA = {
    "id": 2956,
    "name": "Find Common Elements Between Two Arrays",
    "slug": "find-common-elements-between-two-arrays",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "two_pointer", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(min(n, m))",
    "description": "Find the intersection of two arrays where each element in the result must appear as many times as it occurs in both arrays.",
}

def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Finds the common elements between two arrays, accounting for frequency.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        A list of integers representing the intersection of nums1 and nums2.

    Examples:
        >>> solve([1, 2, 2, 1], [2, 2])
        [2, 2]
        >>> solve([4, 9, 5], [9, 4, 9, 8, 4])
        [4, 9]
    """
    # To optimize space, we ensure the hash map is built from the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    counts: dict[int, int] = {}
    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    result: list[int] = []
    
    # Iterate through the second array and check against the frequency map
    for num in nums2:
        # If the number exists in the map and has a remaining count > 0
        if counts.get(num, 0) > 0:
            result.append(num)
            # Decrement the count to handle duplicate elements correctly
            counts[num] -= 1

    return result
