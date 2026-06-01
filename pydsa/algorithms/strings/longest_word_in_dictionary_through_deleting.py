METADATA = {
    "id": 524,
    "name": "Longest Word in Dictionary through Deleting",
    "slug": "longest-word-in-dictionary-through-deleting",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "sorting", "string"],
    "difficulty": "medium",
    "time_complexity": "O(N * L)",
    "space_complexity": "O(1)",
    "description": "Find the longest word in a dictionary that can be formed by deleting characters from a target string.",
}

def solve(s: str, dictionary: list[str]) -> str:
    """
    Finds the longest word in the dictionary that is a subsequence of the target string s.
    If multiple words have the same maximum length, the lexicographically smallest one is returned.

    Args:
        s: The target string.
        dictionary: A list of strings to search through.

    Returns:
        The longest lexicographically smallest word that is a subsequence of s.
        Returns an empty string if no such word exists.

    Examples:
        >>> solve("abpcplea", ["ale", "apple", "monkey", "plea"])
        'apple'
        >>> solve("abpcplea", ["a", "b", "c"])
        'a'
    """
    longest_word = ""

    # Sort dictionary: primary key is length (descending), secondary key is lexicographical (ascending)
    # This allows us to return the first valid word we find that meets the criteria.
    # However, to keep the logic simple and avoid complex sorting, we can just iterate 
    # and compare against the current best.
    
    for word in dictionary:
        # Check if 'word' is a subsequence of 's' using two pointers
        s_idx = 0
        word_idx = 0
        
        while s_idx < len(s) and word_idx < len(word):
            if s[s_idx] == word[word_idx]:
                word_idx += 1
            s_idx += 1
        
        # If word_idx reached the end, the whole word was found as a subsequence
        if word_idx == len(word):
            # Update longest_word if:
            # 1. Current word is longer than the best found so far
            # 2. Current word is same length but lexicographically smaller
            if len(word) > len(longest_word):
                longest_word = word
            elif len(word) == len(longest_word):
                if word < longest_word:
                    longest_word = word
                    
    return longest_word
