METADATA = {
    "id": 783,
    "name": "Minimum Distance Between BST Nodes",
    "slug": "minimum-distance-between-bst-nodes",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "in_order_traversal", "binary_search_tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the minimum absolute difference between the values of any two different nodes in a Binary Search Tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Args:
        root: The root node of a Binary Search Tree.

    Returns:
        The minimum absolute difference between any two nodes in the tree.
    """
    min_difference = float('inf')
    previous_value = None

    def in_order_traversal(node: TreeNode) -> None:
        nonlocal min_difference, previous_value

        if not node:
            return

        in_order_traversal(node.left)

        if previous_value is not None:
            min_difference = min(min_difference, node.val - previous_value)
        
        previous_value = node.val

        in_order_traversal(node.right)

    in_order_traversal(root)
    return int(min_difference)