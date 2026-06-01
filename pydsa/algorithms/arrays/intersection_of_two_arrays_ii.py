METADATA = {
    "id": 350,
    "name": "Intersection of Two Arrays II",
    "slug": "intersection_of_two_arrays_ii",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(min(n, m))",
    "description": "Return the intersection of two integer arrays including duplicate elements.",
}


def solve(nums1: list[int], nums2: list[int]) -> list[int]:
    """Return the intersection of two integer arrays, including duplicates.

    Args:
        nums1: First list of integers.
        nums2: Second list of integers.

    Returns:
        A list containing the intersecting elements. Each element appears as many
        times as it shows in both arrays.

    Examples:
        >>> solve([1,2,2,1], [2,2])
        [2, 2]
        >>> solve([4,9,5], [9,4,9,8,4])
        [4, 9]
    """
    # Choose the smaller array to build the frequency map, minimizing extra space.
    if len(nums1) <= len(nums2):
        smaller, larger = nums1, nums2
    else:
        smaller, larger = nums2, nums1

    frequency: dict[int, int] = {}
    for value in smaller:
        frequency[value] = frequency.get(value, 0) + 1  # count occurrences

    intersection: list[int] = []
    for value in larger:
        count = frequency.get(value, 0)
        if count > 0:
            intersection.append(value)          # add to result
            frequency[value] = count - 1        # decrement remaining count

    return intersection