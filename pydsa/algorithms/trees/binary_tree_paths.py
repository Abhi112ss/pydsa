METADATA = {
    "id": 257,
    "name": "Binary Tree Paths",
    "slug": "binary-tree-paths",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary_tree"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return all root-to-leaf paths in a binary tree as strings.",
}

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> List[str]:
    """
    Args:
        root: The root node of the binary tree.

    Returns:
        A list of strings representing all root-to-leaf paths.
    """
    if not root:
        return []

    paths: List[str] = []

    def traverse(node: TreeNode, current_path: str) -> None:
        current_path += str(node.val)

        if not node.left and not node.right:
            paths.append(current_path)
            return

        if node.left:
            traverse(node.left, current_path + "->")
        
        if node.right:
            traverse(node.right, current_path + "->")

    traverse(root, "")
    return paths