METADATA = {
    "id": 1356,
    "name": "Sort Integers by The Number of 1 Bits",
    "slug": "sort-integers-by-the-number-of-1-bits",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "bit-manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Sort an array of integers based on the number of set bits (1s) in their binary representation, with ties broken by the integer's value.",
}

def solve(arr: list[int]) -> list[int]:
    """
    Sorts an array of integers based on the number of set bits (1s) in their binary representation.
    If two integers have the same number of set bits, the smaller integer comes first.

    Args:
        arr: A list of integers to be sorted.

    Returns:
        A new list containing the sorted integers.

    Examples:
        >>> solve([0, 1, 2, 3, 4])
        [0, 1, 2, 4, 3]
        >>> solve([3, 9, 17, 15, 16])
        [16, 17, 9, 3, 15]
    """
    
    # The key function returns a tuple: (count_of_ones, original_value).
    # Python's sort is stable and handles tuple comparison lexicographically:
    # It compares the first element (bit count), and if they are equal, 
    # it compares the second element (the value itself).
    
    # bit_count() is available in Python 3.10+ and is highly optimized.
    # For older versions, bin(x).count('1') would be the alternative.
    
    return sorted(arr, key=lambda x: (x.bit_count(), x))
