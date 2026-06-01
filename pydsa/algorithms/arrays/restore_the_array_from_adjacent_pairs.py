METADATA = {
    "id": 1743,
    "name": "Restore the Array From Adjacent Pairs",
    "slug": "restore-the-array-from-adjacent-pairs",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "adjacency_list", "dfs", "hash-table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a list of pairs representing adjacent elements in an array, reconstruct the original array.",
}

def solve(pairs: list[list[int]]) -> list[int]:
    """
    Reconstructs the original array from a list of adjacent pairs.

    The problem can be modeled as finding a path in a graph where each element 
    is a node and each pair is an edge. Since the array is a linear sequence, 
    the graph is a simple path. The endpoints of the array will have a degree of 1.

    Args:
        pairs: A list of integer pairs representing adjacent elements.

    Returns:
        The reconstructed array.

    Examples:
        >>> solve([[2,1],[3,4],[4,2],[3,5]])
        [1, 2, 4, 3, 5]
        >>> solve([[1,2],[2,3],[3,4]])
        [1, 2, 3, 4]
    """
    from collections import defaultdict

    # Build an adjacency list to represent the graph
    adj_list = defaultdict(list)
    for u, v in pairs:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Find an endpoint: an element that appears in only one pair (degree 1)
    start_node = None
    for node in adj_list:
        if len(adj_list[node]) == 1:
            start_node = node
            break

    # Traverse the path starting from the endpoint
    reconstructed_array = []
    current_node = start_node
    previous_node = None

    # We iterate exactly N times (where N is the number of elements)
    # Since it's a simple path, we just move to the neighbor that isn't the previous node
    while len(reconstructed_array) < len(pairs) + 1:
        reconstructed_array.append(current_node)
        
        # Find the next neighbor that is not the one we just came from
        neighbors = adj_list[current_node]
        next_node = None
        for neighbor in neighbors:
            if neighbor != previous_node:
                next_node = neighbor
                break
        
        # Update pointers for the next iteration
        previous_node = current_node
        current_node = next_node
        
        # If we reach a dead end (the other endpoint), break
        if current_node is None:
            break

    return reconstructed_array
