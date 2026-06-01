METADATA = {
    "id": 3667,
    "name": "Sort Array By Absolute Value",
    "slug": "sort-array-by-absolute-value",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort an array of integers based on their absolute values in ascending order.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Sorts an array of integers based on their absolute values.

    If two numbers have the same absolute value, their relative order 
    is preserved (stable sort) or can be defined by their actual values.
    In standard LeetCode interpretations of this problem, if absolute values 
    are equal, the smaller actual value typically comes first.

    Args:
        nums: A list of integers to be sorted.

    Returns:
        A new list of integers sorted by their absolute values.

    Examples:
        >>> solve([1, -2, -3, 3, 2])
        [1, -2, 2, -3, 3]
        >>> solve([-5, 5, 2, -1])
        [-1, 2, -5, 5]
    """
    # We use Python's built-in Timsort which is stable.
    # To handle the case where absolute values are equal, we provide a tuple 
    # as the sort key: (absolute_value, original_value).
    # This ensures that if abs(a) == abs(b), the smaller actual value comes first.
    
    return sorted(nums, key=lambda x: (abs(x), x))
