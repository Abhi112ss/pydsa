METADATA = {
    "id": 2464,
    "name": "Minimum Subarrays in a Valid Split",
    "slug": "minimum-subarrays-in-a-valid-split",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Split an array into minimum number of subarrays such that each subarray contains only even numbers or only odd numbers.",
}

def solve(nums: list[int]) -> int:
    """
    Splits the array into the minimum number of subarrays where each subarray 
    contains only even or only odd numbers.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of subarrays required for a valid split.

    Examples:
        >>> solve([2, 3, 5, 4])
        3
        >>> solve([1, 2, 3, 4])
        4
        >>> solve([2, 4, 6, 8])
        1
    """
    if not nums:
        return 0

    subarray_count = 1
    # Track if the current subarray contains an even or an odd number
    # We use None to represent that we haven't encountered any number in the current subarray yet
    current_parity = None

    for num in nums:
        # Determine parity: 0 for even, 1 for odd
        num_parity = num % 2

        if current_parity is None:
            # First element of a new subarray
            current_parity = num_parity
        elif num_parity != current_parity:
            # If the current number's parity differs from the subarray's parity,
            # we must start a new subarray.
            subarray_count += 1
            current_parity = num_parity
        else:
            # Parity matches, continue the current subarray
            continue

    return subarray_count
