METADATA = {
    "id": 1602,
    "name": "Find Nearest Right Node in Binary Tree",
    "slug": "find-nearest-right-node-in-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["bfs", "trees", "binary-tree", "level-order-traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
    "description": "Find the rightmost node at each level of a binary tree.",
}

from collections import deque
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> list[int]:
    """
    Finds the values of the rightmost nodes at each level of a binary tree using BFS.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of integers representing the values of the rightmost nodes at each level.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
        >>> solve(root)
        [1, 3, 6]
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        >>> solve(root)
        [1, 3, 5]
    """
    if not root:
        return []

    result = []
    # Use a queue for level-order traversal (BFS)
    queue = deque([root])

    while queue:
        level_size = len(queue)
        
        # The last element in the current queue level will be the rightmost node
        for i in range(level_size):
            current_node = queue.popleft()
            
            # If this is the last node in the current level, record its value
            if i == level_size - 1:
                result.append(current_node.val)
            
            # Add children to the queue for the next level
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return result
