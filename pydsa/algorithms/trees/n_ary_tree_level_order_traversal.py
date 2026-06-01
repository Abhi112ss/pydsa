METADATA = {
    "id": 429,
    "name": "N-ary Tree Level Order Traversal",
    "slug": "nary_tree_level_order_traversal",
    "category": "Tree",
    "aliases": ["level order traversal n-ary tree", "bfs n-ary tree"],
    "tags": ["bfs", "queue"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given an n-ary tree, return the level order traversal of its nodes' values.",
}

from collections import deque
from typing import Optional


class Node:
    """Definition for a Node in an N-ary tree."""
    def __init__(self, val: int = 0, children: Optional[list] = None):
        self.val = val
        self.children = children if children is not None else []


def solve(root: Optional[Node]) -> list[list[int]]:
    """Perform level order traversal on an N-ary tree.

    Uses a queue to process nodes level by level, iterating through the list
    of children for each node.

    Args:
        root: The root node of the N-ary tree.

    Returns:
        A list of lists, where each inner list contains the values of nodes
        at that level.

    Examples:
        >>> # Tree: 1 -> [3, 2, 4], 3 -> [5, 6]
        >>> root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        >>> solve(root)
        [[1], [3, 2, 4], [5, 6]]
    """
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            # Add all children of the current node to the queue
            for child in node.children:
                queue.append(child)

        result.append(current_level)

    return result