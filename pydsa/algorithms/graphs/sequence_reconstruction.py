METADATA = {
    "id": 444,
    "name": "Sequence Reconstruction",
    "slug": "sequence-reconstruction",
    "category": "Graph",
    "aliases": [],
    "tags": ["topological_sort", "bfs", "dfs", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Determine if a unique shortest common supersequence can be reconstructed from a given sequence of sequences.",
}

def solve(sequence: list[int], seqs: list[list[int]]) -> bool:
    """
    Determines if the given sequence is the unique shortest common supersequence 
    of all sequences in seqs using topological sort.

    Args:
        sequence: The target sequence to reconstruct.
        seqs: A list of sequences that define the ordering constraints.

    Returns:
        True if the sequence is the unique shortest common supersequence, False otherwise.

    Examples:
        >>> solve([1, 2, 3], [[1, 2], [1, 3], [2, 3]])
        True
        >>> solve([1, 2, 3], [[1, 2], [1, 3]])
        False
    """
    # Build adjacency list and in-degree map
    adj: dict[int, set[int]] = {}
    in_degree: dict[int, int] = {}
    nodes: set[int] = set()

    # Initialize graph structures
    for seq in seqs:
        for val in seq:
            nodes.add(val)
            if val not in adj:
                adj[val] = set()
            if val not in in_degree:
                in_degree[val] = 0

    # Populate edges and in-degrees
    for seq in seqs:
        for i in range(len(seq) - 1):
            u, v = seq[i], seq[i + 1]
            if v not in adj[u]:
                adj[u].add(v)
                in_degree[v] += 1

    # The sequence must contain exactly the same elements as the graph nodes
    if nodes != set(sequence) or len(sequence) != len(nodes):
        return False

    # Kahn's algorithm for topological sort
    # A unique topological sort exists if and only if at every step 
    # there is exactly one node with an in-degree of 0.
    queue: list[int] = [node for node in nodes if in_degree[node] == 0]
    reconstructed_sequence: list[int] = []

    while queue:
        # If there's more than one choice, the reconstruction is not unique
        if len(queue) > 1:
            return False
        
        current = queue.pop(0)
        reconstructed_sequence.append(current)

        for neighbor in adj[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if the reconstructed sequence matches the input sequence
    return reconstructed_sequence == sequence
