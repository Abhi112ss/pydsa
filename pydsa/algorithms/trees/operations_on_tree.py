METADATA = {
    "id": 1993,
    "name": "Operations on Tree",
    "slug": "operations_on_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Perform operations on a binary tree where nodes with value 0 are transformed to 1 and their descendants are updated, returning the total number of 1s.",
}

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> int:
    """
    Performs operations on a binary tree and returns the total number of nodes with value 1.
    
    The operation: if a node has value 0, it is changed to 1, and all its descendants 
    are also changed to 1. This is equivalent to saying if a node's ancestor was 
    already turned into a 1, this node becomes a 1 regardless of its original value.

    Args:
        root: The root of the binary tree.

    Returns:
        The total count of nodes that have a value of 1 after operations.

    Examples:
        >>> root = TreeNode(0, TreeNode(1, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(0)))
        >>> solve(root)
        6
    """
    total_ones = 0

    def dfs(node: Optional[TreeNode], is_descendant_of_zero: bool) -> None:
        nonlocal total_ones
        if not node:
            return

        # If an ancestor was 0, this node and all its children effectively become 1
        if is_descendant_of_zero or node.val == 0:
            current_is_one = True
        else:
            current_is_one = False

        if current_is_one:
            total_ones += 1

        # Pass the 'is_descendant_of_zero' flag down to children
        # If current node is 0 or an ancestor was 0, children are marked as descendants of 0
        dfs(node.left, current_is_one)
        dfs(node.right, current_is_one)

    dfs(root, False)
    return total_ones
