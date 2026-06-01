METADATA = {
    "id": 133,
    "name": "Clone Graph",
    "slug": "clone-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Create a deep copy of a connected undirected graph.",
}

class Node:
    def __init__(self, val: int = 0, neighbors: list['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def solve(node: Node) -> Node:
    """
    Args:
        node: The root node of the graph to clone.

    Returns:
        The root node of the newly cloned graph.
    """
    if not node:
        return None

    visited_clones = {}

    def traverse(current_node: Node) -> Node:
        if current_node in visited_clones:
            return visited_clones[current_node]

        clone = Node(current_node.val)
        visited_clones[current_node] = clone

        for neighbor in current_node.neighbors:
            clone.neighbors.append(traverse(neighbor))

        return clone

    return traverse(node)