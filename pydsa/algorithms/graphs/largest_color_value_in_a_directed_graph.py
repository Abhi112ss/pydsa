METADATA = {
    "id": 1857,
    "name": "Largest Color Value in a Directed Graph",
    "slug": "largest-color-value-in-a-directed-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["topological_sort", "dp", "graphs", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Find the maximum number of nodes of the same color on any path in a directed graph, returning -1 if a cycle exists.",
}

from collections import deque

def solve(number_of_nodes: int, color_array: list[int], edges: list[list[int]]) -> int:
    """
    Finds the largest color value in a directed graph using topological sort and DP.

    Args:
        number_of_nodes: The total number of nodes in the graph.
        color_array: A list where color_array[i] is the color of node i.
        edges: A list of directed edges where edges[i] = [u, v] means u -> v.

    Returns:
        The maximum count of any single color on any path, or -1 if a cycle is detected.

    Examples:
        >>> solve(4, [1, 1, 2, 2], [[0, 1], [1, 2], [2, 3]])
        2
        >>> solve(3, [1, 2, 1], [[0, 1], [1, 2], [2, 0]])
        -1
    """
    # Build adjacency list and calculate in-degrees for topological sort
    adj_list: list[list[int]] = [[] for _ in range(number_of_nodes)]
    in_degree: list[int] = [0] * number_of_nodes
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    # dp[node][color] stores the max count of 'color' on a path ending at 'node'
    # To optimize space, we only track colors that actually appear in the graph.
    # However, since we need to track counts for all colors per node, 
    # we use a list of dictionaries to save space on sparse color distributions.
    dp: list[dict[int, int]] = [{} for _ in range(number_of_nodes)]
    
    queue: deque[int] = deque()
    for i in range(number_of_nodes):
        if in_degree[i] == 0:
            queue.append(i)
            # Initialize DP for starting nodes
            dp[i][color_array[i]] = 1

    processed_nodes_count = 0
    max_color_value = 0

    while queue:
        u = queue.popleft()
        processed_nodes_count += 1
        
        # Update the global maximum based on the current node's DP state
        if dp[u]:
            max_color_value = max(max_color_value, max(dp[u].values()))

        for v in adj_list[u]:
            # Propagate color counts from u to v
            # We must ensure v's DP state includes the max counts from u
            v_color = color_array[v]
            
            # Copy existing counts from u to v to maintain path history
            # We only need to update v's counts for colors present in u or v's own color
            for color, count in dp[u].items():
                dp[v][color] = max(dp[v].get(color, 0), count)
            
            # Increment the count for the color of node v itself
            dp[v][v_color] = dp[v].get(v_color, 0) + 1

            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # If processed_nodes_count < number_of_nodes, a cycle exists
    if processed_nodes_count < number_of_nodes:
        return -1

    return max_color_value
