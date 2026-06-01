METADATA = {
    "id": 3517,
    "name": "Smallest Palindromic Rearrangement I",
    "slug": "smallest_palindromic_rearrangement_i",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Construct the lexicographically smallest palindrome possible from a given string, or return an empty string if no palindrome can be formed.",
}

def solve(s: str) -> str:
    """
    Constructs the lexicographically smallest palindrome using the characters of the input string.

    Args:
        s: The input string containing characters to be rearranged.

    Returns:
        The lexicographically smallest palindromic rearrangement of s, 
        or an empty string if no palindrome can be formed.

    Examples:
        >>> solve("aabbc")
        'abcba'
        >>> solve("aabbcc")
        'abccba'
        >>> solve("abc")
        ''
    """
    # Count the frequency of each character
    char_counts: dict[str, int] = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # A palindrome can have at most one character with an odd frequency
    odd_chars: list[str] = []
    for char, count in char_counts.items():
        if count % 2 != 0:
            odd_chars.append(char)

    if len(odd_chars) > 1:
        return ""

    # To get the lexicographically smallest palindrome, 
    # we sort the characters and build the first half greedily.
    sorted_chars: list[str] = sorted(char_counts.keys())
    
    first_half: list[str] = []
    middle_char: str = ""

    if odd_chars:
        middle_char = odd_chars[0]

    for char in sorted_chars:
        # Use half of the occurrences for the first half of the palindrome
        count = char_counts[char]
        # If it's the odd character, we use (count - 1) // 2 for the half
        # If it's an even character, we use count // 2
        num_to_add = count // 2
        first_half.extend([char] * num_to_add)

    # The full palindrome is: first_half + middle_char + reversed(first_half)
    # Since first_half is built from sorted keys, it is already lexicographically minimal
    result_half = "".join(first_half)
    return result_half + middle_char + result_half[::-1]
