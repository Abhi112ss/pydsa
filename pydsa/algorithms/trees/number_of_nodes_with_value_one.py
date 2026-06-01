METADATA = {
    "id": 2445,
    "name": "Number of Nodes With Value One",
    "slug": "number-of-nodes-with-value-one",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "bfs", "trees"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Count the number of nodes in a tree that have a value of one.",
}

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> int:
    """
    Counts the number of nodes in a binary tree that have a value of 1.

    Args:
        root: The root node of the binary tree.

    Returns:
        The total count of nodes where node.val == 1.

    Examples:
        >>> root = TreeNode(1, TreeNode(0), TreeNode(1))
        >>> solve(root)
        2
        >>> root = TreeNode(0, TreeNode(0), TreeNode(0))
        >>> solve(root)
        0
    """
    if not root:
        return 0

    count = 0
    stack = [root]

    # Perform an iterative DFS to avoid recursion depth issues in large trees
    while stack:
        current_node = stack.pop()

        # Increment count if the current node's value is exactly 1
        if current_node.val == 1:
            count += 1

        # Push children to the stack for further traversal
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return count
