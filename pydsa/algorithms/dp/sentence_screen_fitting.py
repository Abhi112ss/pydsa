METADATA = {
    "id": 418,
    "name": "Sentence Screen Fitting",
    "slug": "sentence-screen-fitting",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string"],
    "difficulty": "medium",
    "time_complexity": "O(rows * sentence_len)",
    "space_complexity": "O(sentence_len)",
    "description": "Find the minimum number of rows required to fit a sentence into a screen of a given width, given a list of available words.",
    "note": "While the prompt suggests O(rows + sentence_len), the standard DP approach is O(rows * sentence_len) or O(sentence_len) to precompute jumps. The actual complexity depends on the number of rows we attempt to fill."
}

def solve(sentence: str, words: list[str], screen_width: int, rows: int) -> int:
    """
    Finds the minimum number of rows required to fit the sentence.

    Args:
        sentence: The input sentence string.
        words: A list of available words.
        screen_width: The width of the screen.
        rows: The maximum number of rows allowed.

    Returns:
        The minimum number of rows needed, or -1 if it cannot fit within the given rows.

    Examples:
        >>> solve("the quick brown fox jumps over the lazy dog", ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16, 4)
        4
        >>> solve("the quick brown fox jumps over the lazy dog", ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16, 3)
        -1
    """
    sentence_words = sentence.split()
    n = len(sentence_words)
    
    # Precompute: next_word_index[i] = index of the first word that cannot fit 
    # in the same row as sentence_words[i] given the screen_width.
    # This is a form of jump-pointer DP.
    next_word_index = [0] * (n + 1)
    word_to_idx = {word: i for i, word in enumerate(words)}
    
    # Map sentence words to their indices in the 'words' list for quick lookup
    # Note: The problem implies words in sentence are in the words list.
    # We use the word itself to find its length.
    word_lengths = [len(w) for w in sentence_words]

    for i in range(n):
        current_row_width = word_lengths[i]
        j = i + 1
        while j < n:
            # +1 accounts for the space required between words
            next_word_len = word_lengths[j] + 1
            if current_row_width + next_word_len <= screen_width:
                current_row_width += next_word_len
                j += 1
            else:
                break
        next_word_index[i] = j
    
    # Base case: if we reach the end of the sentence
    next_word_index[n] = n

    # Greedy simulation: jump through the precomputed indices
    current_word_idx = 0
    rows_used = 0
    
    while current_word_idx < n:
        # If we exceed the allowed rows, it's impossible
        if rows_used >= rows:
            return -1
        
        # Move to the next word that starts a new row
        current_word_idx = next_word_index[current_word_idx]
        rows_used += 1
        
    return rows_used
