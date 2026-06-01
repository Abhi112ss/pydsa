METADATA = {
    "id": 3582,
    "name": "Generate Tag for Video Caption",
    "slug": "generate-tag-for-video-caption",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Identify the most frequent word in a caption to generate a single representative tag, handling punctuation and case sensitivity.",
}

def solve(caption: str, stop_words: list[str]) -> str:
    """
    Generates a single representative tag for a video caption by finding the 
    most frequent word that is not in the provided stop_words list.

    The function processes the caption by converting it to lowercase and 
    removing non-alphanumeric characters. If multiple words have the same 
    maximum frequency, the one that appears first in the caption is chosen.

    Args:
        caption: The raw string containing the video caption.
        stop_words: A list of words to be ignored when counting frequencies.

    Returns:
        The most frequent non-stop-word as a string. Returns an empty string 
        if no valid words are found.

    Examples:
        >>> solve("Hello world! Hello everyone.", ["everyone"])
        'hello'
        >>> solve("Coding is fun, coding is life.", ["is"])
        'coding'
    """
    import re

    # Convert to lowercase and use regex to extract only alphanumeric words
    # This handles punctuation like 'world!' -> 'world'
    words = re.findall(r'\w+', caption.lower())
    
    # Convert stop_words to a set for O(1) average lookup time
    stop_words_set = set(word.lower() for word in stop_words)
    
    word_counts: dict[str, int] = {}
    # We need to track the first appearance index to break ties correctly
    first_appearance: dict[str, int] = {}
    
    valid_word_count = 0
    
    for index, word in enumerate(words):
        if word not in stop_words_set:
            # Update frequency count
            word_counts[word] = word_counts.get(word, 0) + 1
            
            # Record the first time we see this specific valid word
            if word not in first_appearance:
                first_appearance[word] = index
            
            valid_word_count += 1

    if not word_counts:
        return ""

    # Find the word with the maximum frequency. 
    # In case of ties, the word with the smallest first_appearance index is chosen.
    best_word = ""
    max_freq = -1
    
    for word, count in word_counts.items():
        if count > max_freq:
            max_freq = count
            best_word = word
        elif count == max_freq:
            # Tie-breaking: choose the word that appeared earlier in the original sequence
            if first_appearance[word] < first_appearance[best_word]:
                best_word = word
                
    return best_word
