METADATA = {
    "id": 806,
    "name": "Number of Lines To Write String",
    "slug": "number_of_lines_to_write_string",
    "category": "string",
    "aliases": [],
    "tags": ["simulation", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate how many lines and the width of the last line needed to write a string given character widths and a 100‑unit line limit.",
}


def solve(widths: list[int], s: str) -> list[int]:
    """Calculate the number of lines and the width of the last line required to write a string.

    Args:
        widths: A list of 26 integers where widths[i] is the width of the i‑th lowercase
                English letter ('a' -> widths[0], ..., 'z' -> widths[25]).
        s: The string consisting only of lowercase English letters.

    Returns:
        A list of two integers [total_lines, last_line_width] where total_lines is the
        number of lines needed and last_line_width is the width occupied on the last line.

    Examples:
        >>> solve([10]*26, "abcdefghijklmnopqrstuvwxyz")
        [3, 60]
        >>> solve([4,2,1,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26], "bbbcccdddaaa")
        [2, 23]
    """
    total_lines = 1  # start with the first line
    current_width = 0

    for character in s:
        char_width = widths[ord(character) - ord('a')]  # width of the current character
        # If adding this character exceeds the 100‑unit limit, start a new line
        if current_width + char_width > 100:
            total_lines += 1
            current_width = char_width
        else:
            current_width += char_width

    return [total_lines, current_width]