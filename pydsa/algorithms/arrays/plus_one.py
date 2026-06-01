METADATA = {
    "id": 66,
    "name": "Plus One",
    "slug": "plus-one",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a large integer represented as an integer array digits, increment the integer by one.",
}

def solve(digits: list[int]) -> list[int]:
    """
    Increments the integer represented by the digits array by one.

    Args:
        digits: A list of integers representing a non-negative integer.

    Returns:
        A list of integers representing the incremented integer.
    """
    n = len(digits)
    for index in range(n - 1, -1, -1):
        if digits[index] < 9:
            digits[index] += 1
            return digits
        digits[index] = 0
    
    return [1] + digits