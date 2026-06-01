METADATA = {
    "id": 349,
    "name": "Intersection of Two Arrays",
    "slug": "intersection_of_two_arrays",
    "category": "Array",
    "aliases": ["intersection of two arrays", "array intersection"],
    "tags": ["hash_set", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(min(n, m))",
    "description": "Given two integer arrays nums1 and nums2, return an array of their intersection elements.",
}

def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    """Find the intersection of two arrays using a hash set.

    Args:
        nums1: First integer array.
        nums2: Second integer array.

    Returns:
        List of unique elements present in both arrays.

    Examples:
        >>> solve([1, 2, 2, 1], [2, 2])
        [2]
        >>> solve([4, 9, 5], [9, 4, 9, 8, 4])
        [9, 4]
    """
    # Use the smaller array for the set to optimize space
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # Store elements of the smaller array in a set for O(1) lookups
    elements = set(nums1)

    # Find intersection by checking which elements of nums2 are in the set
    result = []
    seen = set()
    for num in nums2:
        if num in elements and num not in seen:
            result.append(num)
            seen.add(num)

    return result