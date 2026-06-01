METADATA = {
    "id": 2154,
    "name": "Keep Multiplying Found Values by Two",
    "slug": "keep-multiplying-found-values-by-two",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_set", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given an array of integers, repeatedly find a value that exists in the array and multiply it by two until no such value can be found.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Repeatedly finds a value in the array that is a multiple of 2 of a previously 
    found value, starting from k, and returns the total count of such values.

    Args:
        nums: A list of integers.
        k: The starting integer value.

    Returns:
        The total number of values found (including k if it exists in nums).

    Examples:
        >>> solve([1, 2, 4, 8, 16], 1)
        5
        >>> solve([1, 2, 4, 8, 16], 3)
        0
        >>> solve([1, 2, 4, 8, 16], 2)
        4
    """
    # Convert list to a set for O(1) average time complexity lookups
    lookup_set = set(nums)
    count = 0
    current_value = k

    # Continue as long as the current value exists in the set
    while current_value in lookup_set:
        count += 1
        # Double the value for the next iteration
        current_value *= 2
        
    return count
