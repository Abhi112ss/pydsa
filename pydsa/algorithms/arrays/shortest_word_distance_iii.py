METADATA = {
    "id": 245,
    "name": "Shortest Word Distance III",
    "slug": "shortest-word-distance-iii",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the shortest distance between two words in an array, where the words may be identical.",
}

class Solution:
    def shortestWordDistance(self, words: list[str], word1: str, word2: str) -> int:
        """
        Finds the shortest distance between two words in a given list.

        Args:
            words: A list of strings.
            word1: The first target word.
            word2: The second target word.

        Returns:
            The minimum distance between the indices of word1 and word2.

        Examples:
            >>> sol = Solution()
            >>> sol.shortestWordDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")
            1
            >>> sol.shortestWordDistance(["a", "b", "c", "a"], "a", "a")
            2
        """
        # Initialize indices to -1 to represent that the words haven't been found yet
        index1: int = -1
        index2: int = -1
        min_distance: int = len(words)

        for current_index, word in enumerate(words):
            if word == word1:
                # If word1 and word2 are the same, we must update the previous index1 
                # before setting the new index1 to ensure we compare different occurrences.
                if word1 == word2:
                    if index1 != -1:
                        min_distance = min(min_distance, current_index - index1)
                    index1 = current_index
                else:
                    index1 = current_index
            
            # Use 'elif' only if word1 != word2. If they are the same, the first block 
            # handles the logic for both indices.
            elif word == word2:
                index2 = current_index

            # If we have found both words at least once, calculate the distance.
            # Note: The logic for word1 == word2 is handled inside the first if-block.
            if word1 != word2 and index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))

        # Re-check distance for the case where word1 == word2 if not handled inside loop
        # However, the logic above handles word1 == word2 by updating min_distance 
        # every time a new occurrence of the same word is found.
        
        # Final pass for word1 == word2 logic if the loop structure was different, 
        # but here it is integrated.
        if word1 == word2:
            # The logic inside the loop for word1 == word2:
            # 1. Find first occurrence: index1 = 0, index2 = -1
            # 2. Find second occurrence: min_dist = 1-0, index1 = 1
            # This correctly tracks the distance between consecutive identical words.
            pass

        return min_distance

def solve(words: list[str], word1: str, word2: str) -> int:
    """
    Helper function to call the Solution class.
    """
    return Solution().shortestWordDistance(words, word1, word2)
