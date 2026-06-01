METADATA = {
    "id": 1297,
    "name": "Maximum Number of Occurrences of a Substring",
    "slug": "maximum-number-of-occurrences-of-a-substring",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of occurrences of any substring with length at least min_len.",
}

def solve(s: str, min_len: int) -> int:
    """
    Finds the maximum number of occurrences of any substring with length at least min_len.

    The key insight is that if a substring of length > min_len occurs K times, 
    its prefix of length min_len must also occur at least K times. 
    Therefore, we only need to count occurrences of all substrings of length exactly min_len.

    Args:
        s: The input string.
        min_len: The minimum length of the substring.

    Returns:
        The maximum number of occurrences of any substring of length >= min_len.

    Examples:
        >>> solve("aaaaa", 2)
        4
        >>> solve("abacaba", 3)
        2
        >>> solve("abcde", 1)
        1
    """
    n = len(s)
    if n < min_len:
        return 0

    # Dictionary to store the frequency of each substring of length min_len
    substring_counts: dict[str, int] = {}
    max_occurrences = 0

    # Iterate through the string using a sliding window of fixed size min_len
    for i in range(n - min_len + 1):
        # Extract the substring of length min_len
        current_substring = s[i : i + min_len]
        
        # Update the count in the hash map
        substring_counts[current_substring] = substring_counts.get(current_substring, 0) + 1
        
        # Track the maximum frequency encountered so far
        if substring_counts[current_substring] > max_occurrences:
            max_occurrences = substring_counts[current_substring]

    return max_occurrences
