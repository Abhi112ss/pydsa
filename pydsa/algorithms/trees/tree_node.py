METADATA = {
    "id": 608,
    "name": "Tree Node",
    "slug": "tree-node",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree_traversal", "conditional_logic"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Classify each node in a binary tree as a Root, Inner, or Leaf node.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> dict[int, str]:
    """
    Classifies each node in a binary tree as 'Root', 'Inner', or 'Leaf'.

    Args:
        root: The root node of the binary tree.

    Returns:
        A dictionary where keys are node values and values are the classification strings.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        {1: 'Root', 2: 'Leaf', 3: 'Leaf'}

        >>> root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        >>> solve(root)
        {1: 'Root', 2: 'Inner', 4: 'Leaf', 3: 'Leaf'}
    """
    if not root:
        return {}

    results: dict[int, str] = {}

    def traverse(node: TreeNode, is_root: bool) -> None:
        if not node:
            return

        # Determine if the current node is a leaf (no children)
        is_leaf = node.left is None and node.right is None

        if is_root:
            results[node.val] = "Root"
        elif is_leaf:
            results[node.val] = "Leaf"
        else:
            # If it's not a root and not a leaf, it must be an inner node
            results[node.val] = "Inner"

        # Recursively visit children, passing False for is_root as they are descendants
        traverse(node.left, False)
        traverse(node.right, False)

    # Start traversal from the root
    traverse(root, True)
    return results
