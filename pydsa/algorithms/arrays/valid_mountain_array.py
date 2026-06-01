METADATA = {
    "id": 941,
    "name": "Valid Mountain Array",
    "slug": "valid-mountain-array",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array_traversal", "monotonic"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if an array is a valid mountain array where elements strictly increase to a peak and then strictly decrease.",
}

def solve(arr: list[int]) -> bool:
    """
    Determines if the given array follows a mountain pattern.
    
    A mountain array must:
    1. Have at least 3 elements.
    2. Have a single peak such that elements strictly increase to the peak
       and strictly decrease after the peak.
    3. The peak cannot be the first or the last element.

    Args:
        arr: A list of integers to evaluate.

    Returns:
        True if the array is a valid mountain array, False otherwise.

    Examples:
        >>> solve([0, 3, 2, 1])
        True
        >>> solve([3, 5, 5])
        False
        >>> solve([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        False
    """
    n = len(arr)
    
    # A mountain array must have at least 3 elements (up, peak, down)
    if n < 3:
        return False

    i = 0

    # Walk up the mountain: strictly increasing
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    # The peak cannot be the first element (must have an ascent)
    # or the last element (must have a descent)
    if i == 0 or i == n - 1:
        return False

    # Walk down the mountain: strictly decreasing
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    # If we reached the end of the array, it is a valid mountain
    return i == n - 1
