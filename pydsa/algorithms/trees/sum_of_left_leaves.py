METADATA = {
    "id": 404,
    "name": "Sum of Left Leaves",
    "slug": "sum_of_left_leaves",
    "category": "Tree",
    "aliases": ["sum_left_leaves", "left_leaves_sum"],
    "tags": ["dfs", "bfs", "binary_tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the sum of all left leaves in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode) -> int:
    """
    Calculate the sum of all left leaves in a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The sum of values of all left leaves.

    Examples:
        >>> # Tree:    3
        >>> #         / \\
        >>> #        9   20
        >>> #           /  \\
        >>> #          15   7
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        24
        >>> # Tree: 1
        >>> root = TreeNode(1)
        >>> solve(root)
        0
    """
    if not root:
        return 0

    total_sum = 0
    # Use a stack with (node, is_left_child) tuples for iterative DFS
    stack = [(root, False)]

    while stack:
        current_node, is_left_child = stack.pop()

        # Check if this node is a left leaf (no children and is a left child)
        if is_left_child and not current_node.left and not current_node.right:
            total_sum += current_node.val

        # Push children onto the stack with appropriate flags
        if current_node.right:
            stack.append((current_node.right, False))
        if current_node.left:
            stack.append((current_node.left, True))

    return total_sum