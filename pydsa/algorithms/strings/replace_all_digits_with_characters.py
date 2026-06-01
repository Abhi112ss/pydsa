METADATA = {
    "id": 1844,
    "name": "Replace All Digits with Characters",
    "slug": "replace_all_digits_with_characters",
    "category": "string",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Replace each digit in the string with a character offset from the preceding letter.",
}


def solve(s: str) -> str:
    """Replace all digits in the input string according to the problem rule.

    Args:
        s: A non‑empty string consisting of lowercase English letters and digits.
           Every digit is guaranteed to follow a letter.

    Returns:
        A new string where each digit `d` is replaced by the character that is
        `d` positions after the preceding letter in the alphabet.

    Examples:
        >>> solve("a1c1e1")
        'abcdef'
        >>> solve("a1b2c3d4e")
        'abbcdddeef'
    """
    result_chars: list[str] = []
    previous_letter: str = ""

    for current_char in s:
        if current_char.isalpha():
            # Store the current letter and copy it to the result.
            previous_letter = current_char
            result_chars.append(current_char)
        else:
            # current_char is a digit; compute the new character based on the
            # previously seen letter and append it.
            offset: int = int(current_char)
            new_char: str = chr(ord(previous_letter) + offset)
            result_chars.append(new_char)

    return "".join(result_chars)