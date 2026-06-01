METADATA = {
    "id": 244,
    "name": "Shortest Word Distance II",
    "slug": "shortest-word-distance-ii",
    "category": "Design",
    "aliases": [],
    "tags": ["hash_map", "two_pointer", "design"],
    "difficulty": "medium",
    "time_complexity": "O(N) for initialization, O(K) for query where K is frequency of word",
    "space_complexity": "O(N)",
    "description": "Design a class that finds the shortest distance between two words in a list of words.",
}

from collections import defaultdict

class WordDistance:
    def __init__(self, words: list[str]):
        """
        Initializes the object with a list of words.

        Args:
            words: A list of strings.
        """
        # Map each word to a list of its indices in the input array
        self.word_indices: dict[str, list[int]] = defaultdict(list)
        for index, word in enumerate(words):
            self.word_indices[word].append(index)

    def shortestDistance(self, word1: str, word2: str) -> int:
        """
        Finds the shortest distance between two words.

        Args:
            word1: The first word.
            word2: The second word.

        Returns:
            The minimum distance between any occurrence of word1 and word2.

        Examples:
            >>> wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
            >>> wd.shortestDistance("makes", "coding")
            1
            >>> wd.shortestDistance("makes", "practice")
            1
        """
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]
        
        min_distance = float('inf')
        ptr1 = 0
        ptr2 = 0

        # Use two pointers to traverse the sorted index lists
        # Since indices are added sequentially, they are naturally sorted
        while ptr1 < len(indices1) and ptr2 < len(indices2):
            idx1 = indices1[ptr1]
            idx2 = indices2[ptr2]

            # Calculate the absolute difference between current indices
            diff = abs(idx1 - idx2)
            if diff < min_distance:
                min_distance = diff
            
            # If we found a distance of 1, it's the smallest possible
            if min_distance == 1:
                return 1

            # Move the pointer pointing to the smaller index to try and close the gap
            if idx1 < idx2:
                ptr1 += 1
            else:
                ptr2 += 1

        return int(min_distance)

def solve():
    """
    Entry point for testing the implementation.
    """
    words = ["practice", "makes", "perfect", "coding", "makes"]
    wd = WordDistance(words)
    
    # Test cases
    assert wd.shortestDistance("makes", "coding") == 1
    assert wd.shortestDistance("makes", "practice") == 1
    assert wd.shortestDistance("coding", "practice") == 3
    print("All test cases passed!")
