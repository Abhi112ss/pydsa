METADATA = {
    "id": 1714,
    "name": "Sum Of Special Evenly-Spaced Elements In Array",
    "slug": "sum_of_special_evenly_spaced_elements_in_array",
    "category": "array",
    "aliases": [],
    "tags": ["array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Sum of elements that have another equal element at an even index distance.",
}


def solve(nums: list[int]) -> int:
    """Return the sum of all special evenly-spaced elements in the array.

    An element is *special* if there exists another element with the same value
    whose index differs by an even number (i.e., both indices have the same parity).

    Args:
        nums: List of integers.

    Returns:
        The sum of all elements that are special.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6])
        0
        >>> solve([1, 2, 1, 2, 1, 2])
        9
    """
    # Count occurrences of each value separately for even and odd indices.
    even_counts: dict[int, int] = {}
    odd_counts: dict[int, int] = {}
    for index, value in enumerate(nums):
        if index % 2 == 0:
            even_counts[value] = even_counts.get(value, 0) + 1
        else:
            odd_counts[value] = odd_counts.get(value, 0) + 1

    total_sum = 0
    # Add contributions from even-indexed values that appear at least twice.
    for value, count in even_counts.items():
        if count >= 2:
            total_sum += value * count
    # Add contributions from odd-indexed values that appear at least twice.
    for value, count in odd_counts.items():
        if count >= 2:
            total_sum += value * count

    return total_sum