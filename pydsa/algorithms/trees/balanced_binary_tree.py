METADATA = {
    "id": 110,
    "name": "Balanced Binary Tree",
    "slug": "balanced-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if a binary tree is height-balanced, where the depth of the two subtrees of every node never differs by more than one.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> bool:
    """
    Determines if a binary tree is height-balanced using a bottom-up DFS approach.

    A tree is balanced if for every node, the height difference between its 
    left and right subtrees is at most 1, and both subtrees are themselves balanced.

    Args:
        root: The root node of the binary tree.

    Returns:
        True if the tree is balanced, False otherwise.

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        True
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(3)))
        >>> solve(root)
        False
    """

    def check_height(node: TreeNode | None) -> int:
        """
        Helper function that returns the height of the tree if balanced, 
        or -1 if any subtree is unbalanced.
        """
        if not node:
            return 0

        # Recursively get the height of the left subtree
        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        # Recursively get the height of the right subtree
        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        # Key logic: If the current node is unbalanced, propagate -1 upwards.
        # Otherwise, return the actual height of the current node.
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1

    # If the helper returns -1, it means an imbalance was detected somewhere.
    return check_height(root) != -1