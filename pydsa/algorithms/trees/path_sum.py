METADATA = {
    "id": 112,
    "name": "Path Sum",
    "slug": "path-sum",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, target_sum: int) -> bool:
    """
    Determines if there is a root-to-leaf path in a binary tree where the 
    sum of the values along the path equals target_sum.

    Args:
        root: The root node of the binary tree.
        target_sum: The integer sum to search for.

    Returns:
        True if such a path exists, False otherwise.

    Examples:
        >>> root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(1), TreeNode(5))))
        >>> solve(root, 22)
        True
        >>> solve(root, 5)
        False
    """
    # Base case: If the node is None, no path exists through this branch
    if not root:
        return False

    # Subtract current node's value from the remaining sum required
    remaining_sum = target_sum - root.val

    # Check if we are at a leaf node (no children)
    if not root.left and not root.right:
        # If it's a leaf, the path is valid if the remaining sum is exactly 0
        return remaining_sum == 0

    # Recursively check the left and right subtrees
    # If either subtree returns True, a valid path exists
    return solve(root.left, remaining_sum) or solve(root.right, remaining_sum)