METADATA = {
    "id": 383,
    "name": "Ransom Note",
    "slug": "ransom_note",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Determine if a ransom note can be constructed from a magazine.",
}


def solve(ransom_note: str, magazine: str) -> bool:
    """Determine whether the `ransom_note` can be formed using characters from `magazine`.

    Args:
        ransom_note: The target string that needs to be constructed.
        magazine: The source string containing available characters.

    Returns:
        True if `ransom_note` can be built from `magazine`; otherwise False.

    Examples:
        >>> solve("a", "b")
        False
        >>> solve("aa", "aab")
        True
        >>> solve("abc", "defabc")
        True
    """
    # Frequency array for 26 lowercase English letters (constant space)
    letter_counts: list[int] = [0] * 26

    # Count characters in the magazine
    for char in magazine:
        index = ord(char) - ord('a')
        if 0 <= index < 26:
            letter_counts[index] += 1

    # Verify each character needed by the ransom note
    for char in ransom_note:
        index = ord(char) - ord('a')
        if 0 <= index < 26:
            if letter_counts[index] == 0:
                return False
            letter_counts[index] -= 1
        else:
            # Non‑lowercase characters cannot be satisfied
            return False

    return True