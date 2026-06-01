METADATA = {
    "id": 99,
    "name": "Recover Binary Search Tree",
    "slug": "recover-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "binary search tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Two nodes of a Binary Search Tree have been swapped by mistake. Recover the tree without changing its structure.",
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
        The root of the recovered binary search tree.
    """
    first_node = None
    second_node = None
    previous_node = None

    def inorder_traversal(current_node: TreeNode) -> None:
        nonlocal first_node, second_node, previous_node

        if not current_node:
            return

        inorder_traversal(current_node.left)

        if previous_node and previous_node.val > current_node.val:
            if not first_node:
                first_node = previous_node
            second_node = current_node

        previous_node = current_node

        inorder_traversal(current_node.right)

    inorder_traversal(root)

    if first_node and second_node:
        first_node.val, second_node.val = second_node.val, first_node.val

    return root