METADATA = {
    "id": 3319,
    "name": "K-th Largest Perfect Subtree Size in Binary Tree",
    "slug": "kth-largest-perfect-subtree-size-in-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "heaps"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the k-th largest size among all perfect subtrees in a given binary tree.",
}

from typing import Optional, List
import heapq

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode], k: int) -> int:
    """
    Finds the k-th largest size of a perfect subtree in the given binary tree.

    A perfect binary tree is a tree where all interior nodes have two children 
    and all leaves are at the same level.

    Args:
        root: The root of the binary tree.
        k: The rank (1-indexed) of the size to find.

    Returns:
        The size of the k-th largest perfect subtree, or -1 if fewer than k exist.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root, 1)
        1
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        >>> solve(root, 1)
        7
    """
    # This list will store the sizes of all identified perfect subtrees.
    perfect_subtree_sizes: List[int] = []

    def dfs(node: Optional[TreeNode]) -> tuple[bool, int]:
        """
        Post-order traversal to identify perfect subtrees.
        
        Returns:
            A tuple of (is_perfect, height) where height is the height of 
            the subtree if it is perfect, otherwise -1.
        """
        if not node:
            # Base case: An empty node is technically perfect with height 0.
            return True, 0

        left_perfect, left_height = dfs(node.left)
        right_perfect, right_height = dfs(node.right)

        # A subtree is perfect if:
        # 1. Both children are perfect subtrees.
        # 2. Both children have the same height.
        if left_perfect and right_perfect and left_height == right_height:
            current_height = left_height + 1
            # Size of a perfect binary tree of height h is 2^h - 1.
            # However, since we are calculating iteratively, 
            # size = 1 + size_left + size_right.
            # But we only need the height to determine the size.
            # Let's use the formula: size = (2^height) - 1.
            # To avoid floating point, we use bit shifting.
            size = (1 << current_height) - 1
            perfect_subtree_sizes.append(size)
            return True, current_height
        
        # If not perfect, return False and height -1 to signal failure to parent.
        return False, -1

    dfs(root)

    # If we found fewer than k perfect subtrees, return -1.
    if len(perfect_subtree_sizes) < k:
        return -1

    # Use a min-heap to find the k-th largest element efficiently.
    # We maintain a heap of size k.
    min_heap = []
    for size in perfect_subtree_sizes:
        if len(min_heap) < k:
            heapq.heappush(min_heap, size)
        else:
            if size > min_heap[0]:
                heapq.heapreplace(min_heap, size)

    return min_heap[0]
