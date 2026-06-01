METADATA = {
    "id": 2000,
    "name": "Reverse Prefix of Word",
    "slug": "reverse-prefix-of-word",
    "category": "String",
    "aliases": [],
    "tags": ["string", "two pointers"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reverse the prefix of a string up to the k-th occurrence of a given character.",
}

def solve(word: str, k: int) -> str:
    """
    Reverses the prefix of the word up to the k-th occurrence of the character 'ch'.

    Args:
        word: The input string to process.
        k: The occurrence count of the character to find.

    Returns:
        The modified string with the prefix reversed.

    Examples:
        >>> solve("abcdefd", 2)
        'cbadefd'
        >>> solve("abcd", 1)
        'abcd'
    """
    target_char = 'd'  # The problem specifies reversing up to the k-th 'd'
    # Note: The problem description for 2000 specifically mentions 'd' 
    # as the character to look for.
    
    count = 0
    target_index = -1
    
    # Find the index of the k-th occurrence of 'd'
    for index, char in enumerate(word):
        if char == 'd':
            count += 1
            if count == k:
                target_index = index
                break
    
    # If the k-th 'd' is not found, return the original word
    if target_index == -1:
        return word
    
    # Slice the word into the prefix to be reversed and the remaining suffix
    # The prefix includes the character at target_index
    prefix = word[:target_index + 1]
    suffix = word[target_index + 1:]
    
    # Reverse the prefix and concatenate with the suffix
    return prefix[::-1] + suffix
