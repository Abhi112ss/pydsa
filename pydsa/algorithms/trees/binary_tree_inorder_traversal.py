METADATA = {
    "id": 94,
    "name": "Binary Tree Inorder Traversal",
    "slug": "binary-tree-inorder-traversal",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "stack"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the inorder traversal of its nodes' values.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> list[int]:
    """
    Performs an iterative inorder traversal of a binary tree.

    Inorder traversal follows the pattern: Left Subtree -> Root -> Right Subtree.
    This implementation uses an explicit stack to simulate the call stack,
    avoiding recursion depth issues.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of integers representing the inorder traversal of the tree nodes.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        [2, 1, 3]
    """
    result: list[int] = []
    stack: list[TreeNode] = []
    current_node: TreeNode | None = root

    # Continue as long as there are nodes to visit or nodes in the stack
    while current_node is not None or stack:
        # Reach the leftmost node of the current subtree
        while current_node is not None:
            stack.append(current_node)
            current_node = current_node.left

        # Current node is None, so we backtrack to the last visited node
        current_node = stack.pop()
        result.append(current_node.val)

        # We have visited the node and its left subtree, now move to the right subtree
        current_node = current_node.right

    return result
