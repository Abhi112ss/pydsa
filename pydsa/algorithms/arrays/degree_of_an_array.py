METADATA = {
    "id": 697,
    "name": "Degree of an Array",
    "slug": "degree_of_an_array",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the smallest length of a contiguous subarray that has the same degree as the original array.",
}

def solve(nums: list[int]) -> int:
    """Find the smallest length of a contiguous subarray with the same degree as the array.

    The degree of an array is the maximum frequency of any element.
    We track the first and last occurrence of each element and compute
    the span (last - first + 1) for elements achieving the max frequency.

    Args:
        nums: A non-empty list of non-negative integers.

    Returns:
        The length of the shortest contiguous subarray with the same degree as nums.

    Examples:
        >>> solve([1, 2, 2, 3, 1])
        2
        >>> solve([1, 2, 2, 3, 1, 4, 2])
        6
        >>> solve([1])
        1
    """
    # Track frequency, first occurrence index, and last occurrence index per element
    freq: dict[int, int] = {}
    first_occurrence: dict[int, int] = {}
    last_occurrence: dict[int, int] = {}

    for index, value in enumerate(nums):
        freq[value] = freq.get(value, 0) + 1
        if value not in first_occurrence:
            first_occurrence[value] = index
        last_occurrence[value] = index

    # The degree is the maximum frequency across all elements
    max_freq = max(freq.values())

    # Among elements with max frequency, find the smallest span (last - first + 1)
    min_length = len(nums)
    for value, count in freq.items():
        if count == max_freq:
            span = last_occurrence[value] - first_occurrence[value] + 1
            if span < min_length:
                min_length = span

    return min_length