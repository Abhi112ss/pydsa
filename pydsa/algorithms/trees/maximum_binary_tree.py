METADATA = {
    "id": 654,
    "name": "Maximum Binary Tree",
    "slug": "maximum-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "stack", "monotonic stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a maximum binary tree from an integer array where the root is the maximum element and subtrees are built recursively from the left and right partitions.",
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
    Constructs the Maximum Binary Tree using a monotonic decreasing stack in linear time.

    The algorithm maintains a stack of nodes such that their values are in strictly 
    decreasing order. For each new element, we pop elements smaller than it to 
    establish the new element as their parent, and the last popped element 
    becomes the new element's left child.

    Args:
        nums: A list of integers.

    Returns:
        The root of the constructed Maximum Binary Tree.

    Examples:
        >>> solve([3, 2, 1])
        TreeNode(3, left=TreeNode(2, left=TreeNode(1)))
        >>> solve([2, 2, 2])
        TreeNode(2, left=TreeNode(2, left=TreeNode(2)))
    """
    if not nums:
        return None

    stack: list[TreeNode] = []

    for num in nums:
        new_node = TreeNode(num)
        last_popped: Optional[TreeNode] = None

        # Maintain a monotonic decreasing stack.
        # When we find a larger element, the current element becomes the parent
        # of the elements smaller than it.
        while stack and stack[-1].val < num:
            last_popped = stack.pop()

        # The last element popped is the largest element smaller than 'num' 
        # that appeared before it, making it the left child.
        if last_popped:
            new_node.left = last_popped

        # If the stack is not empty, the current element is the right child 
        # of the element currently at the top of the stack.
        if stack:
            stack[-1].right = new_node

        stack.append(new_node)

    # The bottom-most element in the monotonic stack is the root of the tree.
    return stack[0] if stack else None
