METADATA = {
    "id": 951,
    "name": "Flip Equivalent Binary Trees",
    "slug": "flip-equivalent-binary-trees",
    "category": "Tree",
    "aliases": [],
    "tags": ["recursion", "dfs", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if two binary trees are flip equivalent by checking if their structures match either directly or after flipping children.",
}

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """
    Determines if two binary trees are flip equivalent.
    
    Two binary trees are flip equivalent if they can be made identical by 
    flipping the left and right children of any number of nodes.

    Args:
        root1: The root node of the first binary tree.
        root2: The root node of the second binary tree.

    Returns:
        True if the trees are flip equivalent, False otherwise.

    Examples:
        >>> root1 = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> root2 = TreeNode(1, TreeNode(3), TreeNode(2))
        >>> solve(root1, root2)
        True
    """
    # Base Case: Both nodes are None, they are equivalent
    if not root1 and not root2:
        return True
    
    # If one is None or values differ, they cannot be equivalent
    if not root1 or not root2 or root1.val != root2.val:
        return False

    # Case 1: The children match without flipping (left-left and right-right)
    # Case 2: The children match with a flip (left-right and right-left)
    # We use short-circuiting OR to check both possibilities
    return (
        (solve(root1.left, root2.left) and solve(root1.right, root2.right)) or
        (solve(root1.left, root2.right) and solve(root1.right, root2.left))
    )
