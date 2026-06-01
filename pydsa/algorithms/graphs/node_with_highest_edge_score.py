METADATA = {
    "id": 2374,
    "name": "Node With Highest Edge Score",
    "slug": "node-with-highest-edge-score",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "array"],
    "difficulty": "easy",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the node with the highest edge score, where the score is the sum of the degrees of its adjacent nodes.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Finds the node with the highest edge score in an undirected graph.
    
    The edge score of a node is defined as the sum of the degrees of all 
    nodes connected to it by an edge.

    Args:
        n: The number of nodes in the graph (nodes are labeled 0 to n-1).
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        The smallest index of the node with the highest edge score. 
        If multiple nodes have the same highest score, return the smallest index.

    Examples:
        >>> solve(4, [[0,1],[1,2],[2,3],[3,0],[0,2]])
        0
        >>> solve(3, [[0,1],[1,2]])
        1
    """
    # Step 1: Calculate the degree of every node
    # The degree is the number of edges connected to a node.
    degrees = [0] * n
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1

    # Step 2: Calculate the edge score for each node
    # The edge score is the sum of the degrees of its neighbors.
    edge_scores = [0] * n
    for u, v in edges:
        # Since it's an undirected graph, an edge (u, v) contributes 
        # the degree of v to u's score, and the degree of u to v's score.
        edge_scores[u] += degrees[v]
        edge_scores[v] += degrees[u]

    # Step 3: Find the node with the maximum score
    # We iterate through the scores and keep track of the max score and its index.
    max_score = -1
    best_node = -1
    
    for node_index in range(n):
        if edge_scores[node_index] > max_score:
            max_score = edge_scores[node_index]
            best_node = node_index
            
    return best_node
