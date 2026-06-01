METADATA = {
    "id": 637,
    "name": "Average of Levels in Binary Tree",
    "slug": "average_of_levels_in_binary_tree",
    "category": "Algorithms",
    "aliases": ["average of levels in binary tree"],
    "tags": ["bfs", "dfs", "binary_tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.",
}

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> list[float]:
    """
    Compute the average value of nodes at each level of a binary tree using BFS.

    Args:
        root (Optional[TreeNode]): The root node of the binary tree.

    Returns:
        list[float]: A list of average values for each level.

    Examples:
        >>> # Example 1: [3,9,20,null,null,15,7]
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        [3.0, 14.5, 11.0]

        >>> # Example 2: [1,2,3,4,5,6,7]
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        >>> solve(root)
        [1.0, 2.5, 5.5]
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0

        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            # Enqueue children for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Calculate the average for this level
        result.append(level_sum / level_size)

    return result