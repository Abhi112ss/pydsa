METADATA = {
    "id": 530,
    "name": "Minimum Absolute Difference in BST",
    "slug": "minimum_absolute_difference_in_bst",
    "category": "binary_tree",
    "aliases": [],
    "tags": ["dfs", "in_order_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the minimum absolute difference between values of any two nodes in a BST.",
}


from typing import Optional


class TreeNode:
    """Binary tree node definition."""
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val: int = val
        self.left: Optional["TreeNode"] = left
        self.right: Optional["TreeNode"] = right


def solve(root: Optional[TreeNode]) -> int:
    """Calculate the minimum absolute difference between values of any two nodes in a BST.

    Args:
        root: The root node of the binary search tree.

    Returns:
        The smallest absolute difference between values of any two nodes.

    Examples:
        >>> node = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
        >>> solve(node)
        1
        >>> node2 = TreeNode(1, None, TreeNode(3, TreeNode(2), None))
        >>> solve(node2)
        1
    """
    # In-order traversal yields node values in ascending order for a BST.
    stack: list[TreeNode] = []
    current_node: Optional[TreeNode] = root
    previous_value: Optional[int] = None
    minimum_difference: int = 2**31 - 1  # large initial value

    while stack or current_node:
        # Reach the leftmost node of the current subtree.
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        # Process node at the top of the stack.
        current_node = stack.pop()
        if previous_value is not None:
            # Update the minimum difference using consecutive values.
            current_difference = current_node.val - previous_value
            if current_difference < minimum_difference:
                minimum_difference = current_difference
        previous_value = current_node.val

        # Move to the right subtree.
        current_node = current_node.right

    return minimum_difference