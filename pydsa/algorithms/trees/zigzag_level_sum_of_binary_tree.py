METADATA = {
    "id": 3902,
    "name": "Zigzag Level Sum of Binary Tree",
    "slug": "zigzag_level_sum_of_binary_tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
    "description": "Calculate the sum of nodes at each level of a binary tree, where the direction of traversal alternates between left-to-right and right-to-left.",
}

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> list[int]:
    """
    Calculates the sum of node values at each level of a binary tree using a zigzag pattern.

    Note: While the problem asks for a zigzag traversal, the sum of a level remains 
    the same regardless of the order (left-to-right vs right-to-left). However, 
    to strictly follow the zigzag logic for potential variations (like returning 
    node values instead of sums), we implement the level-order traversal.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of integers representing the sum of nodes at each level.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        >>> solve(root)
        [1, 5, 9]
    """
    if not root:
        return []

    level_sums = []
    queue = deque([root])
    # Flag to track if we are on an even or odd level for zigzag logic
    # Though for sums, order doesn't change the result, we maintain the concept.
    is_left_to_right = True

    while queue:
        level_size = len(queue)
        current_level_sum = 0
        
        # Process all nodes currently in the queue (one full level)
        for _ in range(level_size):
            node = queue.popleft()
            current_level_sum += node.val

            # Standard BFS: add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        level_sums.append(current_level_sum)
        # Flip the direction flag for the next level
        is_left_to_right = not is_left_to_right

    return level_sums
