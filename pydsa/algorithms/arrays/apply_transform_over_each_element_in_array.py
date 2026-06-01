METADATA = {
    "id": 2635,
    "name": "Apply Transform Over Each Element in Array",
    "slug": "apply-transform-over-each-element-in-array",
    "category": "Array",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Apply a given transformation function to each element of an array and return a new array.",
}

from typing import Callable, Any

def solve(nums: list[int], transform: Callable[[int], int]) -> list[int]:
    """
    Applies a transformation function to each element in the input list.

    Args:
        nums: A list of integers to be transformed.
        transform: A function that takes an integer and returns an integer.

    Returns:
        A new list containing the transformed elements.

    Examples:
        >>> solve([1, 2, 3], lambda x: x * 2)
        [2, 4, 6]
        >>> solve([10, 20, 30], lambda x: x - 5)
        [5, 15, 25]
    """
    # Initialize an empty list to store the transformed values
    transformed_list: list[int] = []
    
    # Iterate through each element in the original array
    for number in nums:
        # Apply the callback function and append the result to the new list
        transformed_list.append(transform(number))
        
    return transformed_list
