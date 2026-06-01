METADATA = {
    "id": 2634,
    "name": "Filter Elements from Array",
    "slug": "filter_elements_from_array",
    "category": "array",
    "aliases": [],
    "tags": ["array", "iteration", "filter"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return a new list containing only the elements that satisfy a given predicate.",
}

from typing import Callable

def solve(nums: list[int], fn: Callable[[int], bool]) -> list[int]:
    """Filters elements from an array based on a predicate.

    Args:
        nums: List of integers to be filtered.
        fn: A callable that takes an integer and returns True if the element should be kept.

    Returns:
        A list containing only the elements of nums for which fn returns True.

    Examples:
        >>> solve([1, 2, 3, 4, 5], lambda x: x % 2 == 1)
        [1, 3, 5]
        >>> solve([5, 6, 7, 8], lambda x: x > 6)
        [7, 8]
    """
    filtered: list[int] = []
    for element in nums:
        if fn(element):
            filtered.append(element)  # keep element that satisfies predicate
    return filtered