METADATA = {
    "id": 88,
    "name": "Merge Sorted Array",
    "slug": "merge-sorted-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["two_pointers", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(m + n)",
    "space_complexity": "O(1)",
    "description": "Merge two sorted integer arrays into the first array as a single sorted array.",
}

def solve(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merges nums2 into nums1 as one sorted array in-place.

    The algorithm uses three pointers starting from the end of the arrays
    to avoid overwriting elements in nums1 that haven't been processed yet.

    Args:
        nums1: The first sorted array, which has a total size of m + n.
        m: The number of initialized elements in nums1.
        nums2: The second sorted array.
        n: The number of elements in nums2.

    Returns:
        None. The operation is performed in-place on nums1.

    Examples:
        >>> nums1 = [1, 2, 3, 0, 0, 0]
        >>> m = 3
        >>> nums2 = [2, 5, 6]
        >>> n = 3
        >>> solve(nums1, m, nums2, n)
        >>> print(nums1)
        [1, 2, 2, 3, 5, 6]
    """
    # Pointer for the last initialized element in nums1
    pointer_one = m - 1
    # Pointer for the last element in nums2
    pointer_two = n - 1
    # Pointer for the last position in the combined nums1 array
    write_index = m + n - 1

    # Iterate while there are elements to compare in both arrays
    while pointer_one >= 0 and pointer_two >= 0:
        if nums1[pointer_one] > nums2[pointer_two]:
            nums1[write_index] = nums1[pointer_one]
            pointer_one -= 1
        else:
            nums1[write_index] = nums2[pointer_two]
            pointer_two -= 1
        write_index -= 1

    # If there are remaining elements in nums2, copy them.
    # We don't need to worry about remaining elements in nums1 because 
    # they are already in their correct positions.
    while pointer_two >= 0:
        nums1[write_index] = nums2[pointer_two]
        pointer_two -= 1
        write_index -= 1
