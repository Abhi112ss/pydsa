METADATA = {
    "id": 1417,
    "name": "Reformat The String",
    "slug": "reformat_the_string",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Rearrange a string so that letters and digits alternate, or return empty if impossible.",
}


def solve(s: str) -> str:
    """Reformat a string so that letters and digits alternate.

    Args:
        s: Input string consisting of alphanumeric characters.

    Returns:
        A reformatted string where letters and digits alternate.
        If such an arrangement is impossible, returns an empty string.

    Examples:
        >>> solve("a0b1c2")
        'a0b1c2'
        >>> solve("leetcode")
        ''
        >>> solve("1229857369")
        ''
        >>> solve("covid2019")
        'c2o0v1i9d'
    """
    # Separate letters and digits
    letters: list[str] = []
    digits: list[str] = []
    for ch in s:
        if ch.isalpha():
            letters.append(ch)
        else:
            digits.append(ch)

    # If the counts differ by more than one, alternating is impossible
    if abs(len(letters) - len(digits)) > 1:
        return ""

    # Determine which group should start the result
    start_with_letter: bool = len(letters) >= len(digits)

    result_chars: list[str] = []
    # Build the alternating string by popping from the appropriate list
    while letters or digits:
        if start_with_letter:
            if letters:
                result_chars.append(letters.pop())
            if digits:
                result_chars.append(digits.pop())
        else:
            if digits:
                result_chars.append(digits.pop())
            if letters:
                result_chars.append(letters.pop())
        # After the first pair, always alternate the starting type
        start_with_letter = not start_with_letter

    return "".join(result_chars)