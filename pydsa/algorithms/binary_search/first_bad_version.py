METADATA = {
    "id": 278,
    "name": "First Bad Version",
    "slug": "first_bad_version",
    "category": "binary_search",
    "aliases": [],
    "tags": ["binary_search", "interactive"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the first version that is bad using binary search.",
}


from typing import Callable


def solve(total_versions: int, is_bad_version: Callable[[int], bool]) -> int:
    """Find the first bad version among `total_versions` using binary search.

    Args:
        total_versions: The total number of versions, numbered from 1 to `total_versions`.
        is_bad_version: A callable that returns True if a given version is bad,
            otherwise False.

    Returns:
        The smallest version number that is bad.

    Examples:
        >>> # Suppose versions 4,5,6 are bad
        >>> bad = {4, 5, 6}
        >>> def api(v: int) -> bool:
        ...     return v in bad
        >>> solve(6, api)
        4
        >>> # If only version 1 is bad
        >>> solve(1, lambda v: True)
        1
    """
    left = 1
    right = total_versions

    while left < right:
        # Compute mid without overflow and check the condition
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            # Bad version found, continue searching left side (including mid)
            right = mid
        else:
            # Current version is good, discard left side including mid
            left = mid + 1

    # At this point left == right and points to the first bad version
    return left