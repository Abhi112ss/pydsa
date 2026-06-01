METADATA = {
    "id": 2215,
    "name": "Find the Difference of Two Arrays",
    "slug": "find-the-difference-of-two-arrays",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_set", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Find the unique elements present in one array but not the other, returning them as two separate lists.",
}

def solve(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    """
    Finds the unique elements in nums1 that are not in nums2, and vice versa.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        A list containing two lists:
        - The first list contains elements in nums1 not in nums2.
        - The second list contains elements in nums2 not in nums1.

    Examples:
        >>> solve([1, 2, 3], [2, 4, 6])
        [[1, 3], [4, 6]]
        >>> solve([1, 2, 3, 3], [1, 1, 2, 2])
        [[3], []]
    """
    # Convert both lists to sets to achieve O(1) average lookup time
    # and to automatically handle duplicate elements within the same array.
    set1 = set(nums1)
    set2 = set(nums2)

    # Calculate the set difference: elements in set1 that are not in set2.
    diff1 = list(set1 - set2)
    
    # Calculate the set difference: elements in set2 that are not in set1.
    diff2 = list(set2 - set1)

    return [diff1, diff2]
