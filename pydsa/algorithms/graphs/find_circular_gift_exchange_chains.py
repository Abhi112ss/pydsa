METADATA = {
    "id": 3401,
    "name": "Find Circular Gift Exchange Chains",
    "slug": "find_circular_gift_exchange_chains",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "cycle_detection", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify the lengths of all disjoint cycles in a functional graph where each node has exactly one outgoing edge.",
}

def solve(gifts: list[int]) -> list[int]:
    """
    Finds the lengths of all disjoint cycles in a functional graph.

    In a functional graph where every node has exactly one outgoing edge, 
    the graph consists of several components, each containing exactly one cycle.
    This function identifies the length of each cycle found.

    Args:
        gifts: A list of integers where gifts[i] is the index of the person 
               to whom person i gives a gift.

    Returns:
        A list of integers representing the lengths of all detected cycles, 
        sorted in non-decreasing order.

    Examples:
        >>> solve([1, 2, 0, 4, 3])
        [3, 2]
        >>> solve([1, 0, 3, 2])
        [2, 2]
    """
    n = len(gifts)
    visited = [False] * n
    cycle_lengths = []

    for i in range(n):
        if not visited[i]:
            # Track nodes in the current traversal to detect the cycle
            path_nodes = []
            current_node = i
            path_set = {}
            
            # Traverse until we hit a node already visited in this path 
            # or a node visited in a previous traversal
            while not visited[current_node]:
                path_set[current_node] = len(path_nodes)
                path_nodes.append(current_node)
                visited[current_node] = True
                current_node = gifts[current_node]
            
            # If the current_node is in path_set, we found a new cycle
            if current_node in path_set:
                cycle_start_index = path_set[current_node]
                cycle_len = len(path_nodes) - cycle_start_index
                cycle_lengths.append(cycle_len)
                
    # The problem asks for the lengths of the cycles found
    cycle_lengths.sort()
    return cycle_lengths
