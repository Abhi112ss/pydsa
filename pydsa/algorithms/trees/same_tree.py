METADATA = {
    "id": 100,
    "name": "Same Tree",
    "slug": "same-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "recursion"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if two binary trees are structurally identical and have the same node values.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(p: TreeNode | None, q: TreeNode | None) -> bool:
    """
    Determines if two binary trees are the same.

    Args:
        p: The root of the first binary tree.
        q: The root of the second binary tree.

    Returns:
        True if the trees are identical, False otherwise.

    Examples:
        >>> p = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> q = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(p, q)
        True
        >>> p = TreeNode(1, TreeNode(2))
        >>> q = TreeNode(1, None, TreeNode(2))
        >>> solve(p, q)
        False
    """
    # Base Case 1: Both nodes are None, meaning we reached the end of both branches simultaneously
    if not p and not q:
        return True

    # Base Case 2: One node is None and the other isn't, or values differ
    if not p or not q or p.val != q.val:
        return False

    # Recursive Step: Check if left subtrees are identical AND right subtrees are identical
    return solve(p.left, q.left) and solve(p.right, q.right)