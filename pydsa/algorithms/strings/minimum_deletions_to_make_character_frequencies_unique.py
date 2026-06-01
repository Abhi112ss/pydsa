METADATA = {
    "id": 1647,
    "name": "Minimum Deletions to Make Character Frequencies Unique",
    "slug": "minimum_deletions_to_make_character_frequencies_unique",
    "category": "greedy",
    "aliases": [],
    "tags": ["hash_map", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of deletions required so that each character's frequency in a string becomes unique.",
}


def solve(s: str) -> int:
    """Return the minimum number of deletions needed to make all character frequencies unique.

    Args:
        s: Input string consisting of lowercase English letters.

    Returns:
        The minimal count of deletions required.

    Examples:
        >>> solve("aab")
        0
        >>> solve("aaabbbcc")
        2
        >>> solve("ceabaacb")
        2
    """
    # Count frequencies of each character.
    frequency_map: dict[str, int] = {}
    for character in s:
        frequency_map[character] = frequency_map.get(character, 0) + 1

    used_frequencies: set[int] = set()
    deletions_needed = 0

    # Process each frequency, reducing it until it becomes unique or zero.
    for original_freq in frequency_map.values():
        current_freq = original_freq
        while current_freq > 0 and current_freq in used_frequencies:
            current_freq -= 1
            deletions_needed += 1
        used_frequencies.add(current_freq)

    return deletions_needed