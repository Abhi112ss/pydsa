METADATA = {
    "id": 1859,
    "name": "Sorting the Sentence",
    "slug": "sorting-the-sentence",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reorder words in a sentence based on the digit at the end of each word.",
}

def solve(sentence: str) -> str:
    """
    Reorders the words in a sentence such that the word with the digit '1' 
    comes first, '2' second, and so on.

    Args:
        sentence: A string containing words, each ending with a digit representing its position.

    Returns:
        A string containing the words in the correct order, separated by single spaces.

    Examples:
        >>> solve("is2 sentence4 a3 sentence1")
        'sentence1 is2 a3 sentence4'
        >>> solve("l0veleetcode")
        'l0veleetcode'
    """
    # Split the sentence into individual words
    words = sentence.split()
    
    # Initialize a list of the same size to hold words in their correct positions
    # We use a list because strings are immutable in Python
    result_array: list[str] = [None] * len(words)
    
    for word in words:
        # The last character is the position index (1-based)
        # We convert it to an integer and subtract 1 for 0-based indexing
        position_index = int(word[-1]) - 1
        
        # Extract the word content by removing the trailing digit
        actual_word = word[:-1]
        
        # Place the word in its designated slot in the result array
        result_array[position_index] = actual_word
        
    # Join the words back into a single string separated by spaces
    return " ".join(result_array)
