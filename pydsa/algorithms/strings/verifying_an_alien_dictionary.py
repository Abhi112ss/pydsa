METADATA = {
    "id": 953,
    "name": "Verifying an Alien Dictionary",
    "slug": "verifying_an_alien_dictionary",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string_comparison"],
    "difficulty": "easy",
    "time_complexity": "O(c)",
    "space_complexity": "O(1)",
    "description": "Check if a list of words is sorted according to a given alien alphabet order.",
}


def solve(words: list[str], order: str) -> bool:
    """Determine whether the given list of words is sorted according to an alien alphabet.

    Args:
        words: A list of lowercase English words to be verified.
        order: A permutation of the 26 lowercase English letters representing the alien order.

    Returns:
        True if the words are sorted lexicographically under the alien order, otherwise False.

    Examples:
        >>> solve(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
        True
        >>> solve(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
        False
        >>> solve(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
        False
    """
    # Build a direct mapping from character to its rank in the alien alphabet.
    alien_rank: dict[str, int] = {character: index for index, character in enumerate(order)}

    # Compare each adjacent pair of words.
    for first_index in range(len(words) - 1):
        first_word = words[first_index]
        second_word = words[first_index + 1]

        # Find the first differing character between the two words.
        for position in range(min(len(first_word), len(second_word))):
            first_char = first_word[position]
            second_char = second_word[position]

            if first_char != second_char:
                # If the order of the differing characters is incorrect, the list is not sorted.
                if alien_rank[first_char] > alien_rank[second_char]:
                    return False
                # Correct ordering found; move to the next pair.
                break
        else:
            # All characters matched up to the length of the shorter word.
            # The longer word should not come before the shorter one.
            if len(first_word) > len(second_word):
                return False

    return True