METADATA = {
    "id": 1961,
    "name": "Check If String Is a Prefix of Array",
    "slug": "check-if-string-is-a-prefix-of-array",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given string is a prefix of the array of strings by matching characters sequentially.",
}

def solve(word: str, words: list[str]) -> bool:
    """
    Checks if the given word is a prefix of the array of words.

    A word is a prefix of the array if the characters of the word can be 
    formed by concatenating the first few elements of the array in order.

    Args:
        word: The target string to check.
        words: A list of strings to check against.

    Returns:
        True if word is a prefix of the array, False otherwise.

    Examples:
        >>> solve("apple", ["app", "le", "apple"])
        True
        >>> solve("apple", ["app", "le", "ap", "ple"])
        False
        >>> solve("a", ["a", "b", "c"])
        True
    """
    word_index = 0
    word_length = len(word)
    
    # Iterate through each string in the array
    for current_word in words:
        # Check if the current word matches the segment of 'word' we are looking for
        # We use slicing or comparison; here we check if the current word matches 
        # the substring of 'word' starting at word_index.
        word_segment = word[word_index : word_index + len(current_word)]
        
        if current_word != word_segment:
            return False
        
        # Move the pointer forward by the length of the matched word
        word_index += len(current_word)
        
        # If we have matched all characters in the target word, we are done
        if word_index == word_length:
            return True
            
    # If we finish the loop and haven't matched the entire word, it's not a prefix
    return word_index == word_length
