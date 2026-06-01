METADATA = {
    "id": 3499,
    "name": "Maximize Active Section with Trade I",
    "slug": "maximize_active_section_with_trade_i",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum length of a contiguous subarray of active trades given a single trade modification constraint.",
}

def solve(trades: list[int], k: int) -> int:
    """
    Calculates the maximum length of a contiguous section of active trades (value 1)
    given that you can change at most 'k' inactive trades (value 0) to active.

    Args:
        trades: A list of integers where 1 represents an active trade and 0 represents inactive.
        k: The maximum number of inactive trades that can be converted to active.

    Returns:
        The maximum length of a contiguous subarray containing only 1s after at most k conversions.

    Examples:
        >>> solve([1, 0, 1, 1, 0, 1], 1)
        4
        >>> solve([0, 0, 0], 2)
        2
        >>> solve([1, 1, 1], 0)
        3
    """
    max_length = 0
    left = 0
    zero_count = 0
    n = len(trades)

    # Use a sliding window approach to find the longest subarray 
    # containing at most 'k' zeros.
    for right in range(n):
        # If we encounter an inactive trade, increment our zero counter
        if trades[right] == 0:
            zero_count += 1

        # If the number of zeros in the current window exceeds k,
        # shrink the window from the left until zero_count is within limits.
        while zero_count > k:
            if trades[left] == 0:
                zero_count -= 1
            left += 1

        # The current window [left, right] is valid, update the maximum length found.
        current_window_size = right - left + 1
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length
