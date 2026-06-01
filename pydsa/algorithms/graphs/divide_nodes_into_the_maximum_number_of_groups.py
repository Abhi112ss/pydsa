METADATA = {
    "id": 2493,
    "name": "Divide Nodes Into the Maximum Number of Groups",
    "slug": "divide-nodes-into-the-maximum-number-of-groups",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "dfs", "bipartite"],
    "difficulty": "hard",
    "time_complexity": "O(N * (N + M))",
    "space_complexity": "O(N + M)",
    "description": "Find the maximum number of groups nodes can be divided into such that no two nodes in the same group are adjacent, which is equivalent to the maximum distance from any node to any other node in a bipartite graph.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the maximum number of groups nodes can be divided into.
    
    The problem is equivalent to finding the maximum shortest path distance 
    between any two nodes in the graph. Since the graph must be bipartite 
    to allow such grouping, we first check for bipartiteness. If not 
    bipartite, return -1. Otherwise, the answer is max(BFS_depth) + 1.

    Args:
        n: The number of nodes in the graph.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        The maximum number of groups possible, or -1 if the graph is not bipartite.

    Examples:
        >>> solve(4, [[1, 2], [2, 3], [3, 4], [4, 1]])
        2
        >>> solve(3, [[1, 2], [2, 3], [3, 1]])
        -1
    """
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Step 1: Check if the graph is bipartite using BFS/DFS coloring
    # A graph is bipartite if and only if it contains no odd cycles.
    colors = [0] * (n + 1)  # 0: uncolored, 1: color A, -1: color B
    for i in range(1, n + 1):
        if colors[i] == 0:
            stack = [(i, 1)]
            colors[i] = 1
            while stack:
                curr, color = stack.pop()
                for neighbor in adj[curr]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -color
                        stack.append((neighbor, -color))
                    elif colors[neighbor] == color:
                        return -1

    # Step 2: Find the maximum shortest path distance (diameter)
    # Since N is small (up to 500), we can run BFS from every node.
    max_distance = 0
    
    for start_node in range(1, n + 1):
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = [start_node]
        head = 0
        
        while head < len(queue):
            u = queue[head]
            head += 1
            
            for v in adj[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    max_distance = max(max_distance, distances[v])
                    queue.append(v)
                    
    # The number of groups is the maximum distance + 1
    # (e.g., distance 0 means 1 group, distance 1 means 2 groups)
    return max_distance + 1
