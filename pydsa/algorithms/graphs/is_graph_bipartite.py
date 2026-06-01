METADATA = {
    "id": 785,
    "name": "Is Graph Bipartite?",
    "slug": "is-graph-bipartite",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graph_coloring", "traversal"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Determine if a graph is bipartite by checking if it can be colored with two colors such that no two adjacent nodes have the same color.",
}

def solve(graph: list[list[int]]) -> bool:
    """
    Determines if a given undirected graph is bipartite using Breadth-First Search (BFS).

    A graph is bipartite if we can split its vertices into two independent sets 
    U and V such that every edge connects a vertex in U to one in V. This is 
    equivalent to saying the graph is 2-colorable.

    Args:
        graph: An adjacency list where graph[i] is a list of nodes adjacent to node i.

    Returns:
        True if the graph is bipartite, False otherwise.

    Examples:
        >>> solve([[1,3],[0,2],[1,3],[0,2]])
        True
        >>> solve([[1,2,3],[0,2],[0,1,3],[0,2]])
        False
    """
    n = len(graph)
    # color_map stores the color assigned to each node: 0 for uncolored, 1 and -1 for the two colors.
    color_map = [0] * n

    for start_node in range(n):
        # If the node is already colored, it has been processed in a previous component.
        if color_map[start_node] != 0:
            continue

        # Start BFS for a new connected component
        queue = [start_node]
        color_map[start_node] = 1  # Assign initial color

        idx = 0
        while idx < len(queue):
            current_node = queue[idx]
            idx += 1

            for neighbor in graph[current_node]:
                # If the neighbor has the same color as the current node, it's not bipartite.
                if color_map[neighbor] == color_map[current_node]:
                    return False
                
                # If the neighbor is uncolored, assign the opposite color and add to queue.
                if color_map[neighbor] == 0:
                    color_map[neighbor] = -color_map[current_node]
                    queue.append(neighbor)

    return True
