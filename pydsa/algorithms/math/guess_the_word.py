METADATA = {
    "id": 843,
    "name": "Guess the Word",
    "slug": "guess-the-word",
    "category": "Interactive",
    "aliases": [],
    "tags": ["minimax", "randomized", "string"],
    "difficulty": "hard",
    "time_complexity": "O(N * L)",
    "space_complexity": "O(N)",
    "description": "Find a hidden word in a list of words by minimizing the number of guesses using a strategy that filters candidates based on match counts.",
}

class Solution:
    def findSecretWord(self, words: list[str], master: 'Master') -> None:
        """
        Finds the secret word by iteratively filtering the candidate list.
        
        The strategy uses a heuristic to pick a word that minimizes the 
        worst-case number of remaining candidates. A common effective 
        heuristic is to pick a word that has the most 'average' match 
        distribution or simply picking words that are likely to prune 
        the search space significantly.

        Args:
            words: A list of strings representing the candidate words.
            master: An instance of the Master class with a guess(word) method.

        Returns:
            None. The result is communicated via master.compare(word).

        Examples:
            >>> # This is a conceptual example as master is an interface
            >>> words = ["apple", "apply", "ample"]
            >>> master.compare("apple") -> 2
            >>> # The algorithm would then filter words that don't have 2 matches with "apple"
        """

        def get_match_count(word1: str, word2: str) -> int:
            """Calculates the number of indices where characters match."""
            count = 0
            for char1, char2 in zip(word1, word2):
                if char1 == char2:
                    count += 1
            return count

        def get_score_distribution(target_word: str, candidates: list[str]) -> dict[int, int]:
            """Counts how many candidates would result in each possible match score."""
            distribution = {}
            for word in candidates:
                score = get_match_count(target_word, word)
                distribution[score] = distribution.get(score, 0) + 1
            return distribution

        # We perform up to 10 guesses as per problem constraints
        for _ in range(10):
            if not words:
                break
            
            # Heuristic: Pick a word that minimizes the maximum possible size of the next candidate list.
            # We evaluate each word by looking at its score distribution.
            # The 'worst case' for a word is the largest group in its distribution.
            best_word = words[0]
            min_max_group_size = float('inf')

            # To keep complexity manageable, we can sample or just iterate.
            # For LeetCode constraints, iterating through the current list is fine.
            for candidate in words:
                dist = get_score_distribution(candidate, words)
                # The worst case is the size of the largest group of words 
                # that share the same match count with this candidate.
                max_group_size = max(dist.values()) if dist else 0
                
                if max_group_size < min_max_group_size:
                    min_max_group_size = max_group_size
                    best_word = candidate

            # Perform the guess
            matches = master.compare(best_word)
            
            if matches == 6:
                # Found the word
                return

            # Filter the list: only keep words that have exactly 'matches' 
            # characters in common with the guessed word.
            new_words = []
            for word in words:
                if get_match_count(best_word, word) == matches:
                    new_words.append(word)
            
            words = new_words

# Note: The Master class is provided by the LeetCode environment.
# The implementation above follows the minimax-inspired heuristic.