METADATA = {
    "id": 1592,
    "name": "Rearrange Spaces Between Words",
    "slug": "rearrange_spaces_between_words",
    "category": "String",
    "aliases": [],
    "tags": ["string", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Rearrange spaces so that they are evenly distributed between words, with extra spaces at the end.",
}


def solve(text: str) -> str:
    """Rearrange spaces between words so that they are evenly distributed.

    Args:
        text: The original string containing words and spaces.

    Returns:
        A new string where spaces are evenly distributed between words; any
        leftover spaces are placed at the end.

    Examples:
        >>> solve("  this   is a sentence ")
        'this   is   a   sentence'
        >>> solve(" practice   makes   perfect")
        'practice makes perfect  '
    """
    # Count total spaces in the original string.
    total_spaces: int = text.count(' ')
    # Extract words ignoring any number of spaces.
    words: list[str] = text.split()
    number_of_words: int = len(words)

    # If there is only one word, all spaces go to the end.
    if number_of_words == 1:
        return words[0] + ' ' * total_spaces

    # Compute equal spaces between each adjacent pair of words.
    spaces_per_gap: int = total_spaces // (number_of_words - 1)
    # Remaining spaces that cannot be evenly distributed.
    extra_spaces: int = total_spaces % (number_of_words - 1)

    # Join words with the calculated equal spaces.
    evenly_spaced: str = (' ' * spaces_per_gap).join(words)
    # Append any leftover spaces at the end.
    result: str = evenly_spaced + (' ' * extra_spaces)
    return result