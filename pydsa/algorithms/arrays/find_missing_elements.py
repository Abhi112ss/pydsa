METADATA = {
    "id": 3731,
    "name": "Find Missing Elements",
    "slug": "find_missing_elements",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all elements in the range [min(nums), max(nums)] that are not present in the input array.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Finds all integers in the range [min(nums), max(nums)] that are missing from the input list.

    Args:
        nums: A list of integers.

    Returns:
        A sorted list of integers that are missing from the range defined by the 
        minimum and maximum values in the input list.

    Examples:
        >>> solve([4, 3, 2, 7, 8, 2, 3, 1])
        [5, 6]
        >>> solve([1, 2, 3])
        []
        >>> solve([1, 5])
        [2, 3, 4]
    """
    if not nums:
        return []

    # Convert the list to a set for O(1) average time complexity lookups
    num_set = set(nums)
    
    # Determine the boundaries of the range
    min_val = min(nums)
    max_val = max(nums)
    
    missing_elements = []
    
    # Iterate through the full range from min to max
    for current_num in range(min_val, max_val + 1):
        # If the current number is not in our set, it is a missing element
        if current_num not in num_set:
            missing_elements.append(current_num)
            
    return missing_elements
