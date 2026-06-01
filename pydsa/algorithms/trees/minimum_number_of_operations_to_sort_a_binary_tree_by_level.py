METADATA = {
    "id": 2471,
    "name": "Minimum Number of Operations to Sort a Binary Tree by Level",
    "slug": "minimum-number-of-operations-to-sort-a-binary-tree-by-level",
    "category": "Trees",
    "aliases": [],
    "tags": ["bfs", "sorting", "cycle decomposition"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of swaps required to sort a binary tree level by level.",
}

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> int:
    """
    Calculates the minimum number of swaps needed to sort a binary tree level by level.

    The algorithm performs a Breadth-First Search (BFS) to extract the values 
    level by level into a flat list. It then calculates the minimum swaps 
    required to sort this list using cycle decomposition.

    Args:
        root: The root node of the binary tree.

    Returns:
        The minimum number of swaps required to sort the tree elements.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        0
        >>> root = TreeNode(3, TreeNode(1), TreeNode(2))
        >>> solve(root)
        2
    """
    if not root:
        return 0

    # Step 1: Perform BFS to collect elements level by level
    level_order_elements = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        level_order_elements.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # Step 2: Calculate minimum swaps using cycle decomposition
    # Create a list of (value, original_index) pairs
    indexed_elements = []
    for index, value in enumerate(level_order_elements):
        indexed_elements.append((value, index))

    # Sort the pairs by value to see where each element 'should' be
    indexed_elements.sort()

    visited = [False] * len(level_order_elements)
    swaps_count = 0

    for i in range(len(level_order_elements)):
        # If already visited or already in the correct position, skip
        if visited[i] or indexed_elements[i][1] == i:
            continue

        # Find the size of the cycle
        cycle_size = 0
        current_index = i
        
        while not visited[current_index]:
            visited[current_index] = True
            # Move to the index where the current element belongs
            current_index = indexed_elements[current_index][1]
            cycle_size += 1

        # A cycle of size K requires K-1 swaps to sort
        if cycle_size > 0:
            swaps_count += (cycle_size - 1)

    return swaps_count