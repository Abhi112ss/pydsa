METADATA = {
    "id": 434,
    "name": "Number of Segments in a String",
    "slug": "number_of_segments_in_a_string",
    "category": "String",
    "aliases": ["Number of Segments in a String"],
    "tags": ["string", "two pointers", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the number of words (segments) in a given string.",
}


def solve(s: str) -> int:
    """Count the number of segments (words) in a string.

    Args:
        s: Input string that may contain spaces and words.

    Returns:
        The count of non‑empty words separated by spaces.

    Examples:
        >>> solve("Hello, World")
        2
        >>> solve("   fly me   to   the moon  ")
        4
        >>> solve("")
        0
    """
    # Flag indicating whether the previous character was a space (or start of string)
    previous_was_space: bool = True
    segment_count: int = 0

    for character in s:
        if character != " " and previous_was_space:
            # Start of a new word detected
            segment_count += 1
            previous_was_space = False
        elif character == " ":
            # Update flag when encountering a space
            previous_was_space = True

    return segment_count