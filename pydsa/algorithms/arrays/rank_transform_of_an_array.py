METADATA = {
    "id": 1331,
    "name": "Rank Transform of an Array",
    "slug": "rank_transform_of_an_array",
    "category": "array",
    "aliases": [],
    "tags": ["sorting", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Replace each element with its rank among the distinct sorted values.",
}


def solve(arr: list[int]) -> list[int]:
    """Return the rank transform of the given integer array.

    Args:
        arr: A list of integers.

    Returns:
        A list where each element is replaced by its rank (1‑based) among the
        distinct values of ``arr`` when sorted in ascending order.

    Examples:
        >>> solve([40, 10, 20, 30])
        [4, 1, 2, 3]
        >>> solve([100, 100, 100])
        [1, 1, 1]
        >>> solve([-10, -20, -30])
        [3, 2, 1]
    """
    # Obtain the sorted list of unique values.
    unique_sorted = sorted(set(arr))

    # Map each unique value to its rank (1‑based index).
    value_to_rank = {value: index + 1 for index, value in enumerate(unique_sorted)}

    # Build the result by replacing each element with its rank.
    return [value_to_rank[value] for value in arr]