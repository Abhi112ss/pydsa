METADATA = {
    "id": 101,
    "name": "Symmetric Tree",
    "slug": "symmetric-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "bfs", "recursion", "binary tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if a binary tree is a mirror of itself.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> bool:
    """
    Determines if a binary tree is symmetric around its center.

    Args:
        root: The root node of the binary tree.

    Returns:
        True if the tree is symmetric, False otherwise.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, None, TreeNode(4)))
        >>> solve(root)
        True
        >>> root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2))
        >>> solve(root)
        False
    """
    if not root:
        return True

    def is_mirror(left_node: TreeNode | None, right_node: TreeNode | None) -> bool:
        """
        Helper function to check if two subtrees are mirror images of each other.
        """
        # If both nodes are null, they are symmetric
        if not left_node and not right_node:
            return True
        
        # If only one node is null, or values differ, they are not symmetric
        if not left_node or not right_node or left_node.val != right_node.val:
            return False

        # To be a mirror:
        # 1. Left child of left subtree must match right child of right subtree (outer)
        # 2. Right child of left subtree must match left child of right subtree (inner)
        return (is_mirror(left_node.left, right_node.right) and 
                is_mirror(left_node.right, right_node.left))

    return is_mirror(root.left, root.right)
