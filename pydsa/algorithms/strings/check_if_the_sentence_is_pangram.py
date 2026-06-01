METADATA = {
    "id": 1832,
    "name": "Check if the Sentence Is Pangram",
    "slug": "check_if_the_sentence_is_pangram",
    "category": "String",
    "aliases": [],
    "tags": ["hash_set", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine whether a sentence contains every letter of the English alphabet.",
}


def solve(sentence: str) -> bool:
    """Check if the given sentence is a pangram.

    Args:
        sentence: A string consisting of lowercase English letters and spaces.

    Returns:
        True if the sentence contains every letter from 'a' to 'z', otherwise False.

    Examples:
        >>> solve("thequickbrownfoxjumpsoverthelazydog")
        True
        >>> solve("leetcode")
        False
    """
    # Collect unique alphabetic characters in the sentence
    unique_letters = {char for char in sentence if 'a' <= char <= 'z'}

    # The sentence is a pangram if we have all 26 letters
    return len(unique_letters) == 26