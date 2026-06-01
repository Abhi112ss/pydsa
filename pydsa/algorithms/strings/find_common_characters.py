METADATA = {
    "id": 1002,
    "name": "Find Common Characters",
    "slug": "find_common_characters",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Return characters that appear in all strings of the array.",
}

def solve(strings: list[str]) -> list[str]:
    """Find common characters across all strings.

    Args:
        strings: List of lowercase alphabetic strings.

    Returns:
        List of characters that appear in every string, including duplicates.
        The order of characters follows alphabetical order.

    Examples:
        >>> solve(["bella", "label", "roller"])
        ['e', 'l', 'l']
        >>> solve(["cool", "lock", "cook"])
        ['c', 'o']
    """
    if not strings:
        return []

    # Minimum frequency of each letter across all strings; start with infinity.
    min_counts: list[int] = [float('inf')] * 26

    for word in strings:
        # Frequency of each letter in the current word.
        current_counts: list[int] = [0] * 26
        for ch in word:
            index = ord(ch) - ord('a')
            current_counts[index] += 1

        # Update the global minimum frequencies.
        for i in range(26):
            if current_counts[i] < min_counts[i]:
                min_counts[i] = current_counts[i]

    # Build the result based on the minimum frequencies.
    result: list[str] = []
    for i, count in enumerate(min_counts):
        result.extend([chr(ord('a') + i)] * count)

    return result