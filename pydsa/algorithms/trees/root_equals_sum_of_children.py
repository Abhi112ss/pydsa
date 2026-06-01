METADATA = {
    "id": 2236,
    "name": "Root Equals Sum of Children",
    "slug": "root-equals-sum-of-children",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if the value of a root node is equal to the sum of its left and right child nodes.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> bool:
    """
    Args:
        root: The root node of a binary tree with exactly three nodes.

    Returns:
        True if the root's value equals the sum of its children's values, False otherwise.
    """
    return root.val == root.left.val + root.right.val