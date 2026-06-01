METADATA = {
    "id": 2875,
    "name": "Minimum Size Subarray in Infinite Array",
    "slug": "minimum-size-subarray-in-infinite-array",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "math", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(k)",
    "space_complexity": "O(1)",
    "description": "Find the minimum length of a contiguous subarray whose sum is at least target in an infinite array formed by repeating a pattern.",
}

def solve(target: int, pattern: list[int]) -> int:
    """
    Finds the minimum length of a contiguous subarray in an infinite array 
    formed by repeating 'pattern' such that the sum is at least 'target'.

    Args:
        target: The required minimum sum.
        pattern: The base array that repeats infinitely.

    Returns:
        The minimum length of the subarray.

    Examples:
        >>> solve(10, [1, 2, 3])
        7
        >>> solve(1, [1, 2, 3])
        1
    """
    pattern_sum = sum(pattern)
    n = len(pattern)

    # Calculate how many full cycles of the pattern are needed.
    # We subtract 1 from target to handle cases where target is an exact multiple 
    # of pattern_sum, ensuring we don't over-calculate full cycles unnecessarily.
    full_cycles = max(0, (target - 1) // pattern_sum)
    remaining_target = target - (full_cycles * pattern_sum)

    # To handle the "wrap-around" nature of the infinite array, 
    # we simulate the sliding window on a doubled pattern.
    # This covers any subarray that might span across the boundary of two cycles.
    extended_pattern = pattern + pattern
    
    min_len = float('inf')
    current_sum = 0
    left = 0

    # Standard sliding window approach on the extended pattern
    for right in range(len(extended_pattern)):
        current_sum += extended_pattern[right]

        while current_sum >= remaining_target:
            # The length is the window size in the extended array + the full cycles
            current_len = (right - left + 1) + (full_cycles * n)
            if current_len < min_len:
                min_len = current_len
            
            # Shrink window from the left
            current_sum -= extended_pattern[left]
            left += 1

    return int(min_len)
