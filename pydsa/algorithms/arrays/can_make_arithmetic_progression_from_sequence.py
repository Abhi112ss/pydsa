METADATA = {
    "id": 1502,
    "name": "Can Make Arithmetic Progression From Sequence",
    "slug": "can_make_arithmetic_progression_from_sequence",
    "category": "array",
    "aliases": [],
    "tags": ["sorting", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Determine if the given array can be reordered to form an arithmetic progression.",
}


def solve(arr: list[int]) -> bool:
    """Determine whether the input array can be reordered to form an arithmetic progression.

    Args:
        arr: A list of integers.

    Returns:
        True if the elements of ``arr`` can be rearranged to form an arithmetic progression,
        otherwise False.

    Examples:
        >>> solve([3, 5, 1])
        True
        >>> solve([1, 2, 4])
        False
    """
    # An array with fewer than two elements is trivially an arithmetic progression.
    if len(arr) < 2:
        return True

    # Sort the array in-place to examine consecutive differences.
    arr.sort()

    # The common difference is defined by the first two elements after sorting.
    common_difference = arr[1] - arr[0]

    # Verify that each subsequent pair maintains the same difference.
    for index in range(2, len(arr)):
        if arr[index] - arr[index - 1] != common_difference:
            return False

    return True
