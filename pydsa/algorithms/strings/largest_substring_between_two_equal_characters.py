METADATA = {
    "id": 1624,
    "name": "Largest Substring Between Two Equal Characters",
    "slug": "largest_substring_between_two_equal_characters",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that is bounded by two equal characters.",
}


def solve(s: str) -> int:
    """Return the length of the longest substring that is bounded by two equal characters.

    Args:
        s: A non‑empty string consisting of lowercase English letters.

    Returns:
        The maximum length of a substring that starts and ends with the same character.
        If no such substring exists, returns -1.

    Examples:
        >>> solve("aa")
        0
        >>> solve("abca")
        2
        >>> solve("cbzxy")
        -1
    """
    # Store the first index where each character appears; -1 indicates not seen yet.
    first_occurrence: list[int] = [-1] * 26
    max_length: int = -1

    for current_index, character in enumerate(s):
        char_code: int = ord(character) - ord('a')
        if first_occurrence[char_code] == -1:
            # Record the first occurrence of this character.
            first_occurrence[char_code] = current_index
        else:
            # Compute the distance between the current and first occurrence (exclusive).
            candidate_length: int = current_index - first_occurrence[char_code] - 1
            if candidate_length > max_length:
                max_length = candidate_length

    return max_length