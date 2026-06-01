METADATA = {
    "id": 662,
    "name": "Maximum Width of Binary Tree",
    "slug": "maximum-width-of-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "dfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum width of a binary tree, where the width is defined as the number of nodes between the leftmost and rightmost non-null nodes in a level, including null nodes.",
}

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> int:
    """
    Calculates the maximum width of a binary tree using a BFS approach with heap-based indexing.

    Args:
        root: The root node of the binary tree.

    Returns:
        The maximum width of the binary tree.

    Examples:
        >>> root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3, TreeNode(6))), TreeNode(2, None, TreeNode(7)))
        >>> solve(root)
        4
    """
    if not root:
        return 0

    max_width = 0
    # Queue stores tuples of (node, index)
    # We use heap-based indexing: left child is 2*i, right child is 2*i + 1
    queue: list[tuple[TreeNode, int]] = [(root, 0)]

    while queue:
        level_length = len(queue)
        # The width of the current level is the difference between the last and first index
        _, first_index = queue[0]
        _, last_index = queue[-1]
        max_width = max(max_width, last_index - first_index + 1)

        # Process all nodes at the current level to prepare the next level
        for _ in range(level_length):
            node, index = queue.pop(0)

            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))

    return max_width
