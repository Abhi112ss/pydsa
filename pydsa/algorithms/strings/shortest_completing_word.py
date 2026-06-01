METADATA = {
    "id": 748,
    "name": "Shortest Completing Word",
    "slug": "shortest_completing_word",
    "category": "String",
    "aliases": [],
    "tags": ["hash_table", "string_counting"],
    "difficulty": "easy",
    "time_complexity": "O(N * L)",
    "space_complexity": "O(1)",
    "description": "Find the shortest word that contains all letters from a license plate with required frequencies.",
}


def solve(license_plate: str, words: list[str]) -> str:
    """Return the shortest completing word for a given license plate.

    Args:
        license_plate: A string containing letters, digits and spaces.
        words: A list of candidate words consisting of lowercase English letters.

    Returns:
        The shortest word from *words* that contains each alphabetic character
        in *license_plate* (case‑insensitive) at least as many times as it appears
        in the plate. If multiple words qualify, the first one of minimal length
        is returned.

    Examples:
        >>> solve("1s3 PSt", ["step","steps","stripe","stepple"])
        'steps'
        >>> solve("GrC8950", ["measure","other","every","base","according","meeting"])
        'according'
    """
    # Build frequency array for the letters required by the license plate.
    required_counts = [0] * 26
    for ch in license_plate.lower():
        if 'a' <= ch <= 'z':
            required_counts[ord(ch) - ord('a')] += 1

    shortest_word = None
    shortest_length = float('inf')

    for word in words:
        # Quick length check to skip obviously longer candidates.
        if len(word) > shortest_length:
            continue

        # Count letters in the current word.
        word_counts = [0] * 26
        for ch in word:
            word_counts[ord(ch) - ord('a')] += 1

        # Verify that the word satisfies all required counts.
        satisfies = True
        for idx in range(26):
            if required_counts[idx] > word_counts[idx]:
                satisfies = False
                break

        if satisfies and len(word) < shortest_length:
            shortest_word = word
            shortest_length = len(word)

    return shortest_word if shortest_word is not None else ""