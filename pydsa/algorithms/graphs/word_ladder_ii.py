METADATA = {
    "id": 126,
    "name": "Word Ladder II",
    "slug": "word_ladder_ii",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "backtracking", "shortest_path", "string"],
    "difficulty": "hard",
    "time_complexity": "O(N * K^2 + P)",
    "space_complexity": "O(N * K^2 + P)",
    "description": "Find all shortest transformation sequences from beginWord to endWord such that only one letter can be changed at a time.",
}

from collections import deque, defaultdict

def solve(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    """
    Finds all shortest transformation sequences from beginWord to endWord.

    Args:
        beginWord: The starting word.
        endWord: The target word.
        wordList: A list of valid words.

    Returns:
        A list of lists, where each inner list is a shortest transformation sequence.

    Examples:
        >>> solve("hit", "cog", ["hot","dot","dog","lot","log","cog"])
        [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
    """
    word_set = set(wordList)
    if endWord not in word_set:
        return []

    # distance_map stores the minimum steps to reach each word from beginWord
    # adjacency_map stores the DAG (Directed Acyclic Graph) of shortest paths
    distance_map = {beginWord: 0}
    adjacency_map = defaultdict(list)
    
    queue = deque([beginWord])
    found = False

    # Step 1: BFS to find the shortest distance and build the DAG
    while queue and not found:
        level_size = len(queue)
        visited_this_level = {}
        
        for _ in range(level_size):
            current_word = queue.popleft()
            current_dist = distance_map[current_word]

            # Try all possible single-character transformations
            for i in range(len(current_word)):
                for char_code in range(ord('a'), ord('z') + 1):
                    char = chr(char_code)
                    if char == current_word[i]:
                        continue
                    
                    next_word = current_word[:i] + char + current_word[i+1:]

                    if next_word in word_set:
                        # If we haven't seen this word in previous levels
                        if next_word not in distance_map:
                            if next_word not in visited_this_level:
                                visited_this_level[next_word] = current_dist + 1
                                queue.append(next_word)
                            
                            # If this is a valid shortest path edge
                            if visited_this_level[next_word] == current_dist + 1:
                                adjacency_map[current_word].append(next_word)
                        
                        if next_word == endWord:
                            found = True

        # Update distance map with words found at this level to prevent cycles/longer paths
        for word, dist in visited_this_level.items():
            distance_map[word] = dist

    if not found:
        return []

    # Step 2: Backtracking (DFS) to reconstruct all paths from the DAG
    results = []

    def backtrack(current_path: list[str]):
        current_node = current_path[-1]
        if current_node == endWord:
            results.append(list(current_path))
            return

        if current_node in adjacency_map:
            for neighbor in adjacency_map[current_node]:
                # Only follow edges that move us closer to the target in the DAG
                # (Though adjacency_map is already built as a DAG, this is safe)
                current_path.append(neighbor)
                backtrack(current_path)
                current_path.pop()

    backtrack([beginWord])
    return results
