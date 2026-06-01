METADATA = {
    "id": 1089,
    "name": "Duplicate Zeros",
    "slug": "duplicate_zeros",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Duplicates each zero in-place within a fixed-length integer array, shifting subsequent elements to the right.",
}


def solve(arr: list[int]) -> None:
    """Duplicate each zero in the given list in-place.

    Args:
        arr: A list of integers representing the fixed-length array.

    Returns:
        None. The input list is modified directly.

    Example:
        >>> nums = [1,0,2,3,0,4,5,0]
        >>> solve(nums)
        >>> nums
        [1,0,0,2,3,0,0,4]
    """
    length: int = len(arr)
    zero_count: int = arr.count(0)

    # Iterate from the end, moving elements to their new positions.
    for index in range(length - 1, -1, -1):
        if arr[index] == 0:
            # Place the rightmost zero if it fits within the array.
            if index + zero_count < length:
                arr[index + zero_count] = 0
            zero_count -= 1  # One zero has been accounted for.
            # Place the left zero (the duplicate) if it fits.
            if index + zero_count < length:
                arr[index + zero_count] = 0
        else:
            # Shift non-zero element to its new position.
            if index + zero_count < length:
                arr[index + zero_count] = arr[index]