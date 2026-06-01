METADATA = {
    "id": 222,
    "name": "Count Complete Tree Nodes",
    "slug": "count_complete_tree_nodes",
    "category": "Tree",
    "aliases": [],
    "tags": ["binary_search", "trees", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(log^2 n)",
    "space_complexity": "O(log n)",
    "description": "Count the number of nodes in a complete binary tree by leveraging the complete tree property to skip subtrees.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode) -> int:
    """
    Count the number of nodes in a complete binary tree.

    Uses the complete tree property: if left and right depths are equal,
    the left subtree is a perfect binary tree (2^h - 1 nodes).
    Otherwise, recurse into both subtrees.

    Args:
        root: The root node of the complete binary tree.

    Returns:
        The total number of nodes in the tree.

    Examples:
        >>> # Tree: [1,2,3,4,5,6]
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        >>> solve(root)
        6

        >>> # Tree: [1]
        >>> solve(TreeNode(1))
        1

        >>> # Empty tree
        >>> solve(None)
        0
    """
    if root is None:
        return 0

    # Compute left depth by traversing left children
    left_depth = 0
    node = root
    while node:
        left_depth += 1
        node = node.left

    # Compute right depth by traversing right children
    right_depth = 0
    node = root
    while node:
        right_depth += 1
        node = node.right

    # If left and right depths are equal, it's a perfect binary tree
    if left_depth == right_depth:
        return (1 << left_depth) - 1  # 2^h - 1 nodes in a perfect tree

    # Otherwise, recurse into both subtrees plus the root
    return 1 + solve(root.left) + solve(root.right)