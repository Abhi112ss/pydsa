METADATA = {
    "id": 3159,
    "name": "Find Occurrences of an Element in an Array",
    "slug": "find-occurrences-of-an-element-in-an-array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "array", "linear search"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the first and last index of a target element in an array, returning -1 if not found.",
}

def solve(nums: list[int], target: int) -> list[int]:
    """
    Finds the first and last occurrence of a target element in an integer array.

    Args:
        nums: A list of integers.
        target: The integer value to search for.

    Returns:
        A list containing two integers: [first_index, last_index]. 
        If the target is not found, returns [-1, -1].

    Examples:
        >>> solve([1, 2, 3, 2, 4], 2)
        [1, 3]
        >>> solve([1, 2, 3, 4, 5], 6)
        [-1, -1]
        >>> solve([5, 5, 5, 5, 5], 5)
        [0, 4]
    """
    first_index = -1
    last_index = -1

    # Iterate through the array once to find both indices
    for current_index, value in enumerate(nums):
        if value == target:
            # If this is the first time we encounter the target, set first_index
            if first_index == -1:
                first_index = current_index
            
            # Always update last_index when target is found to capture the latest occurrence
            last_index = current_index

    return [first_index, last_index]
