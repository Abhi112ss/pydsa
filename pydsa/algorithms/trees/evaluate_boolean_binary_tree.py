METADATA = {
    "id": 2331,
    "name": "Evaluate Boolean Binary Tree",
    "slug": "evaluate_boolean_binary_tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "trees", "binary-tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Evaluates a binary tree where internal nodes represent logical OR/AND and leaves represent boolean values.",
}


class TreeNode:
    """Binary tree node used by the evaluate function."""
    def __init__(self, val: int, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode | None) -> bool:
    """Evaluates a boolean binary tree.

    Args:
        root: The root node of the binary tree. Internal nodes have value 2 (OR) or
              3 (AND). Leaf nodes have value 0 (False) or 1 (True).

    Returns:
        The boolean result of evaluating the expression represented by the tree.

    Examples:
        >>> leaf_true = TreeNode(1)
        >>> leaf_false = TreeNode(0)
        >>> root = TreeNode(2, leaf_true, leaf_false)  # OR node
        >>> solve(root)
        True

        >>> root_and = TreeNode(3, leaf_true, leaf_false)  # AND node
        >>> solve(root_and)
        False
    """
    def evaluate(node: TreeNode) -> bool:
        # If the node is a leaf, directly return its boolean value.
        if node.left is None and node.right is None:
            return bool(node.val)

        # Recursively evaluate left and right subtrees first (post-order).
        left_result = evaluate(node.left) if node.left else False
        right_result = evaluate(node.right) if node.right else False

        # Apply the logical operator represented by the current node.
        if node.val == 2:  # OR operation
            return left_result or right_result
        else:  # node.val == 3, AND operation
            return left_result and right_result

    if root is None:
        return False
    return evaluate(root)