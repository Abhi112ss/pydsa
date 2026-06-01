METADATA = {
    "id": 3706,
    "name": "Maximum Distance Between Unequal Words in Array II",
    "slug": "maximum_distance_between_unequal_words_in_array_ii",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the largest index distance between two different words in the array.",
}


def solve(words: list[str]) -> int:
    """Calculate the maximum distance between two unequal words.

    Args:
        words: List of words (strings).

    Returns:
        The maximum absolute difference between indices i and j such that
        words[i] != words[j]. Returns 0 if all words are identical.

    Examples:
        >>> solve(["a","b","c","a"])
        3
        >>> solve(["aaa","aaa","aaa"])
        0
        >>> solve(["hello","world","hello","world"])
        3
    """
    if not words:
        return 0

    n = len(words)
    # If the first and last words differ, the whole array length minus one is the answer.
    if words[0] != words[-1]:
        return n - 1

    # Find the farthest index from the left where the word differs from the last element.
    left_distance = 0
    for index, word in enumerate(words):
        if word != words[-1]:
            left_distance = n - 1 - index
            break

    # Find the farthest index from the right where the word differs from the first element.
    right_distance = 0
    for index in range(n - 1, -1, -1):
        if words[index] != words[0]:
            right_distance = index
            break

    return max(left_distance, right_distance)