METADATA = {
    "id": 285,
    "name": "Inorder Successor in BST",
    "slug": "inorder-successor-in-bst",
    "category": "Tree",
    "aliases": [],
    "tags": ["binary_search_tree", "dfs", "tree_traversal"],
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

def solve(root: TreeNode, p: TreeNode) -> TreeNode:
    """
    Finds the inorder successor of a given node in a Binary Search Tree.

    The inorder successor is the node with the smallest key greater than p.val.
    If p is the largest node in the tree, there is no successor.

    Args:
        root: The root node of the Binary Search Tree.
        p: The target node whose successor we want to find.

    Returns:
        The TreeNode that is the inorder successor of p, or None if no successor exists.

    Examples:
        >>> root = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(4, TreeNode(None, None, TreeNode(5))))
        >>> p = root.left.right # Node with value 2
        >>> solve(root, p)
        <TreeNode object at ...> # Node with value 3
    """
    successor = None
    current = root

    while current:
        # If the current node's value is greater than p's value, 
        # it is a potential successor. We move left to find a smaller value 
        # that is still greater than p.
        if current.val > p.val:
            successor = current
            current = current.left
        # If the current node's value is less than or equal to p's value,
        # the successor must be in the right subtree.
        else:
            current = current.right

    return successor