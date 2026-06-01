METADATA = {
    "id": 2497,
    "name": "Maximum Star Sum of a Graph",
    "slug": "maximum-star-sum-of-a-graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Find the maximum star sum in a graph where a star sum is the value of a node plus the sum of its neighbors' values.",
}

def solve(edges: list[list[int]], values: list[int]) -> int:
    """
    Calculates the maximum star sum in a graph.
    
    A star sum for a node is defined as the value of the node plus the sum 
    of the values of its neighbors. To maximize this, we only include 
    neighbors that have a positive value.

    Args:
        edges: A list of undirected edges where edges[i] = [u, v].
        values: A list of integers representing the value of each node.

    Returns:
        The maximum star sum found in the graph.

    Examples:
        >>> solve([[0,1],[0,2],[1,2]], [1,2,3])
        6
        >>> solve([[0,1],[1,2],[2,3]], [1,2,3,4])
        9
    """
    n = len(values)
    # Adjacency list to store the graph
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    max_star_sum = float('-inf')

    for i in range(n):
        # Start with the value of the current center node
        current_star_sum = values[i]
        
        # To maximize the sum, we only add neighbors with positive values
        # We iterate through neighbors and greedily pick those that increase the sum
        for neighbor in adj[i]:
            neighbor_val = values[neighbor]
            if neighbor_val > 0:
                current_star_sum += neighbor_val
        
        # Update the global maximum
        if current_star_sum > max_star_sum:
            max_star_sum = current_star_sum

    return int(max_star_sum)
