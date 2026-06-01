METADATA = {
    "id": 559,
    "name": "Maximum Depth of N-ary Tree",
    "slug": "maximum_depth_of_n_ary_tree",
    "category": "Tree",
    "aliases": ["n-ary tree", "nary tree", "multiway tree"],
    "tags": ["dfs", "bfs"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the maximum depth of an N-ary tree using DFS or BFS traversal.",
}

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def solve(root: Node | None) -> int:
    """
    Compute the maximum depth of an N-ary tree.

    Args:
        root (Node | None): The root node of the N-ary tree.

    Returns:
        int: The maximum depth of the tree.

    Examples:
        >>> root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        >>> solve(root)
        3
        >>> solve(None)
        0
    """
    if root is None:
        return 0

    # Base case: leaf node has depth 1
    if not root.children:
        return 1

    # Recursively find the maximum depth among all children
    max_child_depth = 0
    for child in root.children:
        child_depth = solve(child)
        if child_depth > max_child_depth:
            max_child_depth = child_depth

    # The depth of this node is 1 + max depth of its children
    return 1 + max_child_depth