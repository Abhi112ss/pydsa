METADATA = {
    "id": 124,
    "name": "Binary Tree Maximum Path Sum",
    "slug": "binary-tree-maximum-path-sum",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree", "depth-first-search"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the maximum path sum in a binary tree where a path can be any sequence of nodes from some starting node to any node in the tree along the parent-child connections.",
}

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> int:
    """
    Calculates the maximum path sum in a binary tree.

    A path is defined as any sequence of nodes from some starting node to any node 
    in the tree along the parent-child connections. The path does not need to 
    pass through the root.

    Args:
        root: The root node of the binary tree.

    Returns:
        The maximum path sum found in the tree.

    Examples:
        >>> root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        42
        >>> root = TreeNode(1)
        >>> solve(root)
        1
    """
    # Initialize with a very small number to handle trees with only negative values
    max_sum = float('-inf')

    def get_max_gain(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0

        # Recursively find the maximum contribution from left and right subtrees.
        # If a subtree returns a negative sum, we ignore it (take 0) to maximize the path.
        left_gain = max(get_max_gain(node.left), 0)
        right_gain = max(get_max_gain(node.right), 0)

        # The price of a new path would be the current node's value plus both gains.
        # This represents a path that "peaks" at the current node.
        current_path_sum = node.val + left_gain + right_gain

        # Update the global maximum if the path through this node is better.
        max_sum = max(max_sum, current_path_sum)

        # For the parent call, we can only return the maximum path that 
        # extends through one of the children to maintain a valid path structure.
        return node.val + max(left_gain, right_gain)

    get_max_gain(root)
    return int(max_sum)
