METADATA = {
    "id": 802,
    "name": "Find Eventual Safe States",
    "slug": "find-eventual-safe-states",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "topological_sort", "cycle_detection"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Find all nodes that are not part of a cycle and do not lead to a cycle.",
}

def solve(graph: list[list[int]]) -> list[int]:
    """
    Finds all nodes that are eventually safe. A node is safe if every possible 
    path starting from that node leads to a terminal node (a node with no outgoing edges).

    The algorithm uses Kahn's algorithm (topological sort) on the reversed graph.
    In the reversed graph, terminal nodes become nodes with zero in-degree.
    By iteratively removing nodes with zero in-degree, we identify all nodes 
    that are not part of a cycle and do not lead to one.

    Args:
        graph: A directed graph represented as an adjacency list where graph[i] 
               is a list of nodes that node i has a directed edge to.

    Returns:
        A sorted list of all safe nodes.

    Examples:
        >>> solve([[1,2],[2,3],[5],[0],[5],[],[]])
        [5, 6]
        >>> solve([[1],[2],[3],[0]])
        []
        >>> solve([[1,2],[2,3],[5],[0],[5],[],[]])
        [5, 6]
    """
    num_nodes = len(graph)
    # reversed_graph[u] will contain all nodes v such that there was an edge v -> u
    reversed_graph: list[list[int]] = [[] for _ in range(num_nodes)]
    # in_degree[u] will track the number of outgoing edges from u in the original graph
    out_degree: list[int] = [0] * num_nodes

    # Build the reversed graph and calculate original out-degrees
    for source_node in range(num_nodes):
        for target_node in graph[source_node]:
            reversed_graph[target_node].append(source_node)
            out_degree[source_node] += 1

    # A node is a "starting point" for topological sort if it has no outgoing edges (terminal)
    queue: list[int] = []
    for node in range(num_nodes):
        if out_degree[node] == 0:
            queue.append(node)

    safe_nodes_mask: list[bool] = [False] * num_nodes
    
    # Process nodes with zero out-degree using BFS (Kahn's approach)
    head = 0
    while head < len(queue):
        current_node = queue[head]
        head += 1
        safe_nodes_mask[current_node] = True
        
        # For every node that points to the current safe node
        for predecessor in reversed_graph[current_node]:
            # Reduce the out-degree of the predecessor
            out_degree[predecessor] -= 1
            # If all paths from predecessor now lead to safe nodes, it is safe
            if out_degree[predecessor] == 0:
                queue.append(predecessor)

    # Return all nodes marked as safe, sorted by index
    return [node for node in range(num_nodes) if safe_nodes_mask[node]]
