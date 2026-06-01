METADATA = {
    "id": 563,
    "name": "Binary Tree Tilt",
    "slug": "binary-tree-tilt",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "binary_tree", "recursion"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Calculate the sum of absolute differences between each node's value and the sum of its children's values.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Args:
        root: The root of the binary tree.

    Returns:
        The total tilt of the binary tree.
    """
    total_tilt = 0

    def calculate_subtree_sum(node: TreeNode) -> int:
        nonlocal total_tilt
        if not node:
            return 0

        left_sum = calculate_subtree_sum(node.left)
        right_sum = calculate_subtree_sum(node.right)

        tilt_value = abs((left_sum + right_sum) - node.val)
        total_tilt += tilt_value

        return node.val + left_sum + right_sum

    calculate_subtree_sum(root)
    return total_tilt