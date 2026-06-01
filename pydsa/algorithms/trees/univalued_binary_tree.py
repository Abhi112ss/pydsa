METADATA = {
    "id": 965,
    "name": "Univalued Binary Tree",
    "slug": "univalued_binary_tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "bfs"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Check if all nodes in a binary tree have the same value.",
}


class TreeNode:
    """Binary tree node definition used by LeetCode."""
    def __init__(self, val: int = 0, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def solve(root: TreeNode | None) -> bool:
    """Determine whether a binary tree is univalued.

    Args:
        root: The root node of the binary tree, or None for an empty tree.

    Returns:
        True if every node in the tree contains the same value as the root,
        otherwise False.

    Examples:
        >>> root = TreeNode(1, TreeNode(1), TreeNode(1))
        >>> solve(root)
        True

        >>> root = TreeNode(1, TreeNode(2), TreeNode(1))
        >>> solve(root)
        False
    """
    if root is None:
        return True

    target_value: int = root.val
    stack: list[TreeNode] = [root]

    while stack:
        current_node = stack.pop()
        # If any node differs from the target value, the tree is not univalued.
        if current_node.val != target_value:
            return False
        if current_node.right is not None:
            stack.append(current_node.right)
        if current_node.left is not None:
            stack.append(current_node.left)

    return True