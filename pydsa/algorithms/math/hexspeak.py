METADATA = {
    "id": 1271,
    "name": "Hexspeak",
    "slug": "hexspeak",
    "category": "string",
    "aliases": [],
    "tags": ["string_manipulation", "base_conversion"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Convert an integer to Hexspeak by mapping hexadecimal digits to allowed letters.",
}


def convert_to_hexspeak(number: int) -> str:
    """Convert an integer to its Hexspeak representation.

    The hexadecimal representation is taken in uppercase, then each
    occurrence of '1' is replaced by 'I' and each '0' by 'O'.  If any
    remaining character is not one of A, B, C, D, E, F, I, O, the function
    returns \"ERROR\".

    Args:
        number: A non‑negative integer.

    Returns:
        The Hexspeak string or \"ERROR\" if the conversion is invalid.

    Examples:
        >>> convert_to_hexspeak(257)
        'IOI'
        >>> convert_to_hexspeak(123)
        'ERROR'
    """
    # Convert to hexadecimal without the '0x' prefix and in uppercase.
    hex_string = hex(number)[2:].upper()

    allowed_characters = {"A", "B", "C", "D", "E", "F", "I", "O"}

    # Build the result while validating each character.
    result_chars = []
    for char in hex_string:
        if char == "1":
            transformed = "I"
        elif char == "0":
            transformed = "O"
        else:
            transformed = char

        if transformed not in allowed_characters:
            return "ERROR"
        result_chars.append(transformed)

    return "".join(result_chars)


def solve() -> None:
    """Read an integer from standard input, convert it to Hexspeak, and print the result.

    Input format:
        A single line containing a non‑negative integer.

    Output format:
        The Hexspeak string or \"ERROR\".

    Example:
        Input: 257
        Output: IOI
    """
    import sys

    data = sys.stdin.read().strip()
    if not data:
        return
    number = int(data)
    hexspeak = convert_to_hexspeak(number)
    sys.stdout.write(hexspeak)