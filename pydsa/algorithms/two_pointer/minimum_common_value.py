METADATA = {
    "id": 2540,
    "name": "Minimum Common Value",
    "slug": "minimum-common-value",
    "category": "Two Pointers",
    "aliases": [],
    "tags": ["two_pointer", "binary_search", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Find the smallest integer that appears in both sorted arrays.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Finds the minimum common value between two sorted arrays using the two-pointer technique.

    Args:
        nums1: A sorted list of integers.
        nums2: A sorted list of integers.

    Returns:
        The smallest integer present in both lists. Returns -1 if no common value exists.

    Examples:
        >>> solve([4, 5, 6], [2, 3, 5, 8, 10])
        5
        >>> solve([1, 2, 3], [4, 5, 6])
        -1
    """
    pointer1 = 0
    pointer2 = 0
    len1 = len(nums1)
    len2 = len(nums2)

    # Traverse both arrays using two pointers
    while pointer1 < len1 and pointer2 < len2:
        val1 = nums1[pointer1]
        val2 = nums2[pointer2]

        if val1 == val2:
            # Since arrays are sorted, the first match found is the minimum
            return val1
        elif val1 < val2:
            # Move the pointer in the array with the smaller value forward
            pointer1 += 1
        else:
            # Move the pointer in the array with the smaller value forward
            pointer2 += 1

    return -1
