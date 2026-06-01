METADATA = {
    "id": 590,
    "name": "N-ary Tree Postorder Traversal",
    "slug": "n_ary_tree_postorder_traversal",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "stack"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given the root of an n-ary tree, return the postorder traversal of its nodes' values.",
}


class Node:
    """Definition for a Node in an n-ary tree."""
    def __init__(self, val: int | None = None, children: list['Node'] | None = None):
        self.val = val
        self.children = children if children is not None else []


def solve(root: Node | None) -> list[int]:
    """
    Perform postorder traversal on an n-ary tree.

    Postorder traversal visits all children of a node (left to right)
    before visiting the node itself.

    Args:
        root: The root node of the n-ary tree.

    Returns:
        A list of node values in postorder traversal order.

    Examples:
        >>> # Tree: 1 -> [3, 2, 4], 3 -> [5, 6]
        >>> n5 = Node(5)
        >>> n6 = Node(6)
        >>> n3 = Node(3, [n5, n6])
        >>> n2 = Node(2)
        >>> n4 = Node(4)
        >>> root = Node(1, [n3, n2, n4])
        >>> solve(root)
        [5, 6, 3, 2, 4, 1]

        >>> solve(None)
        []
    """
    result: list[int] = []

    def postorder(node: Node | None) -> None:
        """Recursively traverse the tree in postorder."""
        if node is None:
            return
        # First, recursively visit all children from left to right
        for child in node.children:
            postorder(child)
        # Then, add the current node's value to the result
        result.append(node.val)

    postorder(root)
    return result