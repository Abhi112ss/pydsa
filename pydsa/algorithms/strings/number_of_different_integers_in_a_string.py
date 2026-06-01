METADATA = {
    "id": 1805,
    "name": "Number of Different Integers in a String",
    "slug": "number_of_different_integers_in_a_string",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count distinct integer values appearing in a mixed alphanumeric string, ignoring leading zeros.",
}


def solve(s: str) -> int:
    """Count the number of different integers in the given string.

    Args:
        s: A string consisting of lowercase letters and digits.

    Returns:
        The count of unique integer values that appear in `s`. Leading zeros are ignored,
        so "001" and "1" are considered the same integer.

    Examples:
        >>> solve("a123bc34d8ef34")
        3
        >>> solve("leet1234code234"
        2)
        >>> solve("a0b0c")
        1
    """
    unique_numbers: set[str] = set()
    current_digits: list[str] = []

    for character in s:
        if character.isdigit():
            # Build the current numeric token.
            current_digits.append(character)
        else:
            if current_digits:
                # Normalize by stripping leading zeros; keep a single zero if all are zeros.
                numeric_string = "".join(current_digits).lstrip('0') or "0"
                unique_numbers.add(numeric_string)
                current_digits.clear()

    # Process a trailing numeric token, if any.
    if current_digits:
        numeric_string = "".join(current_digits).lstrip('0') or "0"
        unique_numbers.add(numeric_string)

    return len(unique_numbers)