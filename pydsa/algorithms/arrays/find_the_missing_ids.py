METADATA = {
    "id": 1613,
    "name": "Find the Missing IDs",
    "slug": "find_the_missing_ids",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return all IDs in the range [1, n] that are absent from the given list.",
}


def solve(ids: list[int]) -> list[int]:
    """Find all missing IDs in the range [1, n].

    Args:
        ids: A list of integers where each integer is between 1 and len(ids) inclusive.
              The list may contain duplicates.

    Returns:
        A sorted list of integers that are missing from the input list.

    Examples:
        >>> solve([3, 1, 2, 5, 3])
        [4]
        >>> solve([1, 2, 3, 4])
        []
        >>> solve([2, 2, 2, 2])
        [1, 3, 4]
    """
    total_ids = len(ids)
    # Store all present IDs in a hash set for O(1) look‑ups.
    present_ids = set(ids)

    missing_ids: list[int] = []
    # Iterate through the full range and collect IDs that are absent.
    for candidate in range(1, total_ids + 1):
        if candidate not in present_ids:
            missing_ids.append(candidate)

    return missing_ids