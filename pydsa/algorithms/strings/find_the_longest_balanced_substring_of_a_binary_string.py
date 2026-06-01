METADATA = {
    "id": 2609,
    "name": "Find the Longest Balanced Substring of a Binary String",
    "slug": "find-the-longest-balanced-substring-of-a-binary-string",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "two_pointer", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that contains an equal number of consecutive 0s followed by consecutive 1s.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest balanced substring where all 0s come before all 1s.

    A balanced substring is defined as having an equal number of consecutive 0s 
    followed by an equal number of consecutive 1s.

    Args:
        s: A binary string consisting of '0's and '1's.

    Returns:
        The length of the longest balanced substring.

    Examples:
        >>> solve("01")
        2
        >>> solve("0110111")
        2
        >>> solve("00011")
        4
        >>> solve("0011100011")
        4
    """
    max_length = 0
    count_zeros = 0
    count_ones = 0
    
    # We iterate through the string to count consecutive blocks.
    # Since the pattern must be 0s then 1s, we track the current run of 0s
    # and the current run of 1s.
    for i in range(len(s)):
        if s[i] == '0':
            # If we encounter a '0', it resets the '1' count because 
            # a balanced substring must have all 0s before all 1s.
            # However, we don't reset count_zeros immediately; we only 
            # reset count_ones to start a new potential block.
            count_ones = 0
            count_zeros += 1
        else:
            # If we encounter a '1', we increment the '1' count.
            # If we haven't seen any '0's yet, count_ones remains 0 
            # (or we can treat it as a sequence starting with 1, which is invalid).
            if count_zeros > 0:
                count_ones += 1
                # The length of a balanced substring is 2 * min(zeros, ones)
                # because we need an equal number of both.
                current_balanced_len = 2 * min(count_zeros, count_ones)
                if current_balanced_len > max_length:
                    max_length = current_balanced_len
            else:
                # If no zeros have been seen, we can't form a balanced substring.
                count_ones = 0

    # Note: The logic above handles the transition from 0s to 1s.
    # If we hit a '0' after some '1's, count_ones is reset, 
    # and count_zeros starts incrementing again.
    
    # Re-implementing with a cleaner single-pass logic for robustness:
    max_len = 0
    zeros = 0
    ones = 0
    
    for char in s:
        if char == '0':
            zeros += 1
            ones = 0  # Reset ones because 0s must come before 1s
        else:
            if zeros > 0:
                ones += 1
                # The length is twice the minimum of the two consecutive counts
                max_len = max(max_len, 2 * min(zeros, ones))
            else:
                ones = 0
                
    return max_len
