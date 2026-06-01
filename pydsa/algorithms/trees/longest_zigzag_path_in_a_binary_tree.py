METADATA = {
    "id": 1372,
    "name": "Longest ZigZag Path in a Binary Tree",
    "slug": "longest_zigzag_path_in_a_binary_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the length of the longest path in a binary tree where each step alternates between left and right directions.",
}

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> int:
    """
    Finds the length of the longest ZigZag path in a binary tree.

    A ZigZag path is defined by alternating between left and right child moves.
    The length is defined as the number of edges in the path.

    Args:
        root: The root node of the binary tree.

    Returns:
        The length of the longest ZigZag path.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(4, TreeNode(5), None))
        >>> solve(root)
        2
    """
    max_zigzag_length = 0

    def dfs(node: TreeNode, go_left: bool, current_length: int) -> None:
        """
        Recursive helper to traverse the tree and track ZigZag lengths.

        Args:
            node: The current node being visited.
            go_left: Boolean indicating if the next move should be to the left child.
            current_length: The current length of the ZigZag path ending at this node.
        """
        nonlocal max_zigzag_length
        if not node:
            return

        # Update the global maximum length found so far
        max_zigzag_length = max(max_zigzag_length, current_length)

        if go_left:
            # If we were supposed to go left:
            # 1. Successfully ZigZagged: move left, increment length, next move must be right.
            if node.left:
                dfs(node.left, False, current_length + 1)
            # 2. Failed to ZigZag: we can't go left if we were supposed to go right, 
            # but here 'go_left' is the requirement. If we go right instead, 
            # we start a new path from this node.
            if node.right:
                dfs(node.right, True, 1)
        else:
            # If we were supposed to go right:
            # 1. Successfully ZigZagged: move right, increment length, next move must be left.
            if node.right:
                dfs(node.right, True, current_length + 1)
            # 2. Failed to ZigZag: start a new path by going left.
            if node.left:
                dfs(node.left, False, 1)

    # Initial calls: starting from root, we can either try to go left or right.
    # We treat the first move as a fresh start (length 0).
    if root:
        # Try starting a path by moving left
        if root.left:
            dfs(root.left, False, 1)
        # Try starting a path by moving right
        if root.right:
            dfs(root.right, True, 1)

    return max_zigzag_length

# Note: The logic in the DFS can be simplified to:
# For every node, we have two choices:
# 1. Continue the ZigZag from the parent.
# 2. Start a new ZigZag from the current node.
# The implementation above handles this by exploring both directions at every node.