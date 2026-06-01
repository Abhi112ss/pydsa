METADATA = {
    "id": 3713,
    "name": "Longest Balanced Substring I",
    "slug": "longest_balanced_substring_i",
    "category": "Strings",
    "aliases": [],
    "tags": ["sliding_window", "strings", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring consisting of an equal number of '0's and '1's where all '0's appear before all '1's.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest substring consisting of an equal number 
    of '0's followed by an equal number of '1's.

    Args:
        s: The input string consisting of '0's and '1's.

    Returns:
        The length of the longest balanced substring of the form '0...01...1'.

    Examples:
        >>> solve("0011")
        4
        >>> solve("0101")
        2
        >>> solve("00011")
        4
    """
    max_length = 0
    i = 0
    n = len(s)

    while i < n:
        zeros_count = 0
        ones_count = 0

        # Count consecutive zeros
        while i < n and s[i] == '0':
            zeros_count += 1
            i += 1
        
        # Count consecutive ones immediately following the zeros
        while i < n and s[i] == '1':
            ones_count += 1
            i += 1
        
        # The balanced part is limited by the smaller of the two counts
        # A balanced substring '0...01...1' must have equal counts.
        # If we have three 0s and two 1s, the longest balanced is '0011' (length 4).
        if zeros_count > 0 and ones_count > 0:
            current_balanced_length = 2 * min(zeros_count, ones_count)
            if current_balanced_length > max_length:
                max_length = current_balanced_length
        
        # If we encountered a '0' after '1's, the loop continues.
        # If we encountered a '0' that was part of the 'ones' block (not possible by logic),
        # we must ensure we don't skip characters. The current structure handles 
        # the transition from 0s to 1s and then looks for the next block of 0s.
        
        # If we stopped because we hit a '0' after '1's, the outer loop 
        # will pick up from that '0' in the next iteration.
        # However, if we stopped because we hit the end, we are done.
        # If we stopped because we hit a '0' after '1's, the 'i' is already at that '0'.
        
        # Special case: if we didn't increment i (e.g., string starts with '1'), 
        # we must increment to avoid infinite loop.
        if zeros_count == 0 and ones_count == 0 and i < n:
            i += 1

    return max_length
