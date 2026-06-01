METADATA = {
    "id": 1160,
    "name": "Find Words That Can Be Formed by Characters",
    "slug": "find-words-that-can-be-formed-by-characters",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n * L)",
    "space_complexity": "O(1)",
    "description": "Find all words in a list that can be constructed using the characters provided in a source string, respecting character frequencies.",
}

def solve(chars: list[str], words: list[str]) -> list[str]:
    """
    Finds all words in the words list that can be formed using the characters in chars.

    Args:
        chars: A list of single-character strings representing the available pool.
        words: A list of strings to check against the character pool.

    Returns:
        A list of strings containing the words that can be formed.

    Examples:
        >>> solve(["a","a","b","c"], ["a","b","c","ab","abc","ac","aac","abc"])
        ['a', 'b', 'c', 'ab', 'abc', 'ac']
        >>> solve(["a","b","c"], ["a","b","c","ab","abc","ac","aac","abc"])
        ['a', 'b', 'c', 'ab', 'abc', 'ac', 'abc']
    """
    # Count the frequency of each character available in the source pool
    char_counts = {}
    for char in chars:
        char_counts[char] = char_counts.get(char, 0) + 1

    result = []

    for word in words:
        # Count the frequency of each character required by the current word
        word_counts = {}
        can_form = True
        
        for char in word:
            word_counts[char] = word_counts.get(char, 0) + 1
            
            # If the required character is not in pool or exceeds available count, fail early
            if char not in char_counts or word_counts[char] > char_counts[char]:
                can_form = False
                break
        
        if can_form:
            result.append(word)

    return result
