METADATA = {
    "id": 103,
    "name": "Binary Tree Zigzag Level Order Traversal",
    "slug": "binary-tree-zigzag-level-order-traversal",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "queue", "stack", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the zigzag level order traversal of its nodes' values (i.e., from left to right, then right to left for the next level and alternate between).",
}

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs a zigzag level order traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of lists, where each inner list contains the values of a level 
        in zigzag order.

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        [[3], [20, 9], [15, 7]]
    """
    if not root:
        return []

    result: List[List[int]] = []
    queue: deque[TreeNode] = deque([root])
    # Flag to track if the current level should be processed left-to-right
    left_to_right: bool = True

    while queue:
        level_size = len(queue)
        # Use a deque for the current level to allow efficient O(1) prepending
        current_level: deque[int] = deque()

        for _ in range(level_size):
            node = queue.popleft()

            # If left_to_right is true, append to the end. 
            # If false, append to the front to simulate reversal.
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.appendleft(node.val)

            # Standard BFS: add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Convert the level deque to a list and add to final result
        result.append(list(current_level))
        # Flip the direction for the next level
        left_to_right = not left_to_right

    return result
