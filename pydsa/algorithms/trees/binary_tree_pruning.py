METADATA = {
    "id": 814,
    "name": "Binary Tree Pruning",
    "slug": "binary-tree-pruning",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Prune a binary tree such that all subtrees that do not contain a 1 are removed.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> TreeNode | None:
    """
    Prunes the binary tree to remove all subtrees that do not contain a 1.

    The algorithm uses a post-order traversal (bottom-up approach). A node is 
    kept if it has a value of 1 OR if any of its children (after pruning) 
    contain a 1.

    Args:
        root: The root of the binary tree.

    Returns:
        The root of the pruned binary tree, or None if the entire tree is pruned.

    Examples:
        >>> root = TreeNode(1, TreeNode(0, TreeNode(0, TreeNode(1)), TreeNode(1)), TreeNode(0, TreeNode(0, TreeNode(0)), TreeNode(1)))
        >>> solve(root)
        TreeNode(1, TreeNode(0, TreeNode(1), TreeNode(1)), TreeNode(0, TreeNode(1)))
    """
    if not root:
        return None

    # Perform post-order traversal: process children first
    root.left = solve(root.left)
    root.right = solve(root.right)

    # After children are processed, check if this node is a leaf and has value 0.
    # If it is a leaf and its value is 0, it means this entire subtree 
    # contains no 1s, so we prune it by returning None.
    if root.val == 0 and not root.left and not root.right:
        return None

    return root
