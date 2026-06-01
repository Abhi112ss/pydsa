METADATA = {
    "id": 114,
    "name": "Flatten Binary Tree to Linked List",
    "slug": "flatten-binary-tree-to-linked-list",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Flatten a binary tree into a linked list in-place using the right child pointers.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> TreeNode:
    """
    Flattens a binary tree into a linked list in-place.

    Args:
        root: The root node of the binary tree.

    Returns:
        The root node of the flattened tree.
    """
    def flatten_recursive(node: TreeNode) -> TreeNode:
        if not node:
            return None
        
        if not node.left and not node.right:
            return node
        
        left_tail = flatten_recursive(node.left)
        right_tail = flatten_recursive(node.right)
        
        if node.left:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
            
        return right_tail if right_tail else left_tail

    if not root:
        return None
        
    flatten_recursive(root)
    return root