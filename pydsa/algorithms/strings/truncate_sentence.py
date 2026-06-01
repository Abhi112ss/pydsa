METADATA = {
    "id": 1816,
    "name": "Truncate Sentence",
    "slug": "truncate-sentence",
    "category": "String",
    "aliases": [],
    "tags": ["string", "substring"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Truncate a sentence to include only the first k words.",
}

def solve(sentence: str, k: int) -> str:
    """
    Truncates the given sentence to include only the first k words.

    Args:
        sentence: The input string containing words separated by single spaces.
        k: The number of words to keep in the truncated sentence.

    Returns:
        The truncated sentence containing the first k words.

    Examples:
        >>> solve("Leetcode is great", 2)
        'Leetcode is'
        >>> solve("Hello world", 1)
        'Hello'
    """
    # We need to find the index of the k-th space.
    # If k is 1, we look for the first space.
    # If k is 2, we look for the second space, and so on.
    
    space_count = 0
    for index, char in enumerate(sentence):
        if char == ' ':
            space_count += 1
            
        # Once we have encountered k spaces, the k-th word ends 
        # just before this space.
        if space_count == k:
            return sentence[:index]
            
    # If we finish the loop without finding k spaces, it means 
    # the sentence has k or fewer words.
    return sentence
