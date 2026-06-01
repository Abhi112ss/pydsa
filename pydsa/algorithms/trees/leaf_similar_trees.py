METADATA = {
    "id": 872,
    "name": "Leaf-Similar Trees",
    "slug": "leaf_similar_trees",
    "category": "Tree",
    "aliases": ["leaf similar trees", "leaf sequence"],
    "tags": ["dfs", "tree_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n1 + n2)",
    "space_complexity": "O(h1 + h2)",
    "description": "Check if two binary trees are leaf-similar by comparing their leaf value sequences.",
}

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """Check if two binary trees are leaf-similar by comparing their leaf value sequences.

    Two binary trees are considered leaf-similar if their leaf value sequences
    (left-to-right order of leaf nodes) are identical.

    Args:
        root1: The root node of the first binary tree.
        root2: The root node of the second binary tree.

    Returns:
        True if both trees have identical leaf value sequences, False otherwise.

    Examples:
        >>> # Example 1: Both trees have leaf sequence [6, 7, 4, 9, 8]
        >>> tree1 = TreeNode(3,
        ...     TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        ...     TreeNode(1, TreeNode(9), TreeNode(8)))
        >>> tree2 = TreeNode(3,
        ...     TreeNode(5, TreeNode(6), TreeNode(7)),
        ...     TreeNode(1, TreeNode(4, TreeNode(9), TreeNode(8))))
        >>> solve(tree1, tree2)
        True

        >>> # Example 2: Different leaf sequences
        >>> tree3 = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> tree4 = TreeNode(1, TreeNode(3), TreeNode(2))
        >>> solve(tree3, tree4)
        False
    """

    def get_leaf_sequence(node: Optional[TreeNode]) -> list[int]:
        """Perform DFS to collect leaf node values in left-to-right order.

        Args:
            node: Current node being visited.

        Returns:
            List of leaf values in left-to-right order.
        """
        if node is None:
            return []

        # Base case: leaf node (no children)
        if node.left is None and node.right is None:
            return [node.val]

        # Recursive case: traverse left subtree first, then right subtree
        # This ensures left-to-right ordering of leaf values
        return get_leaf_sequence(node.left) + get_leaf_sequence(node.right)

    # Extract leaf sequences from both trees
    leaves1 = get_leaf_sequence(root1)
    leaves2 = get_leaf_sequence(root2)

    # Compare the two leaf sequences
    return leaves1 == leaves2