METADATA = {
    "id": 1255,
    "name": "Maximum Score Words Formed by Letters",
    "slug": "maximum-score-words-formed-by-letters",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "bitmask", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(2^n * word_len)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score you can get by picking a subset of words such that the total count of each letter used does not exceed the available letters.",
}

def solve(words: list[str], letters: str) -> int:
    """
    Calculates the maximum score possible by selecting a subset of words.

    Args:
        words: A list of strings representing the words available.
        letters: A string representing the available pool of letters.

    Returns:
        The maximum score achievable.

    Examples:
        >>> solve(["dog", "cat", "dad", "good"], "adg")
        0
        >>> solve(["a", "b", "c"], "abc")
        3
        >>> solve(["dog", "cat", "dad", "good"], "adg")
        0
        >>> solve(["apple", "pear", "peach"], "aapplee")
        0
    """
    # Pre-calculate frequency of available letters
    available_counts = [0] * 26
    for char in letters:
        available_counts[ord(char) - ord('a')] += 1

    # Pre-calculate frequency and score for each word
    word_data = []
    for word in words:
        counts = [0] * 26
        score = 0
        for char in word:
            idx = ord(char) - ord('a')
            counts[idx] += 1
            score += idx + 1
        word_data.append({"counts": counts, "score": score})

    num_words = len(words)

    def backtrack(index: int, current_counts: list[int]) -> int:
        """
        Explores word combinations using backtracking.

        Args:
            index: The current word index being considered.
            current_counts: The current tally of letters used.

        Returns:
            The maximum score from this point forward.
        """
        if index == num_words:
            return 0

        # Option 1: Skip the current word
        max_score = backtrack(index + 1, current_counts)

        # Option 2: Try to include the current word
        word_info = word_data[index]
        can_use = True
        
        # Check if the word can be formed with remaining letters
        for i in range(26):
            if word_info["counts"][i] > current_counts[i]:
                can_use = False
                break
        
        if can_use:
            # Deduct letters used by this word
            for i in range(26):
                current_counts[i] -= word_info["counts"][i]
            
            # Recurse and add current word's score
            score_with_word = word_info["score"] + backtrack(index + 1, current_counts)
            max_score = max(max_score, score_with_word)
            
            # Backtrack: Restore letters for other branches
            for i in range(26):
                current_counts[i] += word_info["counts"][i]

        return max_score

    return backtrack(0, available_counts)
