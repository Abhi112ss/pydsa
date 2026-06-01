METADATA = {
    "id": 2192,
    "name": "All Ancestors of a Node in a Directed Acyclic Graph",
    "slug": "all-ancestors-of-a-node-in-a-directed-acyclic-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graph", "topological sort"],
    "difficulty": "medium",
    "time_complexity": "O(n * (n + e))",
    "space_complexity": "O(n^2)",
    "description": "Find all ancestors for each node in a directed acyclic graph.",
}

def solve(edges: list[list[int]], n: int) -> list[list[int]]:
    """
    Finds all ancestors for each node in a Directed Acyclic Graph (DAG).

    An ancestor of a node is any node from which there is a path to that node.
    The result for each node should be a sorted list of its ancestors.

    Args:
        edges: A list of directed edges where edges[i] = [u, v] means u -> v.
        n: The number of nodes in the graph.

    Returns:
        A list of lists where the i-th list contains all ancestors of node i,
        sorted in ascending order.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 5], [1, 5]], 6)
        [[ ], [ ], [1], [2], [1, 2, 3], [1, 2, 3]]
    """
    # Build adjacency list representing the graph
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)

    # Initialize the result matrix with empty sets to avoid duplicates
    # Using sets allows O(1) insertion and automatic handling of multiple paths
    ancestors_sets: list[set[int]] = [set() for _ in range(n)]

    def dfs(start_node: int, current_node: int):
        """
        Performs DFS to find all nodes reachable from start_node.
        Every node reachable from start_node (except start_node itself)
        will have start_node as an ancestor.
        """
        for neighbor in adj[current_node]:
            # If we haven't recorded this start_node as an ancestor of neighbor yet
            if start_node not in ancestors_sets[neighbor]:
                ancestors_sets[neighbor].add(start_node)
                dfs(start_node, neighbor)

    # For every node, treat it as a potential ancestor and traverse the graph
    # to mark all nodes it can reach.
    for i in range(n):
        dfs(i, i)

    # Convert sets to sorted lists as required by the problem
    result: list[list[int]] = []
    for s in ancestors_sets:
        result.append(sorted(list(s)))

    return result
