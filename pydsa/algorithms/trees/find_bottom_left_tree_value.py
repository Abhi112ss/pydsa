METADATA = {
    "id": 513,
    "name": "Find Bottom Left Tree Value",
    "slug": "find-bottom-left-tree-value",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "dfs", "tree_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
    "description": "Find the value of the leftmost node in the last row of a binary tree.",
}

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> int:
    """
    Finds the value of the leftmost node in the last row of a binary tree.

    The algorithm uses a modified Breadth-First Search (BFS). By processing 
    nodes from right to left at each level, the very last node dequeued 
    is guaranteed to be the bottom-leftmost node.

    Args:
        root: The root node of the binary tree.

    Returns:
        The integer value of the bottom-leftmost node.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
        >>> solve(root)
        4
    """
    if not root:
        raise ValueError("The tree root cannot be None.")

    # Use a queue for level-order traversal
    queue: deque[TreeNode] = deque([root])
    current_node: TreeNode = root

    while queue:
        # Pop the current node from the front
        current_node = queue.popleft()

        # To ensure the last node visited is the leftmost one in the bottom row,
        # we add the RIGHT child first, then the LEFT child.
        # This way, the traversal moves from right to left across each level.
        if current_node.right:
            queue.append(current_node.right)
        if current_node.left:
            queue.append(current_node.left)

    # After the loop, current_node holds the last node processed in the BFS
    return current_node.val
