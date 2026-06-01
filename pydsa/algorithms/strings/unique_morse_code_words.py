METADATA = {
    "id": 804,
    "name": "Unique Morse Code Words",
    "slug": "unique_morse_code_words",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_set", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(S)",
    "space_complexity": "O(S)",
    "description": "Count the number of unique Morse code representations among a list of words.",
}

MORSE_TABLE = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
    "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
    "..-", "...-", ".--", "-..-", "-.--", "--..",
]


def solve(words: list[str]) -> int:
    """Return the number of unique Morse code representations among the given words.

    Each letter is mapped to its Morse code equivalent using the standard
    International Morse Code table.  A word's representation is the
    concatenation of the Morse codes of its letters.  The answer is the
    number of distinct representations across all words.

    Args:
        words: A list of lowercase English words.

    Returns:
        The count of unique Morse code representations.

    Examples:
        >>> solve(["gin", "zen", "gig", "msg"])
        2
        >>> solve(["a"])
        1
        >>> solve(["abc", "bca"])
        2
    """
    unique_representations: set[str] = set()

    for word in words:
        # Build the Morse string for the current word by looking up each letter.
        morse_chars = [MORSE_TABLE[ord(letter) - ord("a")] for letter in word]
        morse_string = "".join(morse_chars)

        # Add the full Morse string to the set; duplicates are automatically ignored.
        unique_representations.add(morse_string)

    # The size of the set equals the number of unique representations.
    return len(unique_representations)