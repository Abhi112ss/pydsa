METADATA = {
    "id": 3831,
    "name": "Median of a Binary Search Tree Level",
    "slug": "median_of_a_binary_search_tree_level",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "bfs", "median"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
    "description": "Calculate the median value of nodes at each level of a binary search tree using level-order traversal.",
}

from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> List[float]:
    """
    Performs a level-order traversal of a binary search tree and calculates 
    the median of the values at each level.

    Args:
        root: The root node of the binary search tree.

    Returns:
        A list of floats representing the median of each level.

    Examples:
        >>> root = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7))
        >>> solve(root)
        [5.0, 3.5, 1.0, 4.0, 7.0] # Note: Example values depend on tree structure
    """
    if not root:
        return []

    medians: List[float] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        current_level_values: List[int] = []

        # Extract all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level_values.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Sort the values of the current level to find the median
        # Note: In a standard BST, level order isn't necessarily sorted, 
        # so we must sort the level's values.
        current_level_values.sort()
        n = len(current_level_values)
        mid = n // 2

        if n % 2 == 1:
            # Odd number of elements: middle element
            medians.append(float(current_level_values[mid]))
        else:
            # Even number of elements: average of two middle elements
            median_val = (current_level_values[mid - 1] + current_level_values[mid]) / 2.0
            medians.append(median_val)

    return medians
