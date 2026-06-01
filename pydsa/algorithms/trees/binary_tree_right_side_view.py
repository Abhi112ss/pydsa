METADATA = {
    "id": 199,
    "name": "Binary Tree Right Side View",
    "slug": "binary_tree_right_side_view",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Given the root of a binary tree, return the values of the nodes visible from the right side, ordered from top to bottom.",
}

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> list[int]:
    """Return the right side view of a binary tree.

    Performs a level-order (BFS) traversal and records the last node
    encountered at each level, which corresponds to the rightmost visible node.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of node values visible from the right side, top to bottom.

    Examples:
        >>> # Tree: [1,2,3,null,5,null,4]
        >>> root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
        >>> solve(root)
        [1, 3, 4]

        >>> # Tree: [1,null,3]
        >>> root = TreeNode(1, None, TreeNode(3))
        >>> solve(root)
        [1, 3]

        >>> solve(None)
        []
    """
    if root is None:
        return []

    result: list[int] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        # Process all nodes at the current level
        for index in range(level_size):
            current_node = queue.popleft()
            # The last node in this level is the rightmost visible one
            if index == level_size - 1:
                result.append(current_node.val)
            # Enqueue children for the next level
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

    return result