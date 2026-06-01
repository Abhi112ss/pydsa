METADATA = {
    "id": 1864,
    "name": "Minimum Number of Swaps to Make the Binary String Alternating",
    "slug": "minimum-number-of-swaps-to-make-the-binary-string-alternating",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of swaps to make a binary string alternating, or return -1 if impossible.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of swaps required to make a binary string alternating.

    A swap involves two indices. For a swap to be valid in this context, 
    the number of 0s and 1s must be balanced such that an alternating 
    pattern is mathematically possible.

    Args:
        s: A string consisting of '0's and '1's.

    Returns:
        The minimum number of swaps required, or -1 if it is impossible.

    Examples:
        >>> solve("0100")
        -1
        >>> solve("010")
        0
        >>> solve("111000")
        2
    """
    n = len(s)
    count_zero = s.count('0')
    count_one = n - count_zero

    # An alternating string of length n can only exist if 
    # the difference between counts of 0s and 1s is at most 1.
    if abs(count_zero - count_one) > 1:
        return -1

    def get_swaps(pattern_start: str) -> int:
        """
        Calculates swaps needed to match a specific alternating pattern.
        
        Args:
            pattern_start: The character ('0' or '1') the pattern should start with.
            
        Returns:
            Number of swaps needed, or float('inf') if pattern is impossible 
            due to character count mismatch.
        """
        mismatches = 0
        current_char = pattern_start
        
        # Count how many characters are in the wrong position
        for char in s:
            if char != current_char:
                mismatches += 1
            # Flip the expected character for the next position
            current_char = '1' if current_char == '0' else '0'
        
        # A swap fixes two mismatches (one '0' where '1' should be, 
        # and one '1' where '0' should be). 
        # Therefore, mismatches must be even and we return mismatches // 2.
        if mismatches % 2 != 0:
            return float('inf')
        return mismatches // 2

    # Case 1: Pattern starts with '0' (e.g., 0101...)
    # This is only valid if count_zero >= count_one (for odd n) or count_zero == count_one
    res_start_zero = float('inf')
    if count_zero >= count_one and (n % 2 == 0 or count_zero == count_one + 1):
        res_start_zero = get_swaps('0')

    # Case 2: Pattern starts with '1' (e.g., 1010...)
    # This is only valid if count_one >= count_zero (for odd n) or count_one == count_zero
    res_start_one = float('inf')
    if count_one >= count_zero and (n % 2 == 0 or count_one == count_zero + 1):
        res_start_one = get_swaps('1')

    ans = min(res_start_zero, res_start_one)
    return int(ans) if ans != float('inf') else -1
