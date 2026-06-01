METADATA = {
    "id": 111,
    "name": "Minimum Depth of Binary Tree",
    "slug": "minimum-depth-of-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "bfs", "binary tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum depth of a binary tree, which is the number of nodes along the shortest path from the root node down to the nearest leaf node.",
}

from collections import deque
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> int:
    """
    Calculates the minimum depth of a binary tree using Breadth-First Search (BFS).

    BFS is optimal here because it explores the tree level by level. The first 
    leaf node encountered is guaranteed to be at the minimum depth, allowing 
    us to exit early without traversing the entire tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The minimum depth of the tree (number of nodes along the shortest path).

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        2
        >>> root = TreeNode(1, None, TreeNode(2))
        >>> solve(root)
        2
    """
    if not root:
        return 0

    # Queue stores tuples of (node, current_depth)
    queue: deque[tuple[TreeNode, int]] = deque([(root, 1)])

    while queue:
        current_node, depth = queue.popleft()

        # A leaf node is defined as a node with no children
        if not current_node.left and not current_node.right:
            return depth

        # Add children to the queue to continue level-order traversal
        if current_node.left:
            queue.append((current_node.left, depth + 1))
        if current_node.right:
            queue.append((current_node.right, depth + 1))

    return 0