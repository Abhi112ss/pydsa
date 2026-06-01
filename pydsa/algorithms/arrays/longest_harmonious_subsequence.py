METADATA = {
    "id": 594,
    "name": "Longest Harmonious Subsequence",
    "slug": "longest_harmonious_subsequence",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subsequence where the maximum and minimum values differ by exactly one.",
}


def solve(nums: list[int]) -> int:
    """Return the length of the longest harmonious subsequence.

    A harmonious subsequence is a subsequence where the difference between its
    maximum and minimum elements is exactly 1.

    Args:
        nums: List of integers.

    Returns:
        The maximum length of a harmonious subsequence.

    Examples:
        >>> solve([1, 3, 2, 2, 5, 2, 3, 7])
        5
        >>> solve([1, 2, 3, 4])
        2
        >>> solve([1, 1, 1, 1])
        0
    """
    # Count occurrences of each number.
    frequency: dict[int, int] = {}
    for number in nums:
        frequency[number] = frequency.get(number, 0) + 1

    longest: int = 0
    # For each distinct number, check if its neighbor (num + 1) exists.
    for number, count in frequency.items():
        neighbor_count = frequency.get(number + 1)
        if neighbor_count is not None:
            # Combine counts of the current number and its neighbor.
            combined_length = count + neighbor_count
            if combined_length > longest:
                longest = combined_length

    return longest