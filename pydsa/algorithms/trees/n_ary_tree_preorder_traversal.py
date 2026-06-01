METADATA = {
    "id": 589,
    "name": "N-ary Tree Preorder Traversal",
    "slug": "n_ary_tree_preorder_traversal",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "stack"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the preorder traversal of an N-ary tree.",
}


class Node:
    """Definition for a Node in an N-ary tree."""
    def __init__(self, val: int, children: list['Node'] | None = None):
        self.val = val
        self.children = children if children is not None else []


def solve(root: Node | None) -> list[int]:
    """Perform a preorder traversal of an N-ary tree.

    Args:
        root: The root node of the N-ary tree, or None for an empty tree.

    Returns:
        A list of node values visited in preorder (node first, then children).

    Examples:
        >>> root = Node(1, [Node(2), Node(3, [Node(5), Node(6)]), Node(4)])
        >>> solve(root)
        [1, 2, 3, 5, 6, 4]
        >>> solve(None)
        []
    """
    if root is None:
        return []

    traversal: list[int] = []
    stack: list[Node] = [root]

    while stack:
        current_node = stack.pop()
        traversal.append(current_node.val)  # visit the node first

        # push children onto stack in reverse order so leftmost child is processed first
        for child in reversed(current_node.children):
            stack.append(child)

    return traversal