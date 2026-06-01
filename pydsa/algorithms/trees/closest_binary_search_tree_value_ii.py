METADATA = {
    "id": 272,
    "name": "Closest Binary Search Tree Value II",
    "slug": "closest-binary-search-tree-value-ii",
    "category": "Trees",
    "aliases": [],
    "tags": ["binary_search_tree", "heap", "stack", "trees", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find k closest values in a Binary Search Tree to a target value.",
}

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode], k: int, target: float) -> list[int]:
    """
    Finds k values in a Binary Search Tree that are closest to a target value.

    The algorithm uses an in-order traversal to visit nodes in sorted order.
    A sliding window (implemented via a deque) maintains the k closest values
    encountered so far. Since the in-order traversal is monotonic, we can
    efficiently update the window by comparing the current node with the 
    oldest element in the window.

    Args:
        root: The root of the binary search tree.
        k: The number of closest values to return.
        target: The target value to compare against.

    Returns:
        A list of k integers representing the closest values to the target.

    Examples:
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(6)))
        >>> solve(root, 2, 3.7)
        [4, 3]
    """
    window = deque()
    stack = []
    current = root

    # Perform iterative in-order traversal to process nodes in sorted order
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        val = current.val

        # Maintain a sliding window of size k
        if len(window) < k:
            window.append(val)
        else:
            # If current value is closer to target than the oldest value in window,
            # replace the oldest value. Because in-order is sorted, once the 
            # difference starts increasing, we can stop.
            if abs(val - target) < abs(window[0] - target):
                window.popleft()
                window.append(val)
            else:
                # Since values are increasing, if this one isn't closer, 
                # subsequent ones won't be either.
                break
        
        current = current.right

    return list(window)
