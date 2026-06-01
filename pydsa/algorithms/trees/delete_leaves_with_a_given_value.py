METADATA = {
    "id": 1325,
    "name": "Delete Leaves With a Given Value",
    "slug": "delete-leaves-with-a-given-value",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Remove all leaf nodes in a binary tree that have a specific value, potentially creating new leaves in the process.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, target: int) -> TreeNode | None:
    """
    Removes all leaf nodes from a binary tree that have the specified target value.
    The removal is recursive: if removing a leaf makes its parent a leaf with 
    the target value, that parent is also removed.

    Args:
        root: The root node of the binary tree.
        target: The integer value of the leaves to be removed.

    Returns:
        The root of the modified binary tree, or None if the entire tree is removed.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(2))
        >>> solve(root, 2)
        <TreeNode(1)>
        
        >>> root = TreeNode(1, TreeNode(1), TreeNode(1))
        >>> solve(root, 1)
        None
    """
    if not root:
        return None

    # Perform a post-order traversal (bottom-up approach).
    # We must process children before the current node to handle cases 
    # where a node becomes a leaf after its children are deleted.
    root.left = solve(root.left, target)
    root.right = solve(root.right, target)

    # After processing children, check if the current node has become a leaf.
    # If it is a leaf and its value matches the target, return None to "delete" it.
    if root.left is None and root.right is None and root.val == target:
        return None

    return root
