METADATA = {
    "id": 1525,
    "name": "Number of Good Ways to Split a String",
    "slug": "number-of-good-ways-to-split-a-string",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Count the number of ways to split a string into two non-empty parts such that the set of characters in both parts is the same.",
}

def solve(s: str) -> int:
    """
    Calculates the number of ways to split a string into two non-empty parts
    where both parts contain the exact same set of unique characters.

    Args:
        s: The input string to split.

    Returns:
        The total number of 'good' split positions.

    Examples:
        >>> solve("aacaba")
        2
        >>> solve("abacaba")
        1
        >>> solve("abcdef")
        0
    """
    n = len(s)
    if n < 2:
        return 0

    # suffix_counts stores the frequency of characters from index i to n-1
    suffix_counts: dict[str, int] = {}
    for char in s:
        suffix_counts[char] = suffix_counts.get(char, 0) + 1

    # prefix_counts stores the frequency of characters from index 0 to i
    prefix_counts: dict[str, int] = {}
    good_ways = 0

    # Iterate through the string, treating each index as a potential split point.
    # A split at index i means the left part is s[0...i] and right part is s[i+1...n-1].
    # We stop at n-2 because the right part must be non-empty.
    for i in range(n - 1):
        char = s[i]
        
        # Update prefix counts by adding the current character
        prefix_counts[char] = prefix_counts.get(char, 0) + 1
        
        # Update suffix counts by removing the current character
        suffix_counts[char] -= 1
        if suffix_counts[char] == 0:
            del suffix_counts[char]

        # A split is 'good' if the set of unique characters (keys in dicts) is identical
        # Comparing dictionary keys in Python is O(k) where k is the alphabet size (max 26)
        if len(prefix_counts) == len(suffix_counts):
            # Check if all characters in prefix are also in suffix
            # Since lengths are equal, if all prefix keys are in suffix, they are identical sets
            if all(c in suffix_counts for c in prefix_counts):
                good_ways += 1

    return good_ways
