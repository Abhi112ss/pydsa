METADATA = {
    "id": 2492,
    "name": "Minimum Score of a Path Between Two Cities",
    "slug": "minimum-score-of-a-path-between-two-cities",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "bfs", "union_find"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum score of a path between two cities where the score is the minimum weight of any edge on the path.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Finds the minimum score of a path between city 1 and city 2.
    
    The score of a path is the minimum weight of any edge on that path.
    Since all nodes in a connected component can reach each other, the 
    minimum score for any two nodes in the same component is the minimum 
    edge weight present in that entire component.

    Args:
        n: The number of cities.
        edges: A list of edges where edges[i] = [u, v, weight].

    Returns:
        The minimum score of a path between city 1 and city 2.

    Examples:
        >>> solve(3, [[0, 1, 5], [1, 2, 6]])
        5
        >>> solve(3, [[0, 1, 5], [1, 2, 10], [0, 2, 1]])
        1
    """
    # Build adjacency list where each entry is (neighbor, weight)
    adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
    for u, v, weight in edges:
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    visited: set[int] = set()
    # We only need to find the minimum edge weight in the component 
    # containing city 0 (which represents city 1 in 0-indexed logic).
    # Since the problem guarantees city 1 and 2 are connected, 
    # we just traverse the component.
    min_score = float('inf')

    # Iterative DFS to avoid recursion depth issues in large graphs
    stack: list[int] = [0]
    visited.add(0)

    while stack:
        current_node = stack.pop()
        
        for neighbor, weight in adj[current_node]:
            # Update the global minimum weight found in this component
            if weight < min_score:
                min_score = weight
            
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return int(min_score)
