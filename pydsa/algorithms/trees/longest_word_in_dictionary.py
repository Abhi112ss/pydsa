METADATA = {
    "id": 720,
    "name": "Longest Word in Dictionary",
    "slug": "longest-word-in-dictionary",
    "category": "String",
    "aliases": [],
    "tags": ["trie", "hash_set", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N * L)",
    "space_complexity": "O(N * L)",
    "description": "Find the longest word in a list such that every prefix of the word is also present in the list.",
}

def solve(dictionary: list[str]) -> str:
    """
    Args:
        dictionary: A list of strings.

    Returns:
        The longest lexicographically smallest word such that every prefix is in the dictionary.
    """
    word_set = set(dictionary)
    longest_word = ""

    for word in dictionary:
        is_valid = True
        for i in range(1, len(word)):
            if word[:i + 1] not in word_set:
                is_valid = False
                break
        
        if is_valid:
            if len(word) > len(longest_word):
                longest_word = word
            elif len(word) == len(longest_word):
                if word < longest_word:
                    longest_word = word
                    
    return longest_word