METADATA = {
    "id": 1299,
    "name": "Replace Elements with Greatest Element on Right Side",
    "slug": "replace-elements-with-greatest-element-on-right-side",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "suffix_max"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Replace every element in an array with the greatest element among the elements to its right, and replace the last element with -1.",
}

def solve(arr: list[int]) -> list[int]:
    """
    Replaces each element in the array with the greatest element to its right.
    The last element is replaced with -1.

    Args:
        arr: A list of integers.

    Returns:
        A list of integers where each element is replaced by the maximum 
        of the elements to its right.

    Examples:
        >>> solve([17, 18, 5, 4, 6, 1])
        [18, 6, 6, 6, 1, -1]
        >>> solve([1])
        [-1]
    """
    n = len(arr)
    if n == 0:
        return []

    # We track the maximum value encountered so far from the right side.
    # Initialize with -1 because the last element's right side is empty.
    current_max = -1

    # Iterate from the end of the array to the beginning.
    # This allows us to update the maximum in a single pass.
    for i in range(n - 1, -1, -1):
        # Store the current element before overwriting it.
        original_value = arr[i]
        
        # Replace the current element with the max found to its right.
        arr[i] = current_max
        
        # Update the current_max for the next element to the left.
        if original_value > current_max:
            current_max = original_value

    return arr
