METADATA = {
    "id": 108,
    "name": "Convert Sorted Array to Binary Search Tree",
    "slug": "convert-sorted-array-to-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary_search"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(log n)",
    "description": "Convert a sorted integer array into a height-balanced binary search tree.",
}

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(nums: list[int]) -> Optional[TreeNode]:
    """
    Converts a sorted array into a height-balanced Binary Search Tree (BST).

    To maintain balance, the middle element of the current subarray is always 
    selected as the root. This ensures that the number of nodes in the left 
    and right subtrees differs by at most one.

    Args:
        nums: A list of integers sorted in ascending order.

    Returns:
        The root node of the constructed height-balanced BST.

    Examples:
        >>> nums = [-10, -3, 0, 5, 9]
        >>> root = solve(nums)
        >>> # The resulting tree is balanced.
    """

    def build_bst_recursive(left_index: int, right_index: int) -> Optional[TreeNode]:
        # Base case: if the range is invalid, return None
        if left_index > right_index:
            return None

        # Choose the middle element to ensure the tree remains balanced
        mid_index = (left_index + right_index) // 2
        root_node = TreeNode(nums[mid_index])

        # Recursively build the left and right subtrees
        # The left subtree uses elements to the left of the middle
        root_node.left = build_bst_recursive(left_index, mid_index - 1)
        # The right subtree uses elements to the right of the middle
        root_node.right = build_bst_recursive(mid_index + 1, right_index)

        return root_node

    return build_bst_recursive(0, len(nums) - 1)
