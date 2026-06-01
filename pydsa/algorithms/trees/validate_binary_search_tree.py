METADATA = {
    "id": 98,
    "name": "Validate Binary Search Tree",
    "slug": "validate-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "binary-search-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a given binary tree is a valid binary search tree.",
}

from typing import Optional

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> bool:
    """
    Validates if a binary tree satisfies the Binary Search Tree (BST) properties.
    
    A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

    Args:
        root: The root node of the binary tree.

    Returns:
        True if the tree is a valid BST, False otherwise.

    Examples:
        >>> root = TreeNode(2, TreeNode(1), TreeNode(3))
        >>> solve(root)
        True
        >>> root = TreeNode(5, TreeNode(1, None, TreeNode(4)), TreeNode(8, None, TreeNode(9)))
        >>> solve(root)
        False
    """
    
    def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
        """
        Helper function to perform a recursive DFS with range constraints.
        
        Args:
            node: The current node being inspected.
            low: The minimum allowed value for this node.
            high: The maximum allowed value for this node.
            
        Returns:
            True if the subtree rooted at 'node' is a valid BST within (low, high).
        """
        # An empty tree is a valid BST
        if not node:
            return True

        # The current node's value must be strictly between low and high
        if not (low < node.val < high):
            return False

        # Recursively check subtrees:
        # Left child must be in range (low, current_node_value)
        # Right child must be in range (current_node_value, high)
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))

    # Initialize with infinity to allow any integer value at the root
    return validate(root, float('-inf'), float('inf'))
