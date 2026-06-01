METADATA = {
    "id": 298,
    "name": "Binary Tree Longest Consecutive Sequence",
    "slug": "binary-tree-longest-consecutive-sequence",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the length of the longest consecutive sequence of nodes in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Finds the length of the longest consecutive sequence in a binary tree.
    
    A sequence is consecutive if each node's value is exactly 1 greater 
    than its parent's value.

    Args:
        root: The root node of the binary tree.

    Returns:
        The length of the longest consecutive sequence.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(2, TreeNode(3)))
        >>> solve(root)
        3
        >>> root = TreeNode(1, TreeNode(2), TreeNode(4, TreeNode(5)))
        >>> solve(root)
        2
    """
    max_length = 0

    def dfs(node: TreeNode | None, current_length: int) -> None:
        nonlocal max_length
        if not node:
            return

        # Update the global maximum length found so far
        max_length = max(max_length, current_length)

        # Check left child: increment length if consecutive, else reset to 1
        if node.left:
            if node.left.val == node.val + 1:
                dfs(node.left, current_length + 1)
            else:
                dfs(node.left, 1)

        # Check right child: increment length if consecutive, else reset to 1
        if node.right:
            if node.right.val == node.val + 1:
                dfs(node.right, current_length + 1)
            else:
                dfs(node.right, 1)

    # Start DFS from the root with an initial sequence length of 1
    if root:
        dfs(root, 1)
        
    return max_length
