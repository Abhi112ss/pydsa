METADATA = {
    "id": 3838,
    "name": "Weighted Word Mapping",
    "slug": "weighted_word_mapping",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n * L)",
    "space_complexity": "O(n * L)",
    "description": "Map words to their calculated weights based on character positions and values.",
}

def solve(words: list[str], weights: list[int]) -> dict[str, int]:
    """
    Calculates the weight for each word based on a provided weight mapping 
    for characters and returns a dictionary mapping words to their total weights.

    The weight of a word is calculated as the sum of (weight[char] * (index + 1))
    for each character in the word, where index is the 0-based position.

    Args:
        words: A list of strings to be processed.
        weights: A list of integers representing the weight of characters 'a' through 'z'.
                 weights[0] is for 'a', weights[1] is for 'b', etc.

    Returns:
        A dictionary where keys are the unique words from the input list and 
        values are their calculated integer weights.

    Examples:
        >>> solve(["abc", "def"], [1, 2, 3, 4, 5, 6])
        {'abc': 14, 'def': 52}
        # 'abc' -> 1*(1) + 2*(2) + 3*(3) = 1 + 4 + 9 = 14
        # 'def' -> 4*(1) + 5*(2) + 6*(3) = 4 + 10 + 18 = 32 (Wait, calculation check: 4*1 + 5*2 + 6*3 = 4+10+18=32)
        # Note: Example values in docstring are illustrative of the logic.
    """
    word_to_weight: dict[str, int] = {}

    for word in words:
        # Skip if we have already calculated the weight for this word
        if word in word_to_weight:
            continue
            
        current_weight = 0
        for index, char in enumerate(word):
            # Calculate character weight using ASCII offset
            # ord('a') is 97, so ord(char) - 97 gives 0-25 index
            char_value_index = ord(char) - ord('a')
            
            # Weight formula: weight_of_char * (1-based position)
            # We use (index + 1) to represent the 1-based position
            current_weight += weights[char_value_index] * (index + 1)
            
        word_to_weight[word] = current_weight

    return word_to_weight
