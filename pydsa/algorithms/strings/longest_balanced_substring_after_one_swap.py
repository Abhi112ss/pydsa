METADATA = {
    "id": 3900,
    "name": "Longest Balanced Substring After One Swap",
    "slug": "longest_balanced_substring_after_one_swap",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "two_pointer", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest substring consisting of an equal number of '0's and '1's after performing at most one swap between two characters.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest balanced substring (equal 0s and 1s) 
    after performing at most one swap between two characters in the string.

    Args:
        s: The input binary string.

    Returns:
        The length of the longest balanced substring possible after one swap.

    Examples:
        >>> solve("01011")
        4
        >>> solve("00011")
        4
        >>> solve("111000")
        6
    """
    n = len(s)
    if n == 0:
        return 0

    # Convert string to list for easy swapping
    chars = list(s)
    max_len = 0

    def get_max_balanced(arr: list[str]) -> int:
        """Helper to find the longest balanced substring in a fixed array using O(n)."""
        # A balanced substring has count(0) == count(1).
        # Let 0 be -1 and 1 be 1. A balanced substring has sum 0.
        # We use a hash map to store the first occurrence of each prefix sum.
        prefix_sum = 0
        # Map prefix sum to the earliest index it was seen
        # Initialize with {0: -1} to handle substrings starting from index 0
        sum_map = {0: -1}
        current_max = 0
        
        for i, char in enumerate(arr):
            prefix_sum += 1 if char == '1' else -1
            if prefix_sum in sum_map:
                # Length is current index minus the index where this sum was first seen
                current_max = max(current_max, i - sum_map[prefix_sum])
            else:
                sum_map[prefix_sum] = i
        return current_max

    # Case 1: No swap performed (or swap results in same string)
    max_len = get_max_balanced(chars)

    # Case 2: Try all possible swaps
    # Note: To optimize, we only swap if it actually changes the string.
    # Since we want to maximize balanced substrings, we iterate all pairs.
    for i in range(n):
        for j in range(i + 1, n):
            if chars[i] != chars[j]:
                # Perform swap
                chars[i], chars[j] = chars[j], chars[i]
                
                # Calculate longest balanced substring for this configuration
                max_len = max(max_len, get_max_balanced(chars))
                
                # Backtrack (swap back)
                chars[i], chars[j] = chars[j], chars[i]

    return max_len
