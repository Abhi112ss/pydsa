METADATA = {
    "id": 998,
    "name": "Maximum Binary Tree II",
    "slug": "maximum-binary-tree-ii",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(h)",
    "space_complexity": "O(h)",
    "description": "Insert a new value into a maximum binary tree such that the tree property is maintained.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, val: int) -> TreeNode:
    """
    Inserts a value into a maximum binary tree.

    Args:
        root: The root of the existing maximum binary tree.
        val: The integer value to be inserted.

    Returns:
        The root of the updated maximum binary tree.
    """
    if root is None:
        return TreeNode(val)

    if val > root.val:
        new_node = TreeNode(val)
        new_node.left = root
        return new_node

    root.right = solve(root.right, val)
    return root