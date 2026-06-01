METADATA = {
    "id": 1917,
    "name": "Leetcodify Friends Recommendations",
    "slug": "leetcodify_friends_recommendations",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "breadth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find all users within a distance of 2 in a friendship graph for each user.",
}

from collections import deque, defaultdict

def solve(n: int, friendships: list[list[int]]) -> list[list[int]]:
    """
    Finds all users within a distance of 2 in a friendship graph for each user.

    Args:
        n: The total number of users (labeled 0 to n-1).
        friendships: A list of pairs [u, v] representing a friendship between u and v.

    Returns:
        A list of lists where the i-th list contains the IDs of users within 
        distance 2 of user i, excluding user i themselves.

    Examples:
        >>> solve(4, [[0, 1], [1, 2], [2, 3]])
        [[1, 2], [0, 2, 3], [1, 3, 0], [2, 1]]
    """
    # Build adjacency list to represent the undirected graph
    adj = defaultdict(list)
    for u, v in friendships:
        adj[u].append(v)
        adj[v].append(u)

    recommendations = []

    for start_node in range(n):
        # Use BFS to find nodes within distance 2
        visited = {start_node}
        distance_two_nodes = []
        queue = deque([(start_node, 0)])

        while queue:
            current_node, current_dist = queue.popleft()

            # If we have reached distance 2, we don't explore neighbors further
            if current_dist < 2:
                for neighbor in adj[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        distance_two_nodes.append(neighbor)
                        queue.append((neighbor, current_dist + 1))
        
        # The problem asks for nodes within distance 2. 
        # Note: The order of nodes in the output list is not specified, 
        # but BFS naturally finds them in increasing order of distance.
        recommendations.append(distance_two_nodes)

    return recommendations
