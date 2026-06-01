METADATA = {
    "id": 2083,
    "name": "Substrings That Begin and End With the Same Letter",
    "slug": "substrings-that-begin-and-end-with-the-same-letter",
    "category": "String",
    "aliases": [],
    "tags": ["string", "math", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that start and end with the same character.",
}

def solve(s: str) -> int:
    """
    Calculates the number of substrings that begin and end with the same letter.

    The logic relies on the fact that if a character appears 'k' times in a string,
    the number of substrings that can be formed using only those occurrences 
    as start and end points is the sum of the first k integers: k * (k + 1) / 2.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The total count of substrings that start and end with the same letter.

    Examples:
        >>> solve("abcba")
        7
        # Substrings: "a", "b", "c", "b", "a", "bcb", "abcba"
        >>> solve("zz")
        3
        # Substrings: "z", "z", "zz"
    """
    # Frequency map for lowercase English letters (a-z)
    # Since the alphabet size is constant (26), space complexity is O(1)
    char_counts: dict[str, int] = {}

    # Count occurrences of each character in O(n) time
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    total_substrings: int = 0

    # For each character that appears 'k' times, it contributes k*(k+1)/2 substrings
    # This is because any pair of the same character (including the character with itself)
    # forms a valid substring.
    for count in char_counts.values():
        # Using the arithmetic series formula: sum = n * (n + 1) / 2
        total_substrings += (count * (count + 1)) // 2

    return total_substrings
