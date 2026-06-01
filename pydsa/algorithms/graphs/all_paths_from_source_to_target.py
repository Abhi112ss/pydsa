METADATA = {
    "id": 797,
    "name": "All Paths From Source to Target",
    "slug": "all-paths-from-source-to-target",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "backtracking", "dag"],
    "difficulty": "medium",
    "time_complexity": "O(2^n * n)",
    "space_complexity": "O(2^n * n)",
    "description": "Find all possible paths from node 0 to node n-1 in a directed acyclic graph.",
}

def solve(graph: list[list[int]]) -> list[list[int]]:
    """
    Finds all possible paths from node 0 to node n-1 in a Directed Acyclic Graph (DAG).

    Args:
        graph: A list of lists where graph[i] is a list of all nodes you can visit 
               directly from node i.

    Returns:
        A list of all possible paths from node 0 to node n-1.

    Examples:
        >>> solve([[1,2],[3],[3],[]])
        [[0, 1, 3], [0, 2, 3]]
        >>> solve([[1], [2], [3], []])
        [[0, 1, 2, 3]]
    """
    num_nodes = len(graph)
    target_node = num_nodes - 1
    all_paths: list[list[int]] = []

    def backtrack(current_node: int, current_path: list[int]) -> None:
        # If we reached the target node, add a copy of the current path to results
        if current_node == target_node:
            all_paths.append(list(current_path))
            return

        # Explore all neighbors of the current node
        for neighbor in graph[current_node]:
            # Choose: add neighbor to path
            current_path.append(neighbor)
            
            # Explore: recurse with the neighbor
            backtrack(neighbor, current_path)
            
            # Un-choose: backtrack by removing the neighbor to explore other branches
            current_path.pop()

    # Start the DFS from the source node (0)
    backtrack(0, [0])
    
    return all_paths
