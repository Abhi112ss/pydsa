METADATA = {
    "id": 500,
    "name": "Keyboard Row",
    "slug": "keyboard_row",
    "category": "String",
    "aliases": [],
    "tags": ["hash_set", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n*k)",
    "space_complexity": "O(1)",
    "description": "Return the words that can be typed using letters of the same keyboard row.",
}

def solve(words: list[str]) -> list[str]:
    """Return words that can be typed using letters of a single keyboard row.

    Args:
        words: A list of lowercase or uppercase strings to evaluate.

    Returns:
        A list containing only the words that can be typed using letters from
        one of the three rows on a standard QWERTY keyboard.

    Examples:
        >>> solve(["Hello","Alaska","Dad","Peace"])
        ['Alaska', 'Dad']
        >>> solve(["omg","LOL","type"])
        ['omg', 'LOL']
    """
    # Define sets for each keyboard row (case-insensitive)
    top_row = set("qwertyuiop")
    middle_row = set("asdfghjkl")
    bottom_row = set("zxcvbnm")

    result_words: list[str] = []
    for word in words:
        # Determine the row of the first character (lowercased)
        first_char_row = (
            top_row if word[0].lower() in top_row
            else middle_row if word[0].lower() in middle_row
            else bottom_row
        )
        # Check that every character belongs to the same row
        if all((char.lower() in first_char_row) for char in word):
            result_words.append(word)

    return result_words