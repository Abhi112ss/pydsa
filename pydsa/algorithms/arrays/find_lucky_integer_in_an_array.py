METADATA = {
    "id": 1394,
    "name": "Find Lucky Integer in an Array",
    "slug": "find-lucky-integer-in-an-array",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "counting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the largest integer in an array such that the frequency of the integer is equal to its value.",
}

def solve(arr: list[int]) -> int:
    """
    Finds the largest lucky integer in the given array.
    
    A lucky integer is an integer that has a frequency in the array equal to its value.
    If there is no lucky integer, returns -1.

    Args:
        arr: A list of integers.

    Returns:
        The largest lucky integer found, or -1 if no lucky integer exists.

    Examples:
        >>> solve([2, 2, 3, 3, 3])
        3
        >>> solve([1, 2, 2, 3, 3, 3, 4])
        3
        >>> solve([2, 2, 2, 3, 3])
        -1
    """
    # Dictionary to store the frequency of each number
    frequency_map: dict[int, int] = {}
    
    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0) + 1
        
    max_lucky_integer: int = -1
    
    # Iterate through the frequency map to find numbers where key == value
    for num, count in frequency_map.items():
        if num == count:
            # Update max_lucky_integer if the current lucky number is larger
            if num > max_lucky_integer:
                max_lucky_integer = num
                
    return max_lucky_integer
