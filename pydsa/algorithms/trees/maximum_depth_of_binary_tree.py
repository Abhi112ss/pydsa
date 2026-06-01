METADATA = {
    "id": 104,
    "name": "Maximum Depth of Binary Tree",
    "slug": "maximum-depth-of-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "recursion", "tree", "binary tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the length of the longest path from the root node down to the farthest leaf node in a binary tree.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the maximum depth of a binary tree using a depth-first search approach.

    Args:
        root: The root node of the binary tree.

    Returns:
        The maximum depth (number of nodes along the longest path from root to leaf).

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        3
        >>> solve(TreeNode(1))
        1
        >>> solve(None)
        0
    """
    # Base case: if the node is None, the depth is 0
    if not root:
        return 0

    # Recursively find the depth of the left and right subtrees
    left_depth = solve(root.left)
    right_depth = solve(root.right)

    # The depth of the current node is 1 (itself) plus the maximum of its children's depths
    return max(left_depth, right_depth) + 1
