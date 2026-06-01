METADATA = {
    "id": 1200,
    "name": "Minimum Absolute Difference",
    "slug": "minimum_absolute_difference",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find all pairs of elements with the smallest absolute difference.",
}


def solve(arr: list[int]) -> list[list[int]]:
    """Return all pairs of distinct elements with the minimum absolute difference.

    Args:
        arr: A list of distinct integers.

    Returns:
        A list of pairs [a, b] where a < b, each pair has the smallest possible
        absolute difference among all pairs in the input. The list of pairs is
        sorted in ascending order first by the first element then by the second.

    Examples:
        >>> solve([4, 2, 1, 3])
        [[1, 2], [2, 3], [3, 4]]
        >>> solve([5, 4, 3, 2])
        [[2, 3], [3, 4], [4, 5]]
        >>> solve([1])
        []
    """
    # If there are fewer than two elements, no pair can be formed.
    if len(arr) < 2:
        return []

    # Sort the array to bring closest values next to each other.
    sorted_arr = sorted(arr)

    # Compute the minimum difference between consecutive elements.
    min_diff = min(
        sorted_arr[i + 1] - sorted_arr[i] for i in range(len(sorted_arr) - 1)
    )

    # Collect all adjacent pairs whose difference equals the minimum.
    result: list[list[int]] = [
        [sorted_arr[i], sorted_arr[i + 1]]
        for i in range(len(sorted_arr) - 1)
        if sorted_arr[i + 1] - sorted_arr[i] == min_diff
    ]

    return result