METADATA = {
    "id": 3101,
    "name": "Count Alternating Subarrays",
    "slug": "count_alternating_subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of subarrays where every two adjacent elements have different parity.",
}

def solve(nums: list[int]) -> int:
    """
    Counts the number of subarrays where adjacent elements have different parity.

    Args:
        nums: A list of integers.

    Returns:
        The total count of alternating parity subarrays.

    Examples:
        >>> solve([2, 3, 4, 5])
        10
        >>> solve([1, 2, 1, 1, 2])
        8
    """
    if not nums:
        return 0

    total_count = 0
    current_alternating_length = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Check if the current element and the previous element have different parity
        # (even/odd or odd/even)
        if (nums[i] % 2) != (nums[i - 1] % 2):
            current_alternating_length += 1
        else:
            # If parity is the same, the alternating sequence breaks.
            # Reset the length to 1 (the current element itself).
            current_alternating_length = 1
        
        # For a sequence of length 'k', adding the k-th element adds 'k' new subarrays
        # ending at that index (e.g., in [2, 3, 4], adding 4 adds [4], [3, 4], [2, 3, 4])
        total_count += current_alternating_length

    # The first element always forms a subarray of length 1
    return total_count + 1
