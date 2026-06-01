METADATA = {
    "id": 2204,
    "name": "Distance to a Cycle in Undirected Graph",
    "slug": "distance_to_a_cycle_in_undirected_graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "graph", "cycle_detection", "topological_sort"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the minimum distance from each node to any node that is part of a cycle in an undirected graph.",
}

from collections import deque

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Calculates the minimum distance from each node to any node belonging to a cycle.

    Args:
        n: The number of nodes in the undirected graph.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        A list of integers where the i-th element is the distance to the nearest cycle node.
        Returns -1 if no cycle exists.

    Examples:
        >>> solve(4, [[0, 1], [1, 2], [2, 3], [3, 1]])
        [1, 0, 0, 0]
        >>> solve(3, [[0, 1], [1, 2]])
        [-1, -1, -1]
    """
    adj = [[] for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Step 1: Use Kahn's algorithm (topological sort) to prune all nodes 
    # that are not part of any cycle. In an undirected graph, nodes with 
    # degree 1 are leaves and cannot be part of a cycle.
    queue = deque([i for i in range(n) if degree[i] == 1])
    is_cycle_node = [True] * n
    
    while queue:
        curr = queue.popleft()
        is_cycle_node[curr] = False
        for neighbor in adj[curr]:
            degree[neighbor] -= 1
            if degree[neighbor] == 1:
                queue.append(neighbor)

    # Step 2: Identify all nodes that are part of a cycle.
    # If no nodes are left with is_cycle_node == True, there are no cycles.
    cycle_nodes = [i for i in range(n) if is_cycle_node[i]]
    if not cycle_nodes:
        return [-1] * n

    # Step 3: Multi-source BFS starting from all cycle nodes to find 
    # the shortest distance from every node to the nearest cycle node.
    distances = [-1] * n
    bfs_queue = deque()

    for node in cycle_nodes:
        distances[node] = 0
        bfs_queue.append(node)

    while bfs_queue:
        curr = bfs_queue.popleft()
        for neighbor in adj[curr]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[curr] + 1
                bfs_queue.append(neighbor)

    return distances
