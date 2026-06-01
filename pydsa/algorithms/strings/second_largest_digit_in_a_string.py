METADATA = {
    "id": 1796,
    "name": "Second Largest Digit in a String",
    "slug": "second_largest_digit_in_a_string",
    "category": "string",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the second largest digit that appears in the given string, or -1 if it does not exist.",
}


def solve(s: str) -> int:
    """Return the second largest digit found in the input string.

    Args:
        s: A string that may contain digits and other characters.

    Returns:
        The second largest distinct digit (0‑9) present in *s*.
        If fewer than two distinct digits exist, returns -1.

    Examples:
        >>> solve("dfa12321")
        2
        >>> solve("abc111")
        -1
        >>> solve("ab111c")
        -1
        >>> solve("ab12c3d4")
        3
    """
    # Track the largest and second largest distinct digits seen so far.
    max_digit = -1
    second_max_digit = -1

    for character in s:
        if character.isdigit():
            digit = ord(character) - ord('0')  # convert char to int without int()
            if digit > max_digit:
                # Current digit becomes the new maximum; previous max becomes second max.
                second_max_digit = max_digit
                max_digit = digit
            elif max_digit > digit > second_max_digit:
                # Digit is between max and second max, update second max.
                second_max_digit = digit

    return second_max_digit if second_max_digit != -1 else -1