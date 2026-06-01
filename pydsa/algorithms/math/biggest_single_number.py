METADATA = {
    "id": 619,
    "name": "Biggest Single Number",
    "slug": "biggest_single_number",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the largest integer that occurs exactly once in the array, or -1 if none.",
}


from collections import Counter
from typing import List


def solve(nums: List[int]) -> int:
    """Return the biggest number that appears exactly once.

    Args:
        nums: List of integers to evaluate.

    Returns:
        The largest integer with a frequency of one, or -1 if no such integer exists.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 4])
        4
        >>> solve([5, 5, 5])
        -1
        >>> solve([10, 9, 8, 7])
        10
    """
    # Count occurrences of each number.
    frequency_map = Counter(nums)

    # Filter numbers that appear exactly once.
    unique_numbers = [number for number, count in frequency_map.items() if count == 1]

    # If there are no unique numbers, return -1.
    if not unique_numbers:
        return -1

    # Return the maximum among the unique numbers.
    return max(unique_numbers)