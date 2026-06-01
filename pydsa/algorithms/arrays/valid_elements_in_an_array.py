METADATA = {
    "id": 3912,
    "name": "Valid Elements in an Array",
    "slug": "valid_elements_in_an_array",
    "category": "Arrays",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if all elements in an array satisfy a specific set of valid criteria using an efficient lookup mechanism.",
}

def solve(nums: list[int], valid_criteria: list[int]) -> bool:
    """
    Checks if every element in the input array exists within the set of valid criteria.

    Args:
        nums: A list of integers to be validated.
        valid_criteria: A list of integers representing the allowed values.

    Returns:
        True if all elements in nums are present in valid_criteria, False otherwise.

    Examples:
        >>> solve([1, 2, 3], [1, 2, 3, 4])
        True
        >>> solve([1, 5, 3], [1, 2, 3, 4])
        False
    """
    # Convert the criteria list into a hash set for O(1) average time complexity lookups
    criteria_set = set(valid_criteria)

    # Iterate through each number in the input array
    for number in nums:
        # If any number is not found in the set, the entire array is invalid
        if number not in criteria_set:
            return False

    # If the loop completes, all elements are valid
    return True
