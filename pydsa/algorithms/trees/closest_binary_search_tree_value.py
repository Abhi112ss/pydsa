METADATA = {
    "id": 270,
    "name": "Closest Binary Search Tree Value",
    "slug": "closest_binary_search_tree_value",
    "category": "Trees",
    "aliases": ["closest_bst_value", "closest_value_bst"],
    "tags": ["binary_search_tree", "binary_search", "trees"],
    "difficulty": "medium",
    "time_complexity": "O(h)",
    "space_complexity": "O(1)",
    "description": "Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode, target: float) -> int:
    """
    Find the value in the BST that is closest to the target.

    Args:
        root: The root node of the BST.
        target: The target value to find the closest node value to.

    Returns:
        The value in the BST that is closest to the target.

    Examples:
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3), TreeNode(5, None, TreeNode(6)))
        >>> solve(root, 3.5)
        4
    """
    closest = root.val
    current = root

    while current:
        # Update closest if current node is closer to target
        if abs(current.val - target) < abs(closest - target):
            closest = current.val

        # Navigate left or right based on target comparison
        if target < current.val:
            current = current.left
        else:
            current = current.right

    return closest