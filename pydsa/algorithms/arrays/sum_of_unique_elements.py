METADATA = {
    "id": 1748,
    "name": "Sum of Unique Elements",
    "slug": "sum-of-unique-elements",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the sum of all elements in an array that appear exactly once.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the sum of elements in the array that occur exactly once.

    Args:
        arr: A list of integers.

    Returns:
        The sum of all elements that have a frequency of exactly one.

    Examples:
        >>> solve([1, 2, 3, 2])
        4
        >>> solve([1, 1, 1, 1])
        0
        >>> solve([1, 2, 3, 4, 5])
        15
    """
    # Dictionary to store the frequency of each number
    frequency_map: dict[int, int] = {}

    # First pass: Count the occurrences of each element
    for number in arr:
        frequency_map[number] = frequency_map.get(number, 0) + 1

    unique_sum: int = 0
    # Second pass: Sum elements that appeared exactly once
    for number, count in frequency_map.items():
        if count == 1:
            unique_sum += number

    return unique_sum
