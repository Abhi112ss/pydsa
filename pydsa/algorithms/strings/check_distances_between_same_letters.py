METADATA = {
    "id": 2399,
    "name": "Check Distances Between Same Letters",
    "slug": "check_distances_between_same_letters",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Verify that each letter appears exactly twice and the distance between its occurrences matches the given array.",
}


def solve(s: str, distance: list[int]) -> bool:
    """Check whether each letter in the string appears exactly twice and the gap between
    its two occurrences equals the expected distance.

    Args:
        s: A string consisting of lowercase English letters.
        distance: A list of 26 non‑negative integers where distance[i] corresponds to the
            expected number of characters between the two occurrences of the letter
            chr(i + ord('a')).

    Returns:
        True if all letters that appear in `s` satisfy the distance condition and appear
        exactly twice; otherwise False.

    Examples:
        >>> solve("abaccb", [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        True
        >>> solve("aa", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        True
        >>> solve("aba", [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        False
    """
    # Initialize arrays for first occurrence index and occurrence count for each letter.
    first_index = [-1] * 26
    occurrence_count = [0] * 26

    for current_position, character in enumerate(s):
        letter_index = ord(character) - ord('a')
        occurrence_count[letter_index] += 1

        # If a letter appears more than twice, the condition fails.
        if occurrence_count[letter_index] > 2:
            return False

        if first_index[letter_index] == -1:
            # Record the first position of this letter.
            first_index[letter_index] = current_position
        else:
            # Compute the gap between the two occurrences (excluding the letters themselves).
            gap = current_position - first_index[letter_index] - 1
            if gap != distance[letter_index]:
                return False

    # Ensure every letter that appears does so exactly twice.
    for count in occurrence_count:
        if count not in (0, 2):
            return False

    return True