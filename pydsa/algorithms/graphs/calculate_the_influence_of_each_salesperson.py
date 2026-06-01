METADATA = {
    "id": 2372,
    "name": "Calculate the Influence of Each Salesperson",
    "slug": "calculate-the-influence-of-each-salesperson",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "graph", "directed graph"],
    "difficulty": "medium",
    "time_complexity": "O(N * (N + E))",
    "space_complexity": "O(N + E)",
    "description": "Calculate the number of reachable nodes for each node in a directed graph.",
}

def solve(salespeople: list[list[int]], relationships: list[list[int]]) -> list[int]:
    """
    Calculates the influence of each salesperson by counting how many other 
    salespeople they can reach in the directed graph.

    Args:
        salespeople: A list of integers representing the IDs of the salespeople.
        relationships: A list of pairs [u, v] representing a directed relationship 
                       from salesperson u to salesperson v.

    Returns:
        A list of integers where the i-th element is the influence of the 
        i-th salesperson in the input 'salespeople' list.

    Examples:
        >>> solve([1, 2, 3], [[1, 2], [2, 3]])
        [2, 1, 0]
        >>> solve([1, 2, 3], [[1, 2], [1, 3]])
        [2, 0, 0]
    """
    # Map salesperson ID to their index in the input list for O(1) lookup
    id_to_index = {salesperson_id: i for i, salesperson_id in enumerate(salespeople)}
    n = len(salespeople)
    
    # Build adjacency list using indices instead of IDs
    adj = [[] for _ in range(n)]
    for u, v in relationships:
        # Only add relationship if both salespeople exist in the input list
        if u in id_to_index and v in id_to_index:
            adj[id_to_index[u]].append(id_to_index[v])

    results = [0] * n

    def dfs(start_node: int) -> int:
        """Performs DFS to count reachable nodes from start_node."""
        visited = [False] * n
        stack = [start_node]
        visited[start_node] = True
        count = 0
        
        while stack:
            current = stack.pop()
            for neighbor in adj[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += 1
                    stack.append(neighbor)
        return count

    # Calculate influence for each salesperson using DFS
    for i in range(n):
        results[i] = dfs(i)

    return results
