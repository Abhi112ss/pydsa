METADATA = {
    "id": 567,
    "name": "Permutation in String",
    "slug": "permutation-in-string",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "sliding_window", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.",
}

def solve(s1: str, s2: str) -> bool:
    """
    Determines if s2 contains a permutation of s1 using a sliding window approach.

    Args:
        s1: The pattern string to look for permutations of.
        s2: The target string to search within.

    Returns:
        True if a permutation of s1 exists as a substring in s2, False otherwise.

    Examples:
        >>> solve("ab", "eidbaooo")
        True
        >>> solve("ab", "eidboaoo")
        False
    """
    n1, n2 = len(s1), len(s2)
    
    if n1 > n2:
        return False

    # Since we only deal with lowercase English letters, 
    # an array of size 26 acts as an efficient hash map.
    s1_counts = [0] * 26
    window_counts = [0] * 26

    # Initialize the frequency counts for s1 and the first window of s2
    for i in range(n1):
        s1_counts[ord(s1[i]) - ord('a')] += 1
        window_counts[ord(s2[i]) - ord('a')] += 1

    # If the initial window is a match
    if s1_counts == window_counts:
        return True

    # Slide the window across s2
    for i in range(n1, n2):
        # Add the new character entering the window
        window_counts[ord(s2[i]) - ord('a')] += 1
        # Remove the character that is sliding out of the window
        window_counts[ord(s2[i - n1]) - ord('a')] -= 1

        # Compare the current window frequency with s1 frequency
        # Array comparison in Python is O(26), which is O(1)
        if s1_counts == window_counts:
            return True

    return False
