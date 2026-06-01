METADATA = {
    "id": 1408,
    "name": "String Matching in an Array",
    "slug": "string_matching_in_an_array",
    "category": "array",
    "aliases": [],
    "tags": ["strings", "trie"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Return all strings that are substrings of another string in the given array.",
}


def solve(words: list[str]) -> list[str]:
    """Return strings that appear as substrings of another string in the array.

    Args:
        words: List of distinct strings.

    Returns:
        A list containing each string that is a substring of at least one other
        string in ``words``. The order of the returned strings follows the
        original order in ``words``.

    Examples:
        >>> solve(["mass","as","hero","superhero"])
        ['as', 'hero']
        >>> solve(["leetcode","et","code"])
        ['et', 'code']
    """
    # Sort strings by length descending to ensure longer strings are checked first.
    sorted_by_length = sorted(words, key=len, reverse=True)

    # Use a set for O(1) look‑ups of strings that have already been identified as substrings.
    substrings_set: set[str] = set()

    # For each string, check if it appears in any longer string.
    for index, longer in enumerate(sorted_by_length):
        # Compare with all previously processed (longer) strings.
        for shorter in sorted_by_length[index + 1 :]:
            if shorter in longer:
                substrings_set.add(shorter)

    # Preserve original order while filtering.
    return [word for word in words if word in substrings_set]