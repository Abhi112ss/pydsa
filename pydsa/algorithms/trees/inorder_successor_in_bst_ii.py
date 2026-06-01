METADATA = {
    "id": 510,
    "name": "Inorder Successor in BST II",
    "slug": "inorder-successor-in-bst-ii",
    "category": "Tree",
    "aliases": [],
    "tags": ["bst", "tree_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(h)",
    "space_complexity": "O(1)",
    "description": "Find the inorder successor of a given node in a Binary Search Tree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, p: TreeNode | None) -> TreeNode | None:
    """
    Finds the inorder successor of node p in a Binary Search Tree.

    The inorder successor is the node with the smallest key greater than p.val.
    If p has a right child, the successor is the leftmost node in that right subtree.
    Otherwise, the successor is the lowest ancestor of p such that p is in the 
    left subtree of that ancestor.

    Args:
        root: The root of the Binary Search Tree.
        p: The target node for which to find the successor.

    Returns:
        The inorder successor node, or None if no successor exists.

    Examples:
        >>> root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(5))
        >>> p = root.left.right  # Node with value 2
        >>> solve(root, p)
        <TreeNode object at ...> (Node with value 3)
    """
    if not root or not p:
        return None

    successor = None
    current = root

    while current:
        # If current value is greater than p, current could be the successor.
        # We record it and move left to see if there's a smaller value still > p.
        if current.val > p.val:
            successor = current
            current = current.left
        # If current value is less than or equal to p, the successor must be 
        # in the right subtree.
        else:
            current = current.right

    return successor
