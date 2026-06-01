METADATA = {
    "id": 107,
    "name": "Binary Tree Level Order Traversal II",
    "slug": "binary-tree-level-order-traversal-ii",
    "category": "Trees",
    "aliases": [],
    "tags": ["bfs", "queue", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the level order traversal of a binary tree's nodes' values from bottom to top.",
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
    Performs a level-order traversal of a binary tree and returns the values 
    from the bottom level to the top level.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of lists, where each inner list contains the values of nodes 
        at a specific level, ordered from bottom to top.

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        [[15, 7], [20], [3, 9]]
    """
    if not root:
        return []

    result: List[List[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        current_level_values: List[int] = []

        # Process all nodes currently in the queue for the current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level_values.append(node.val)

            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level_values)

    # Reverse the result list to achieve bottom-to-top order
    return result[::-1]
