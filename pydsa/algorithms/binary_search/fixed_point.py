METADATA = {
    "id": 1064,
    "name": "Fixed Point",
    "slug": "fixed_point",
    "category": "Algorithms",
    "aliases": [],
    "tags": ["binary_search", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find an index i where arr[i] == i in a sorted distinct array.",
}


def solve(arr: list[int]) -> int:
    """Find a fixed point in a sorted array of distinct integers.

    A fixed point is an index ``i`` such that ``arr[i] == i``.

    Args:
        arr: A list of distinct integers sorted in non‑decreasing order.

    Returns:
        The index ``i`` where ``arr[i] == i`` if it exists; otherwise ``-1``.

    Examples:
        >>> solve([-10, -5, 0, 3, 7])
        3
        >>> solve([0, 2, 5, 8, 17])
        0
        >>> solve([1, 2, 3])
        -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        # If the middle element matches its index, we have found a fixed point.
        if arr[mid] == mid:
            return mid
        # If arr[mid] < mid, any fixed point must be to the right.
        if arr[mid] < mid:
            left = mid + 1
        else:
            # Otherwise, it must be to the left.
            right = mid - 1

    return -1