METADATA = {
    "id": 235,
    "name": "Lowest Common Ancestor of a Binary Search Tree",
    "slug": "lowest-common-ancestor-of-a-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "bst", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(h)",
    "space_complexity": "O(1)",
    "description": "Find the lowest common ancestor of two given nodes in a binary search tree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree.

    In a BST, for any node, all nodes in its left subtree have smaller values, 
    and all nodes in its right subtree have larger values. The LCA is the 
    first node encountered while traversing from the root where the two 
    target nodes split (one goes left, one goes right) or one node is the 
    ancestor of the other.

    Args:
        root: The root node of the binary search tree.
        p: The first target node.
        q: The second target node.

    Returns:
        The TreeNode that is the lowest common ancestor of p and q.

    Examples:
        >>> root = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(1), TreeNode(3))), TreeNode(8, TreeNode(5), TreeNode(7)))
        >>> p, q = root.left, root.right # p=2, q=8
        >>> solve(root, p, q)
        <TreeNode object at ...> (node with val 6)
    """
    current = root

    while current:
        # If both p and q are smaller than current, LCA must be in the left subtree
        if p.val < current.val and q.val < current.val:
            current = current.left
        # If both p and q are larger than current, LCA must be in the right subtree
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            # We have found the split point:
            # 1. One node is on the left and one is on the right
            # 2. Or current is equal to p or q (one is the ancestor of the other)
            return current

    return None # Should not be reached given valid BST and node existence constraints