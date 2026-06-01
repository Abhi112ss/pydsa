METADATA = {
    "id": 2737,
    "name": "Find the Closest Marked Node",
    "slug": "find-the-closest-marked-node",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the closest marked node for each node in a tree using multi-source BFS.",
}

from collections import deque

def solve(n: int, edges: list[list[int]], marked: list[int]) -> list[int]:
    """
    Finds the closest marked node for each node in a tree using multi-source BFS.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges where edges[i] = [u, v].
        marked: A list of node indices that are marked.

    Returns:
        A list of integers where the i-th element is the index of the closest 
        marked node to node i. If there is a tie, the node with the smallest 
        index is chosen.

    Examples:
        >>> solve(5, [[0,1],[1,2],[1,3],[3,4]], [2,4])
        [2, 2, 2, 4, 4]
    """
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # result[i] stores the closest marked node to node i
    # Initialize with -1 to indicate unvisited
    result: list[int] = [-1] * n
    
    # Queue for multi-source BFS
    # We sort marked nodes initially to handle the "smallest index" tie-breaking rule.
    # By processing smaller indices first in the BFS, the first time we reach 
    # an unvisited node, it is guaranteed to be via the closest marked node,
    # and among those at the same distance, the one with the smallest index.
    queue: deque[int] = deque(sorted(marked))
    
    for m in marked:
        result[m] = m

    while queue:
        current_node = queue.popleft()
        
        for neighbor in adj[current_node]:
            # If the neighbor hasn't been visited yet
            if result[neighbor] == -1:
                # The closest marked node to 'neighbor' is the 'current_node's' closest marked node
                result[neighbor] = result[current_node]
                queue.append(neighbor)
                
    return result
