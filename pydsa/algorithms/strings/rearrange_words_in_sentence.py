METADATA = {
    "id": 1451,
    "name": "Rearrange Words in a Sentence",
    "slug": "rearrange-words-in-a-sentence",
    "category": "String",
    "aliases": [],
    "tags": ["string", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Rearrange words in a sentence such that they are sorted by length in ascending order, maintaining original order for equal lengths, and ensuring only the first word is capitalized.",
}

def solve(sentence: str) -> str:
    """
    Rearranges words in a sentence by length in ascending order.
    
    Words of the same length maintain their relative order from the original sentence.
    The first word in the resulting sentence must be capitalized, and all other 
    words must be lowercase.

    Args:
        sentence: The input string containing words separated by single spaces.

    Returns:
        The rearranged sentence string.

    Examples:
        >>> solve("is sentence This a test")
        'A is test This sentence'
        >>> solve("Keep looking forward to the future")
        'To the look Keep forward future'
    """
    # Split the sentence into individual words
    words = sentence.split()
    
    # Python's sort is stable (Timsort), so we only need to sort by length.
    # This preserves the original relative order for words with the same length.
    words.sort(key=len)
    
    # Process words to ensure correct casing:
    # 1. Convert all words to lowercase first to handle the "all other words lowercase" rule.
    # 2. Capitalize the very first word in the sorted list.
    processed_words = [word.lower() for word in words]
    processed_words[0] = processed_words[0].capitalize()
    
    # Join the words back into a single string separated by spaces
    return " ".join(processed_words)
