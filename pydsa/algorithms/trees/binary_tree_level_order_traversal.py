METADATA = {
    "id": 102,
    "name": "Binary Tree Level Order Traversal",
    "slug": "binary-tree-level-order-traversal",
    "category": "Trees",
    "aliases": [],
    "tags": ["bfs", "queue", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the level order traversal of its nodes' values.",
}

from collections import deque
from typing import Optional, List


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs a Breadth-First Search (BFS) to traverse a binary tree level by level.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of lists, where each inner list contains the values of nodes at a specific level.

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        [[3], [9, 20], [15, 7]]
    """
    if not root:
        return []

    result: List[List[int]] = []
    # Use a deque for O(1) popleft operations
    queue: deque[TreeNode] = deque([root])

    while queue:
        # The number of elements currently in the queue represents the size of the current level
        level_size = len(queue)
        current_level_values: List[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level_values.append(node.val)

            # Add children to the queue for the next level processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level_values)

    return result
