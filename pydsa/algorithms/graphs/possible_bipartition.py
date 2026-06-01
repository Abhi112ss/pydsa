METADATA = {
    "id": 886,
    "name": "Possible Bipartition",
    "slug": "possible_bipartition",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "union_find", "bipartite"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Determine if a group of people can be partitioned into two sets such that no two people in the same set dislike each other.",
}

def solve(dislikes: list[list[int]]) -> bool:
    """
    Determages if the given dislike relationships allow for a bipartite partition.

    Args:
        dislikes: A list of pairs where each pair [a, b] represents that person a 
                  dislikes person b.

    Returns:
        True if the graph is bipartite (can be 2-colored), False otherwise.

    Examples:
        >>> solve([[1, 2], [1, 3], [1, 4]])
        True
        >>> solve([[1, 2], [1, 3], [2, 3]])
        False
    """
    # Find the maximum person ID to determine the number of nodes
    # People are 1-indexed
    max_person = 0
    for u, v in dislikes:
        if u > max_person:
            max_person = u
        if v > max_person:
            max_person = v

    # Build adjacency list for the undirected graph
    adj: dict[int, list[int]] = {}
    for u, v in dislikes:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)

    # color_map stores the color (0 or 1) assigned to each person
    color_map: dict[int, int] = {}

    # Iterate through all people to handle disconnected components
    for person in range(1, max_person + 1):
        if person not in color_map and person in adj:
            # Start BFS for each unvisited component
            queue: list[int] = [person]
            color_map[person] = 0  # Assign initial color
            
            idx = 0
            while idx < len(queue):
                current = queue[idx]
                idx += 1
                
                current_color = color_map[current]
                neighbor_color = 1 - current_color
                
                for neighbor in adj.get(current, []):
                    if neighbor not in color_map:
                        # If neighbor is not colored, assign the opposite color
                        color_map[neighbor] = neighbor_color
                        queue.append(neighbor)
                    elif color_map[neighbor] == current_color:
                        # If neighbor has the same color, the graph is not bipartite
                        return False
                        
    return True
