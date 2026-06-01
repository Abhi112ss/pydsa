METADATA = {
    "id": 1941,
    "name": "Check if All Characters Have Equal Number of Occurrences",
    "slug": "check_if_all_characters_have_equal_number_of_occurrences",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "frequency_count"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine whether each distinct character in a string appears the same number of times."
}


def solve(s: str) -> bool:
    """Check if all characters have equal number of occurrences.

    Args:
        s: Input string consisting of lowercase English letters.

    Returns:
        True if every distinct character occurs the same number of times,
        otherwise False.

    Examples:
        >>> solve("abacbc")
        True
        >>> solve("zzzzzz")
        True
        >>> solve("abacb")
        False
    """
    # Build a frequency map for each character.
    frequency: dict[str, int] = {}
    for character in s:
        frequency[character] = frequency.get(character, 0) + 1

    # All occurrence counts must be identical; a set size of 0 or 1 satisfies this.
    unique_counts = set(frequency.values())
    return len(unique_counts) <= 1