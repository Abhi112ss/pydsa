METADATA = {
    "id": 2955,
    "name": "Number of Same-End Substrings",
    "slug": "number-of-same-end-substrings",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings where the first and last characters are the same.",
}

def solve(s: str) -> int:
    """
    Calculates the total number of substrings that start and end with the same character.

    The problem can be solved by counting the occurrences of each character. 
    If a character appears 'k' times, the number of substrings that start and 
    end with that character is the number of ways to choose 2 positions out of k 
    (for substrings of length > 1) plus the k substrings of length 1.
    This simplifies to the sum of integers from 1 to k, which is k * (k + 1) // 2.

    Args:
        s: The input string.

    Returns:
        The total count of substrings where the first and last characters are identical.

    Examples:
        >>> solve("ababa")
        9
        # Substrings: "a", "b", "a", "b", "a", "aba", "bab", "aba", "ababa"
        >>> solve("abc")
        3
        # Substrings: "a", "b", "c"
    """
    # Dictionary to store the frequency of each character
    # Since the input consists of lowercase English letters, space is O(1)
    char_counts: dict[str, int] = {}

    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    total_substrings: int = 0

    # For each character that appears 'k' times, it contributes 
    # k * (k + 1) // 2 substrings to the total count.
    # This accounts for all single-character substrings and all 
    # multi-character substrings starting and ending with that char.
    for count in char_counts.values():
        total_substrings += (count * (count + 1)) // 2

    return total_substrings
