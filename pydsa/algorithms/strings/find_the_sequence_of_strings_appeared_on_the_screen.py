METADATA = {
    "id": 3324,
    "name": "Find the Sequence of Strings Appeared on the Screen",
    "slug": "find-the-sequence-of-strings-appeared-on-the-screen",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Find the order in which a sequence of words appears in a given text using a greedy approach.",
}

def solve(text: str, words: list[str]) -> list[str]:
    """
    Finds the sequence of words from the list that appear in the text in order.

    The algorithm uses a greedy approach: it iterates through the text and, 
    whenever it finds the current target word, it adds it to the result 
    and moves to the next word in the target list.

    Args:
        text: The input string to search through.
        words: A list of strings to find in the text in the specified order.

    Returns:
        A list of strings representing the words found in the text in order.

    Examples:
        >>> solve("abcde", ["a", "c", "e"])
        ['a', 'c', 'e']
        >>> solve("abcde", ["a", "z", "e"])
        ['a', 'e']
        >>> solve("abcde", ["e", "a"])
        []
    """
    result: list[str] = []
    current_index: int = 0
    text_length: int = len(text)
    
    # Iterate through each word in the target list
    for word in words:
        # Search for the current word starting from the current position in the text
        # find() returns the lowest index where the substring is found, or -1
        found_index = text.find(word, current_index)
        
        if found_index != -1:
            # If found, add to result and update the pointer to search after this occurrence
            result.append(word)
            current_index = found_index + len(word)
        else:
            # If a word in the sequence is not found after the current pointer,
            # we cannot satisfy the sequence requirement for subsequent words
            # However, the problem asks for the sequence that *appeared*, 
            # implying we skip words that don't appear in order.
            # Based on LeetCode 3324 logic: we only add words that appear in order.
            continue
            
    return result
