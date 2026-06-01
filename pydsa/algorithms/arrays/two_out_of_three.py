METADATA = {
    "id": 2032,
    "name": "Two Out of Three",
    "slug": "two_out_of_three",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "array_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return distinct integers appearing in at least two of the three given arrays.",
}


def solve(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    """Return distinct integers that appear in at least two of the three input arrays.

    Args:
        nums1: First list of integers.
        nums2: Second list of integers.
        nums3: Third list of integers.

    Returns:
        A list of distinct integers that are present in at least two of the three arrays.
        The order of elements in the returned list does not matter.

    Examples:
        >>> solve([1,1,3,2], [2,3], [3])
        [2, 3]
        >>> solve([3,1], [2,3], [1,2])
        [1, 2, 3]
    """
    # Convert each array to a set to ensure each element contributes at most once per array.
    unique_nums1 = set(nums1)
    unique_nums2 = set(nums2)
    unique_nums3 = set(nums3)

    frequency_map: dict[int, int] = {}

    # Increment count for elements from the first array.
    for value in unique_nums1:
        frequency_map[value] = frequency_map.get(value, 0) + 1

    # Increment count for elements from the second array.
    for value in unique_nums2:
        frequency_map[value] = frequency_map.get(value, 0) + 1

    # Increment count for elements from the third array.
    for value in unique_nums3:
        frequency_map[value] = frequency_map.get(value, 0) + 1

    # Collect elements that appear in at least two arrays (frequency >= 2).
    result: list[int] = [value for value, count in frequency_map.items() if count >= 2]

    return result