METADATA = {
    "id": 105,
    "name": "Construct Binary Tree from Preorder and Inorder Traversal",
    "slug": "construct-binary-tree-from-preorder-and-inorder-traversal",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "recursion", "hash_map", "binary-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given two integer arrays preorder and inorder, construct the binary tree and return its root.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Constructs a binary tree from preorder and inorder traversal arrays.

    Args:
        preorder: A list of integers representing the preorder traversal.
        inorder: A list of integers representing the inorder traversal.

    Returns:
        The root node of the constructed binary tree.

    Examples:
        >>> preorder = [3, 9, 20, 15, 7]
        >>> inorder = [9, 3, 15, 20, 7]
        >>> root = solve(preorder, inorder)
        >>> root.val
        3
    """
    # Map values to their indices in inorder array for O(1) lookup
    inorder_index_map = {val: i for i, val in enumerate(inorder)}
    
    # Use a pointer to track the current root in the preorder list
    preorder_idx = 0

    def build_subtree(left_boundary: int, right_boundary: int) -> TreeNode:
        nonlocal preorder_idx
        
        # Base case: if the current range is empty
        if left_boundary > right_boundary:
            return None

        # The first element in preorder (at current index) is the root of this subtree
        root_val = preorder[preorder_idx]
        root = TreeNode(root_val)
        preorder_idx += 1

        # Find the split point in the inorder array using the map
        mid_idx = inorder_index_map[root_val]

        # Recursively build the left subtree first (preorder: Root -> Left -> Right)
        # Elements to the left of mid_idx in inorder belong to the left subtree
        root.left = build_subtree(left_boundary, mid_idx - 1)
        
        # Elements to the right of mid_idx in inorder belong to the right subtree
        root.right = build_subtree(mid_idx + 1, right_boundary)

        return root

    return build_subtree(0, len(inorder) - 1)
