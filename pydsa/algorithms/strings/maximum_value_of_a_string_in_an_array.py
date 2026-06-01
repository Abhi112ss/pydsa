METADATA = {
    "id": 2496,
    "name": "Maximum Value of a String in an Array",
    "slug": "maximum_value_of_a_string_in_an_array",
    "category": "algorithms",
    "aliases": [],
    "tags": ["strings", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Return the maximum value of strings where value is sum of digits or length if no digits.",
}


def solve(strings: list[str]) -> int:
    """Compute the maximum value among a list of strings.

    The value of a string is defined as:
      * the sum of all digit characters it contains, if any digit exists;
      * otherwise, the number of alphabetic characters (i.e., its length).

    Args:
        strings: A list of non‑empty strings consisting of lowercase letters and digits.

    Returns:
        The highest value found among the input strings.

    Examples:
        >>> solve(["a1b2c3", "abc", "123"])
        6
        >>> solve(["abcd", "1234", "a1b2"])
        4
    """
    maximum_value = 0

    for string_item in strings:
        digit_sum = 0
        # Accumulate sum of digit characters
        for character in string_item:
            if character.isdigit():
                digit_sum += int(character)

        # Determine the value based on presence of digits
        if digit_sum > 0:
            current_value = digit_sum
        else:
            current_value = len(string_item)

        # Update the running maximum
        if current_value > maximum_value:
            maximum_value = current_value

    return maximum_value