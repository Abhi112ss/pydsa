METADATA = {
    "id": 606,
    "name": "Construct String from Binary Tree",
    "slug": "construct-string-from-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["recursion", "dfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given the root of a binary tree, construct a string representation of the tree using a specific preorder traversal format.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> str:
    """
    Args:
        root: The root node of the binary tree.

    Returns:
        A string representation of the binary tree.
    """
    if not root:
        return ""

    result_parts = []

    def traverse(node: TreeNode) -> None:
        if not node:
            return

        result_parts.append(str(node.val))

        if node.left or node.right:
            if node.left:
                result_parts.append("(")
                traverse(node.left)
                result_parts.append(")")
            elif node.right:
                result_parts.append("()")

            if node.right:
                result_parts.append("(")
                traverse(node.right)
                result_parts.append(")")

    traverse(root)
    return "".join(result_parts)