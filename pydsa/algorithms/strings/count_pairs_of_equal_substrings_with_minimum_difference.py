METADATA = {
    "id": 1794,
    "name": "Count Pairs of Equal Substrings With Minimum Difference",
    "slug": "count-pairs-of-equal-substrings-with-minimum-difference",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of pairs of equal substrings that appear in a given string.",
}

def solve(s: str) -> int:
    """
    Counts the number of pairs of equal substrings in the given string.
    
    A pair of equal substrings is defined by their starting indices and lengths.
    If a substring appears 'k' times, the number of pairs is k * (k - 1) // 2.

    Args:
        s: The input string.

    Returns:
        The total number of pairs of equal substrings.

    Examples:
        >>> solve("abc")
        0
        >>> solve("aaaa")
        6
    """
    n = len(s)
    substring_counts: dict[str, int] = {}

    # Iterate through all possible starting positions
    for start in range(n):
        # Iterate through all possible ending positions to extract substrings
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            # Increment the frequency of the current substring in the hash map
            substring_counts[substring] = substring_counts.get(substring, 0) + 1

    total_pairs = 0
    # For every unique substring found, calculate the number of ways to choose 2
    # from its total occurrences using the combination formula: nC2 = n * (n - 1) / 2
    for count in substring_counts.values():
        if count > 1:
            total_pairs += (count * (count - 1)) // 2

    return total_pairs
