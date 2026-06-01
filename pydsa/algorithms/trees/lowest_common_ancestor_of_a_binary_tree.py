METADATA = {
    "id": 236,
    "name": "Lowest Common Ancestor of a Binary Tree",
    "slug": "lowest-common-ancestor-of-a-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "recursion", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the lowest common ancestor of two given nodes in a binary tree.",
}

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solve(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """
    Finds the lowest common ancestor (LCA) of two nodes in a binary tree.

    The LCA is defined as the lowest node in the tree that has both p and q 
    as descendants (where we allow a node to be a descendant of itself).

    Args:
        root: The root node of the binary tree.
        p: The first target node.
        q: The second target node.

    Returns:
        The TreeNode that is the lowest common ancestor, or None if not found.

    Examples:
        >>> root = TreeNode(3)
        >>> root.left = TreeNode(5)
        >>> root.right = TreeNode(1)
        >>> root.left.left = TreeNode(6)
        >>> root.left.right = TreeNode(2)
        >>> solve(root, root.left.left, root.left.right)
        <TreeNode object at ...> (Node with value 5)
    """
    if not root or root == p or root == q:
        return root

    # Recurse into left and right subtrees
    left_result = solve(root.left, p, q)
    right_result = solve(root.right, p, q)

    # If both left and right recursive calls returned a non-None value,
    # it means p and q are located in different subtrees of the current node.
    # Therefore, the current node is the LCA.
    if left_result and right_result:
        return root

    # If only one side returned a non-None value, it means both nodes 
    # (or the one found so far) are located in that specific subtree.
    return left_result if left_result else right_result