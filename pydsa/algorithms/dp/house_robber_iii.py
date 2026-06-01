METADATA = {
    "id": 337,
    "name": "House Robber III",
    "slug": "house-robber-iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "tree", "depth_first_search"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine the maximum amount of money you can rob from a collection of houses arranged in a binary tree structure, where you cannot rob two directly linked houses.",
}

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> int:
    """
    Calculates the maximum amount of money that can be robbed from the binary tree.

    The algorithm uses a post-order traversal (bottom-up) to compute two values for 
    each node: the maximum money if the node is robbed, and the maximum money if 
    the node is skipped.

    Args:
        root: The root node of the binary tree.

    Returns:
        The maximum amount of money that can be robbed.

    Examples:
        >>> root = TreeNode(3, TreeNode(2), TreeNode(3))
        >>> solve(root)
        4
        >>> root = TreeNode(2, TreeNode(3), TreeNode(3)
        >>> solve(root)
        4
    """
    if not root:
        return 0

    def dfs(node: Optional[TreeNode]) -> list[int]:
        """
        Performs a depth-first search to return a pair of values.

        Args:
            node: The current node being visited.

        Returns:
            A list of two integers: [rob_this_node, skip_this_node].
        """
        if not node:
            # Base case: if node is None, we can rob 0 or skip 0.
            return [0, 0]

        # Recurse down to the children first (Post-order traversal)
        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)

        # 1. If we rob this node, we MUST skip its direct children.
        # We take the 'skip' values from the children.
        rob_this_node = node.val + left_skip + right_skip

        # 2. If we skip this node, we can either rob or skip its children.
        # We take the maximum possible value from each child's subtree.
        skip_this_node = max(left_rob, left_skip) + max(right_rob, right_skip)

        return [rob_this_node, skip_this_node]

    # The result is the maximum of robbing the root or skipping the root.
    result_pair = dfs(root)
    return max(result_pair)
