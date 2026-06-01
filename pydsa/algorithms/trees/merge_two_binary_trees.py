METADATA = {
    "id": 617,
    "name": "Merge Two Binary Trees",
    "slug": "merge-two-binary-trees",
    "category": "Trees",
    "aliases": [],
    "tags": ["recursion", "dfs", "binary_tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Merge two binary trees by summing the values of overlapping nodes.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
    """
    Args:
        root1: The root node of the first binary tree.
        root2: The root node of the second binary tree.

    Returns:
        The root node of the merged binary tree.
    """
    if not root1:
        return root2
    
    if not root2:
        return root1

    merged_value = root1.val + root2.val
    new_node = TreeNode(merged_value)

    new_node.left = solve(root1.left, root2.left)
    new_node.right = solve(root1.right, root2.right)

    return new_node