METADATA = {
    "id": 3054,
    "name": "Binary Tree Nodes",
    "slug": "binary-tree-nodes",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Calculate the total number of nodes in a binary tree using depth-first search.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the total number of nodes in a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The total count of nodes in the tree.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        3
        >>> solve(None)
        0
    """
    # Base case: if the current node is None, it contributes 0 to the count
    if root is None:
        return 0

    # Recursive step: 1 (current node) + nodes in left subtree + nodes in right subtree
    left_count = solve(root.left)
    right_count = solve(root.right)

    return 1 + left_count + right_count
