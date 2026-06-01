METADATA = {
    "id": 1539,
    "name": "Kth Missing Positive Number",
    "slug": "kth-missing-positive-number",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "array"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the kth positive integer that is missing from a strictly increasing array of positive integers.",
}

def solve(arr: list[int], k: int) -> int:
    """
    Finds the kth missing positive integer using binary search.

    The core logic relies on the fact that for any index i, the number of 
    missing positive integers before arr[i] is given by: arr[i] - (i + 1).

    Args:
        arr: A strictly increasing list of positive integers.
        k: The target rank of the missing integer to find.

    Returns:
        The kth missing positive integer.

    Examples:
        >>> solve([2, 3, 4, 7, 11], 5)
        5
        >>> solve([1, 2, 3, 4], 2)
        6
    """
    left = 0
    right = len(arr) - 1

    # Binary search to find the largest index where the number of missing 
    # elements is less than k.
    while left <= right:
        mid = (left + right) // 2
        # Calculate how many numbers are missing up to index mid
        missing_count = arr[mid] - (mid + 1)

        if missing_count < k:
            left = mid + 1
        else:
            right = mid - 1

    # After the loop, 'right' is the largest index such that missing_count < k.
    # The kth missing number is between arr[right] and arr[right + 1].
    # Formula derivation:
    # Result = arr[right] + (k - missing_count_at_right)
    # Result = arr[right] + k - (arr[right] - (right + 1))
    # Result = k + right + 1
    # Since 'left' ends up being 'right + 1' after the loop:
    return k + left
