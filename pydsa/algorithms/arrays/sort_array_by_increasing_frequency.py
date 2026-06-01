METADATA = {
    "id": 1636,
    "name": "Sort Array by Increasing Frequency",
    "slug": "sort_array_by_increasing_frequency",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort the array by increasing frequency, breaking ties by larger value.",
}


def solve(nums: list[int]) -> list[int]:
    """Sort an array by increasing frequency, with ties broken by larger value.

    Args:
        nums: List of integers to be sorted.

    Returns:
        A new list of integers sorted first by frequency (ascending) and then by
        value (descending) when frequencies are equal.

    Examples:
        >>> solve([1,1,2,2,2,3])
        [3, 1, 1, 2, 2, 2]
        >>> solve([2,3,1,3,2])
        [1, 3, 3, 2, 2]
    """
    # Count the frequency of each number.
    frequency: dict[int, int] = {}
    for number in nums:
        frequency[number] = frequency.get(number, 0) + 1

    # Sort using a key that prioritizes lower frequency and higher value.
    sorted_nums = sorted(nums, key=lambda x: (frequency[x], -x))

    return sorted_nums