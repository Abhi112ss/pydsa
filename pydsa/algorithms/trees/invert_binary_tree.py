METADATA = {
    "id": 226,
    "name": "Invert Binary Tree",
    "slug": "invert_binary_tree",
    "category": "Algorithms",
    "aliases": ["invert-binary-tree", "mirror-binary-tree", "flip-binary-tree"],
    "tags": ["tree", "recursion", "dfs", "bfs"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Invert a binary tree by swapping the left and right children of every node.",
}

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Invert a binary tree by recursively swapping left and right children of every node.

    Args:
        root: The root node of the binary tree to invert.

    Returns:
        The root node of the inverted binary tree.

    Examples:
        >>> # Tree:     4          Inverted:     4
        >>> #          / \\                   / \\
        #         2   7                 7   2
        >>> #        / \\               / \\
        #       1   3             3   1
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        >>> inverted = solve(root)
        >>> inverted.val
        4
        >>> inverted.left.val
        7
        >>> inverted.right.val
        2
        >>> inverted.right.left.val
        3
        >>> inverted.right.right.val
        1

        >>> solve(None) is None
        True
    """
    # Base case: empty node, nothing to invert
    if root is None:
        return None

    # Recursively invert the left and right subtrees first
    inverted_left = solve(root.left)
    inverted_right = solve(root.right)

    # Swap the left and right children
    root.left = inverted_right
    root.right = inverted_left

    return root