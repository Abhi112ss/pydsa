METADATA = {
    "id": 988,
    "name": "Smallest String Starting From Leaf",
    "slug": "smallest-string-starting-from-leaf",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "string", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest string formed by concatenating values from a leaf node up to the root.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> str:
    """
    Finds the lexicographically smallest string formed by traversing from leaf to root.

    Args:
        root: The root of the binary tree.

    Returns:
        The lexicographically smallest string.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        '21'
    """
    if not root:
        return ""

    smallest_string = "z"  # Initialize with a value larger than any possible string

    def dfs(node: TreeNode, current_path: str) -> None:
        nonlocal smallest_string
        
        if not node:
            return

        # Prepend current node value to the path (building leaf-to-root)
        new_path = str(node.val) + current_path

        # Check if it's a leaf node
        if not node.left and not node.right:
            # Update smallest_string if new_path is lexicographically smaller
            if new_path < smallest_string:
                smallest_string = new_path
            return

        # Continue DFS to children
        if node.left:
            dfs(node.left, new_path)
        if node.right:
            dfs(node.right, new_path)

    dfs(root, "")
    return smallest_string
