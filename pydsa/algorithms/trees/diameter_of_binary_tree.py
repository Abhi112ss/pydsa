METADATA = {
    "id": 543,
    "name": "Diameter of Binary Tree",
    "slug": "diameter-of-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the length of the longest path between any two nodes in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Args:
        root: The root node of the binary tree.

    Returns:
        The diameter of the binary tree.
    """
    max_diameter = 0

    def calculate_depth(node: TreeNode) -> int:
        nonlocal max_diameter
        if not node:
            return 0

        left_depth = calculate_depth(node.left)
        right_depth = calculate_depth(node.right)

        max_diameter = max(max_diameter, left_depth + right_depth)

        return 1 + max(left_depth, right_depth)

    calculate_depth(root)
    return max_diameter