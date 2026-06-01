METADATA = {
    "id": 1309,
    "name": "Decrypt String from Alphabet to Integer Mapping",
    "slug": "decrypt_string_from_alphabet_to_integer_mapping",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "parsing"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert an encoded string with optional '#' markers into its alphabetical representation.",
}


def solve(s: str) -> str:
    """Decrypt a string encoded with alphabet-to-integer mapping.

    The encoding follows these rules:
    - Characters '1' to '9' map to 'a' to 'i'.
    - Substrings of the form '10#' to '26#' map to 'j' to 'z'.

    Args:
        s: The encoded string consisting of digits and optional '#' characters.

    Returns:
        The decoded alphabetical string.

    Examples:
        >>> solve("10#11#12")
        'jkab'
        >>> solve("1326#")
        'acz'
        >>> solve("25#")
        'y'
    """
    # Result list will be built in reverse order for efficient appends.
    decoded_characters: list[str] = []
    index: int = len(s) - 1

    while index >= 0:
        if s[index] == '#':
            # Extract the two-digit number preceding the '#'.
            two_digit_number: int = int(s[index - 2 : index])
            decoded_characters.append(chr(ord('a') + two_digit_number - 1))
            index -= 3  # Skip the processed digits and '#'.
        else:
            # Single-digit number maps directly.
            single_digit_number: int = int(s[index])
            decoded_characters.append(chr(ord('a') + single_digit_number - 1))
            index -= 1

    # The characters were collected backwards; reverse to obtain correct order.
    return ''.join(reversed(decoded_characters))