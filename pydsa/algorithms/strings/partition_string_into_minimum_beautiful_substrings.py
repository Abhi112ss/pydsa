METADATA = {
    "id": 2767,
    "name": "Partition String Into Minimum Beautiful Substrings",
    "slug": "partition-string-into-minimum-beautiful-substrings",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Partition a string into the minimum number of beautiful substrings where each substring contains at least one character that does not appear in any previous substring.",
}

def solve(s: str) -> int:
    """
    Partitions the string into the minimum number of beautiful substrings.
    
    A substring is beautiful if it contains at least one character that 
    has not appeared in any of the previous substrings.

    Args:
        s: The input string to partition.

    Returns:
        The minimum number of beautiful substrings required.

    Examples:
        >>> solve("abacaba")
        2
        >>> solve("aaaaa")
        1
    """
    n = len(s)
    # memo stores the minimum partitions needed for the suffix starting at index 'start'
    # given the set of characters already seen in previous substrings.
    # Since the set of characters can be represented by a bitmask (26 bits),
    # we use (start, mask) as the key.
    memo: dict[tuple[int, int], int] = {}

    def backtrack(start_index: int, seen_mask: int) -> int:
        """
        Recursive helper to find the minimum partitions using memoization.
        
        Args:
            start_index: The current starting position in the string.
            seen_mask: A bitmask representing characters encountered in previous substrings.
            
        Returns:
            Minimum partitions for the remaining suffix.
        """
        if start_index == n:
            return 0
        
        state = (start_index, seen_mask)
        if state in memo:
            return memo[state]

        # Initialize with a value larger than any possible result (n)
        min_partitions = n + 1
        current_substring_mask = 0
        has_new_char = False

        # Try all possible end positions for the current substring
        for end_index in range(start_index, n):
            char_idx = ord(s[end_index]) - ord('a')
            current_substring_mask |= (1 << char_idx)
            
            # Check if this substring contains at least one character not in seen_mask
            if not has_new_char:
                if (current_substring_mask & ~seen_mask) != 0:
                    has_new_char = True
            
            # If the current substring is beautiful, we can attempt to partition here
            if has_new_char:
                # Recurse for the rest of the string with updated seen_mask
                res = backtrack(end_index + 1, seen_mask | current_substring_mask)
                if res != float('inf'):
                    min_partitions = min(min_partitions, 1 + res)

        memo[state] = min_partitions
        return min_partitions

    result = backtrack(0, 0)
    return result if result <= n else -1
