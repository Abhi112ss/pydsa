METADATA = {
    "id": 792,
    "name": "Number of Matching Subsequences",
    "slug": "number-of-matching-subsequences",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "trie", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(sum(len(word) + len(s)))",
    "space_complexity": "O(len(words))",
    "description": "Count how many words in a list are subsequences of a given string s.",
}

from collections import defaultdict

def solve(s: str, words: list[str]) -> int:
    """
    Counts the number of words in the list that are subsequences of string s.
    
    Uses a bucket-based approach where words are grouped by the next character 
    they are waiting for in the sequence. This allows us to process the 
    string 's' in a single pass.

    Args:
        s: The target string to check subsequences against.
        words: A list of strings to check.

    Returns:
        The count of words that are subsequences of s.

    Examples:
        >>> solve("abcde", ["a","bb","acd","ace"])
        3
        >>> solve("bag", ["baba"])
        0
    """
    # A dictionary mapping characters to a list of iterators.
    # Each iterator represents a word that is currently waiting for that character.
    waiting_buckets = defaultdict(list)
    
    for word in words:
        # We convert each word into an iterator to track progress efficiently.
        it = iter(word)
        # The first character the word is looking for:
        first_char = next(it, None)
        if first_char is None:
            # This handles the edge case of an empty string word (always a subsequence)
            # However, based on constraints, words are non-empty. 
            # If empty words were allowed, we'd increment a counter here.
            pass 
        else:
            waiting_buckets[first_char].append(it)

    # We also need to handle empty strings if they were in the input
    # But per LeetCode constraints, words[i].length >= 1.
    # If we wanted to be robust: count_empty = words.count("")
    count = 0
    
    # Iterate through each character in the target string s
    for char in s:
        # Get the list of iterators waiting for the current character
        # and clear the bucket for this character to avoid re-processing
        current_waiters = waiting_buckets.pop(char, [])
        
        for it in current_waiters:
            # Advance the iterator to the next character
            next_char = next(it, None)
            
            if next_char is None:
                # If the iterator is exhausted, the word is a complete subsequence
                count += 1
            else:
                # Otherwise, put the iterator into the bucket for its next required character
                waiting_buckets[next_char].append(it)
                
    return count
