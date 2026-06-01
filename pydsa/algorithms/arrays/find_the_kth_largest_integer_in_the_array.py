METADATA = {
    "id": 1985,
    "name": "Find the Kth Largest Integer in the Array",
    "slug": "find-the-kth-largest-integer-in-the-array",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "heap", "quick_select"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the kth largest integer in an array of integers.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the kth largest integer in the given list.

    Args:
        nums: A list of integers.
        k: The rank (1-indexed) of the integer to find.

    Returns:
        The kth largest integer in the array.

    Examples:
        >>> solve([3, 2, 1, 5, 6, 4], 2)
        5
        >>> solve([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        4
    """
    # Sort the array in descending order to easily access the kth largest element.
    # Python's Timsort is highly optimized and performs in O(n log n).
    nums.sort(reverse=True)

    # Since k is 1-indexed, the kth largest element is at index k - 1.
    return nums[k - 1]
