METADATA = {
    "id": 897,
    "name": "Increasing Order Search Tree",
    "slug": "increasing-order-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "inorder_traversal", "binary_tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Convert a binary search tree into a skewed tree where nodes are linked in increasing order.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> TreeNode:
    """
    Args:
        root: The root of the binary search tree.

    Returns:
        The root of the new skewed tree in increasing order.
    """
    dummy_head = TreeNode(0)
    current_node = dummy_head

    def inorder_traversal(node: TreeNode) -> None:
        nonlocal current_node
        if not node:
            return

        inorder_traversal(node.left)

        node.left = None
        node.right = None
        current_node.right = node
        current_node = node

        inorder_traversal(node.right)

    inorder_traversal(root)
    return dummy_head.right