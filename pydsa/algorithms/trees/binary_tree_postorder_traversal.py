METADATA = {
    "id": 145,
    "name": "Binary Tree Postorder Traversal",
    "slug": "binary-tree-postorder-traversal",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "stack", "recursion", "binary-tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the postorder traversal of its nodes' values (Left, Right, Root).",
}

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> List[int]:
    """
    Performs a postorder traversal of a binary tree using an iterative approach.
    
    Postorder traversal visits nodes in the order: Left -> Right -> Root.
    The iterative approach uses a stack and a 'last visited' pointer to simulate 
    the call stack without recursion.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of integers representing the postorder traversal.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        [2, 3, 1]
    """
    if not root:
        return []

    result: List[int] = []
    stack: List[TreeNode] = [root]
    last_visited_node: Optional[TreeNode] = None

    while stack:
        current_node = stack[-1]

        # Check if we are moving down the tree or returning up from a child
        # We can only visit the current node if it has no children or we just finished visiting its right child
        is_left_child = current_node.left and current_node.left != last_visited_node
        is_right_child = current_node.right and current_node.right != last_visited_node

        if is_left_child or is_right_child:
            # If there is a left child and we haven't visited it, move left
            if current_node.left and current_node.left != last_visited_node:
                stack.append(current_node.left)
            # Otherwise, if there is a right child and we haven't visited it, move right
            elif current_node.right and current_node.right != last_visited_node:
                stack.append(current_node.right)
        else:
            # We have visited both children (or they don't exist), so process the root
            result.append(current_node.val)
            last_visited_node = stack.pop()

    return result

def solve_recursive(root: Optional[TreeNode]) -> List[int]:
    """
    Performs a postorder traversal of a binary tree using recursion.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of integers representing the postorder traversal.
    """
    result: List[int] = []

    def traverse(node: Optional[TreeNode]) -> None:
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)

    traverse(root)
    return result