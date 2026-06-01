METADATA = {
    "id": 2626,
    "name": "Array Reduce Transformation",
    "slug": "array-reduce-transformation",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "functional_programming"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Apply a reduction operation to an array using a provided callback function to transform elements into a single value.",
}

from typing import Callable, Any

def solve(nums: list[int], callback: Callable[[int, int], int]) -> int:
    """
    Reduces an array of integers to a single value using a callback function.

    The reduction starts with the first element of the array as the initial 
    accumulator. Each subsequent element is processed by applying the 
    callback function to the current accumulator and the next element.

    Args:
        nums: A list of integers to be reduced.
        callback: A function that takes two integers and returns an integer.

    Returns:
        The final accumulated integer value.

    Raises:
        ValueError: If the input list 'nums' is empty.

    Examples:
        >>> solve([1, 2, 3, 4], lambda x, y: x + y)
        10
        >>> solve([1, 2, 3, 4], lambda x, y: x * y)
        24
    """
    if not nums:
        raise ValueError("The input array 'nums' cannot be empty.")

    # Initialize the accumulator with the first element of the array
    accumulator = nums[0]

    # Iterate through the rest of the array starting from the second element
    for index in range(1, len(nums)):
        # Update the accumulator by applying the callback to the current 
        # accumulator and the next element in the sequence
        accumulator = callback(accumulator, nums[index])

    return accumulator
