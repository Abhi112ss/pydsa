METADATA = {
    "id": 1022,
    "name": "Sum of Root To Leaf Binary Numbers",
    "slug": "sum_of_root_to_leaf_binary_numbers",
    "category": "binary_tree",
    "aliases": [],
    "tags": ["dfs", "binary_tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Calculate the sum of all root‑to‑leaf binary numbers represented by paths in a binary tree.",
}


from typing import Optional, List


class TreeNode:
    """Binary tree node definition."""
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> int:
    """Calculate the sum of all root‑to‑leaf binary numbers in a binary tree.

    Args:
        root: The root node of the binary tree. Each node's value is either 0 or 1.

    Returns:
        The integer sum of the binary numbers formed by each root‑to‑leaf path.

    Examples:
        >>> # Tree:      0
        >>> #           / \
        >>> #          1   0
        >>> #         / \ / \
        >>> #        0  1 0  1
        >>> node = TreeNode(0,
        ...     TreeNode(1, TreeNode(0), TreeNode(1)),
        ...     TreeNode(0, TreeNode(0), TreeNode(1))
        ... )
        >>> solve(node)
        22
    """
    if root is None:
        return 0

    total_sum = 0
    stack: List[tuple[TreeNode, int]] = [(root, root.val)]

    while stack:
        current_node, current_value = stack.pop()
        # If leaf, add its accumulated binary value to total_sum
        if current_node.left is None and current_node.right is None:
            total_sum += current_value
        # Push right child with updated binary value (shift left and add child.val)
        if current_node.right is not None:
            stack.append((current_node.right, (current_value << 1) | current_node.right.val))
        # Push left child with updated binary value
        if current_node.left is not None:
            stack.append((current_node.left, (current_value << 1) | current_node.left.val))

    return total_sum