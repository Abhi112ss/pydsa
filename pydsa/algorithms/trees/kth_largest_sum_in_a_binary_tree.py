METADATA = {
    "id": 2583,
    "name": "Kth Largest Sum in a Binary Tree",
    "slug": "kth_largest_sum_in_a_binary_tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "heap", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n log k)",
    "space_complexity": "O(n)",
    "description": "Find the kth largest subtree sum in a binary tree using post-order traversal and a min-heap.",
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
    Finds the kth largest subtree sum in a binary tree.

    Args:
        root: The root of the binary tree.
        k: The rank of the sum to find (1-indexed).

    Returns:
        The kth largest subtree sum. Returns -1 if there are fewer than k subtrees.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root, 2)
        3
    """
    # Min-heap to store the k largest sums encountered so far.
    # Using a min-heap of size k allows us to keep the largest elements 
    # at the top, where the smallest of the 'k largest' is at the root.
    min_heap: List[int] = []

    def post_order_traversal(node: Optional[TreeNode]) -> int:
        """
        Performs post-order traversal to calculate subtree sums.
        
        Args:
            node: Current node being visited.
            
        Returns:
            The sum of the subtree rooted at 'node'.
        """
        if not node:
            return 0

        # Calculate sum of left and right subtrees first (Post-order)
        left_sum = post_order_traversal(node.left)
        right_sum = post_order_traversal(node.right)
        
        current_subtree_sum = node.val + left_sum + right_sum

        # Maintain a min-heap of size k to track the k largest sums
        if len(min_heap) < k:
            heapq.heappush(min_heap, current_subtree_sum)
        elif current_subtree_sum > min_heap[0]:
            heapq.heapreplace(min_heap, current_subtree_sum)

        return current_subtree_sum

    post_order_traversal(root)

    # If the heap doesn't contain k elements, it means there were fewer than k subtrees
    if len(min_heap) < k:
        return -1

    # The root of the min-heap is the kth largest element
    return min_heap[0]
