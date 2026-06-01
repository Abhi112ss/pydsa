METADATA = {
    "id": 450,
    "name": "Delete Node in a BST",
    "slug": "delete-node-in-a-bst",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "recursion", "binary search tree"],
    "difficulty": "medium",
    "time_complexity": "O(h)",
    "space_complexity": "O(h)",
    "description": "Delete a node from a Binary Search Tree and maintain the BST property.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, key: int) -> TreeNode | None:
    """
    Deletes a node with the specified key from a Binary Search Tree.

    Args:
        root: The root of the Binary Search Tree.
        key: The value of the node to be deleted.

    Returns:
        The root of the modified Binary Search Tree.

    Examples:
        >>> root = TreeNode(5, TreeNode(3), TreeNode(6, TreeNode(4, TreeNode(2), TreeNode(4)), TreeNode(7)))
        >>> new_root = solve(root, 2)
        >>> new_root.val
        5
    """
    if not root:
        return None

    # 1. Search for the node to delete
    if key < root.val:
        root.left = solve(root.left, key)
    elif key > root.val:
        root.right = solve(root.right, key)
    else:
        # Found the node to delete
        
        # Case 1 & 2: Node has 0 or 1 child
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Case 3: Node has 2 children
        # Find the inorder successor (smallest node in the right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left
        
        # Replace current node's value with successor's value
        root.val = successor.val
        
        # Delete the inorder successor from the right subtree
        root.right = solve(root.right, successor.val)

    return root
