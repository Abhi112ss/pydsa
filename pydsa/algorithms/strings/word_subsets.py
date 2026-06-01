METADATA = {
    "id": 916,
    "name": "Word Subsets",
    "slug": "word-subsets",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(A + B)",
    "space_complexity": "O(1)",
    "description": "Determine which words in a list can be constructed using characters from a given dictionary.",
}

def solve(words: list[str], letters: list[str]) -> list[str]:
    """
    Finds all words in the 'words' list that can be formed using the characters in 'letters'.

    Args:
        words: A list of strings to check.
        letters: A list of characters available for use.

    Returns:
        A list of strings from 'words' that can be constructed using the available letters.

    Examples:
        >>> solve(["apple", "pear", "peach"], ["a", "p", "l", "e", "c", "h"])
        ['apple', 'peach']
        >>> solve(["a", "b", "c"], ["a", "b"])
        ['a', 'b']
    """
    # Create a frequency map for the available letters
    # Since we only deal with lowercase English letters, space is O(1)
    available_counts = [0] * 26
    for char in letters:
        available_counts[ord(char) - ord('a')] += 1

    result = []

    for word in words:
        # Create a frequency map for the current word
        word_counts = [0] * 26
        can_form = True
        
        for char in word:
            index = ord(char) - ord('a')
            word_counts[index] += 1
            
            # If the word requires more of a character than available, it's invalid
            if word_counts[index] > available_counts[index]:
                can_form = False
                break
        
        if can_form:
            result.append(word)

    return result
