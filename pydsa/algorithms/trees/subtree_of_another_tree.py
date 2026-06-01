METADATA = {
    "id": 572,
    "name": "Subtree of Another Tree",
    "slug": "subtree_of_another_tree",
    "category": "Tree",
    "aliases": ["subtree of another tree", "is subtree"],
    "tags": ["dfs", "recursion", "binary_tree"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(h)",
    "description": "Given two binary trees, determine if the second tree is a subtree of the first tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode, sub_root: TreeNode) -> bool:
    """
    Determine if sub_root is a subtree of root.

    Args:
        root: The main binary tree.
        sub_root: The subtree to search for.

    Returns:
        True if sub_root is a subtree of root, False otherwise.

    Examples:
        >>> # Example 1: sub_root is a subtree
        >>> root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        >>> sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
        >>> solve(root, sub_root)
        True

        >>> # Example 2: sub_root is not a subtree
        >>> root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0)), TreeNode(5))
        >>> sub_root = TreeNode(4, TreeNode(1), TreeNode(2))
        >>> solve(root, sub_root)
        False
    """
    if not root:
        return False
    # Check if the current node matches the subtree
    if is_same_tree(root, sub_root):
        return True
    # Recursively check left and right subtrees
    return solve(root.left, sub_root) or solve(root.right, sub_root)


def is_same_tree(node1: TreeNode, node2: TreeNode) -> bool:
    """
    Check if two binary trees are identical.

    Args:
        node1: First binary tree node.
        node2: Second binary tree node.

    Returns:
        True if both trees are identical, False otherwise.
    """
    if not node1 and not node2:
        return True
    if not node1 or not node2:
        return False
    if node1.val != node2.val:
        return False
    # Recursively check left and right subtrees
    return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)