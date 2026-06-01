METADATA = {
    "id": 140,
    "name": "Word Break II",
    "slug": "word-break-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["backtracking", "dynamic_programming", "memoization", "string"],
    "difficulty": "hard",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(2^n)",
    "description": "Given a string and a dictionary of words, return all possible sentences that can be formed by inserting spaces in the string.",
}

def solve(s: str, wordDict: list[str]) -> list[str]:
    """
    Finds all possible ways to segment the string 's' using words from 'wordDict'.

    Args:
        s: The input string to be segmented.
        wordDict: A list of valid words.

    Returns:
        A list of all possible space-separated sentences.

    Examples:
        >>> solve("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        ['cat sand dog', 'cats and dog']
        >>> solve("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
        ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']
    """
    word_set = set(wordDict)
    memo: dict[int, list[str]] = {}

    def backtrack(start_index: int) -> list[str]:
        """
        Recursive helper that uses memoization to find all valid suffixes.
        
        Args:
            start_index: The current starting position in the string 's'.
            
        Returns:
            A list of sentence fragments starting from start_index.
        """
        # If we have already computed results for this suffix, return them
        if start_index in memo:
            return memo[start_index]

        # Base case: if we reached the end of the string, return a list with an empty string
        # to signify a successful path completion.
        if start_index == len(s):
            return [""]

        results: list[str] = []

        # Try every possible end position for the current word
        for end_index in range(start_index + 1, len(s) + 1):
            current_word = s[start_index:end_index]
            
            if current_word in word_set:
                # Recursively find all ways to complete the sentence from the next index
                sub_sentences = backtrack(end_index)
                
                for sub in sub_sentences:
                    # If sub is empty, it means we reached the end of the string
                    if sub == "":
                        results.append(current_word)
                    else:
                        # Otherwise, join the current word with the suffix results
                        results.append(f"{current_word} {sub}")

        # Store the computed results for this index to avoid redundant work
        memo[start_index] = results
        return results

    return backtrack(0)
