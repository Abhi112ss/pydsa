METADATA = {
    "id": 3471,
    "name": "Find the Largest Almost Missing Integer",
    "slug": "find-the-largest-almost-missing-integer",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the largest integer in an array that appears exactly once.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the largest integer in the input list that appears exactly once.

    Args:
        nums: A list of integers.

    Returns:
        The largest integer that appears exactly once in the list. 
        If no such integer exists, returns -1.

    Examples:
        >>> solve([1, 2, 3, 2, 1])
        3
        >>> solve([1, 1, 1, 1])
        -1
        >>> solve([5, 4, 3, 2, 1])
        5
    """
    # Step 1: Count the frequency of each integer using a hash map
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    # Step 2: Iterate through the original list in reverse order 
    # to find the first (largest index-wise, but we need value-wise) 
    # element that satisfies the condition. 
    # Actually, to find the largest VALUE, we should check all unique 
    # elements and find the maximum.
    
    max_almost_missing: int = -1
    
    for num, count in frequency_map.items():
        # Check if the integer appears exactly once
        if count == 1:
            # Update max_almost_missing if current num is larger
            if num > max_almost_missing:
                max_almost_missing = num
                
    return max_almost_missing
