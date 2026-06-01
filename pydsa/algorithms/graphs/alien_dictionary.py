METADATA = {
    "id": 269,
    "name": "Alien Dictionary",
    "slug": "alien-dictionary",
    "category": "Graph",
    "aliases": [],
    "tags": ["topological_sort", "dfs", "bfs", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(C)",
    "space_complexity": "O(1)",
    "description": "Given a sorted list of words from an alien language, find the order of characters.",
}

def solve(words: list[str]) -> str:
    """
    Finds the lexicographical order of characters in an alien language.

    Args:
        words: A list of strings representing the sorted words in the alien language.

    Returns:
        A string representing the character order. Returns an empty string if 
        the order is invalid or a cycle is detected.

    Examples:
        >>> solve(["wrt", "wrf", "er", "ett", "rftt"])
        'wertf'
        >>> solve(["z", "x"])
        'zx'
        >>> solve(["z", "x", "z"])
        ''
    """
    # Initialize adjacency list and in-degree map for all unique characters
    adj_list: dict[str, set[str]] = {}
    in_degree: dict[str, int] = {}
    
    for word in words:
        for char in word:
            if char not in adj_list:
                adj_list[char] = set()
                in_degree[char] = 0

    # Build the graph by comparing adjacent words
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_len = min(len(word1), len(word2))
        
        # Check for prefix edge case: if word2 is a prefix of word1, it's invalid
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
            
        for j in range(min_len):
            if word1[j] != word2[j]:
                parent, child = word1[j], word2[j]
                # If this edge hasn't been added before, update in-degree
                if child not in adj_list[parent]:
                    adj_list[parent].add(child)
                    in_degree[child] += 1
                break

    # Kahn's Algorithm (BFS-based Topological Sort)
    # Start with all nodes that have an in-degree of 0
    queue: list[str] = [char for char in in_degree if in_degree[char] == 0]
    result_chars: list[str] = []
    
    # Use a simple pointer to simulate a queue for O(1) pops
    head = 0
    while head < len(queue):
        current = queue[head]
        head += 1
        result_chars.append(current)
        
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If result length doesn't match unique character count, a cycle exists
    if len(result_chars) != len(in_degree):
        return ""

    return "".join(result_chars)
