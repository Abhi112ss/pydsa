METADATA = {
    "id": 2206,
    "name": "Divide Array Into Equal Pairs",
    "slug": "divide-array-into-equal-pairs",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be divided into pairs where each pair consists of two equal elements.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the given array can be divided into pairs of equal elements.

    To form equal pairs, every unique number in the array must appear an 
    even number of times.

    Args:
        nums: A list of integers representing the array to be divided.

    Returns:
        True if the array can be divided into equal pairs, False otherwise.

    Examples:
        >>> solve([1, 2, 2, 1])
        True
        >>> solve([1, 2, 3, 4])
        False
        >>> solve([1, 1, 1, 1])
        True
    """
    # Use a dictionary to count the frequency of each number
    counts: dict[int, int] = {}
    
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    # Check if every frequency is even
    for frequency in counts.values():
        # If any number appears an odd number of times, we cannot form equal pairs
        if frequency % 2 != 0:
            return False
            
    return True
