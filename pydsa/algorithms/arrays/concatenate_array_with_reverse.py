METADATA = {
    "id": 3925,
    "name": "Concatenate Array With Reverse",
    "slug": "concatenate-array-with-reverse",
    "category": "Array",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Create a new array by appending the reverse of the input array to the original array.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Concatenates the original array with its reversed version.

    Args:
        nums: A list of integers.

    Returns:
        A new list containing the original elements followed by the elements in reverse order.

    Examples:
        >>> solve([1, 2, 3])
        [1, 2, 3, 3, 2, 1]
        >>> solve([10])
        [10, 10]
        >>> solve([])
        []
    """
    # Create a copy of the original list to avoid mutating the input
    # and then extend it with the reversed version of the list.
    # Slicing with [::-1] is an efficient O(n) way to reverse in Python.
    return nums + nums[::-1]
