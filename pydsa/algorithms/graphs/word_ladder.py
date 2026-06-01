METADATA = {
    "id": 127,
    "name": "Word Ladder",
    "slug": "word-ladder",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "shortest_path", "string"],
    "difficulty": "hard",
    "time_complexity": "O(M^2 * N)",
    "space_complexity": "O(M^2 * N)",
    "description": "Find the length of the shortest transformation sequence from beginWord to endWord using a dictionary of allowed words.",
}

from collections import deque

def solve(beginWord: str, endWord: str, wordList: list[str]) -> int:
    """
    Finds the length of the shortest transformation sequence from beginWord to endWord.

    Args:
        beginWord: The starting word.
        endWord: The target word.
        wordList: A list of valid words that can be used in the transformation.

    Returns:
        The number of words in the shortest transformation sequence, or 0 if no such sequence exists.

    Examples:
        >>> solve("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        7
        >>> solve("hit", "cog", ["hot","dot","dog","lot","log"])
        0
    """
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    # Queue stores tuples of (current_word, current_distance)
    queue = deque([(beginWord, 1)])
    
    # Track visited words to prevent infinite loops and redundant processing
    visited = {beginWord}

    while queue:
        current_word, distance = queue.popleft()

        if current_word == endWord:
            return distance

        # Try changing each character position in the word
        for i in range(len(current_word)):
            original_char = current_word[i]
            
            # Iterate through all possible lowercase English letters
            for char_code in range(ord('a'), ord('z') + 1):
                new_char = chr(char_code)
                if new_char == original_char:
                    continue
                
                # Construct the new candidate word
                next_word = current_word[:i] + new_char + current_word[i+1:]

                # If the word is in the dictionary and hasn't been visited
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, distance + 1))
                    
    return 0
