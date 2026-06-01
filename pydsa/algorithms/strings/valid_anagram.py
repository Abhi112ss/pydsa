METADATA = {
    "id": 242,
    "name": "Valid Anagram",
    "slug": "valid_anagram",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "sorting", "frequency_counter"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if two strings are anagrams of each other.",
}


def solve(s: str, t: str) -> bool:
    """Check whether two strings are anagrams.

    Args:
        s: The first input string.
        t: The second input string.

    Returns:
        True if `t` is an anagram of `s`; otherwise False.

    Examples:
        >>> solve("anagram", "nagaram")
        True
        >>> solve("rat", "car")
        False
    """
    # Anagrams must have the same length; early exit otherwise.
    if len(s) != len(t):
        return False

    # Assuming only lowercase English letters, a fixed-size array of 26 counters
    # gives O(1) extra space.
    char_counts: list[int] = [0] * 26

    for char_s, char_t in zip(s, t):
        index_s = ord(char_s) - ord('a')
        index_t = ord(char_t) - ord('a')
        # If characters fall outside 'a'‑'z', fall back to a dictionary method.
        if not (0 <= index_s < 26) or not (0 <= index_t < 26):
            # Use a hash map for the general case.
            from collections import Counter

            return Counter(s) == Counter(t)
        char_counts[index_s] += 1
        char_counts[index_t] -= 1

    # All counters must be zero for the strings to be anagrams.
    return all(count == 0 for count in char_counts)