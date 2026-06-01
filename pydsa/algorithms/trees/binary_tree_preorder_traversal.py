METADATA = {
    "id": 144,
    "name": "Binary Tree Preorder Traversal",
    "slug": "binary-tree-preorder-traversal",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "stack", "recursion", "binary-tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the preorder traversal of the nodes' values in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> list[int]:
    """
    Performs a preorder traversal of a binary tree using an iterative approach.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of integers representing the preorder traversal of the tree.
    """
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        current_node = stack.pop()
        result.append(current_node.val)

        if current_node.right:
            stack.append(current_node.right)
        
        if current_node.left:
            stack.append(current_node.left)

    return result