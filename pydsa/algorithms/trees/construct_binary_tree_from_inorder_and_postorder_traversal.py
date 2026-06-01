METADATA = {
    "id": 106,
    "name": "Construct Binary Tree from Inorder and Postorder Traversal",
    "slug": "construct-binary-tree-from-inorder-and-postorder-traversal",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "recursion", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a binary tree from its inorder and postorder traversal arrays.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(inorder: list[int], postorder: list[int]) -> TreeNode | None:
    """
    Constructs a binary tree given its inorder and postorder traversal sequences.

    Args:
        inorder: A list of integers representing the inorder traversal.
        postorder: A list of integers representing the postorder traversal.

    Returns:
        The root node of the constructed binary tree.

    Examples:
        >>> inorder = [9, 3, 15, 20, 7]
        >>> postorder = [9, 15, 7, 20, 3]
        >>> root = solve(inorder, postorder)
        >>> root.val
        3
    """
    if not inorder or not postorder:
        return None

    # Map values to their indices in inorder array for O(1) lookup
    inorder_index_map = {val: i for i, val in enumerate(inorder)}
    
    # Use a pointer to track the current root in postorder (working backwards)
    postorder_idx = len(postorder) - 1

    def build_subtree(in_start: int, in_end: int) -> TreeNode | None:
        nonlocal postorder_idx

        # Base case: if the range is invalid
        if in_start > in_end:
            return None

        # The last element in the current postorder segment is the root
        root_val = postorder[postorder_idx]
        root = TreeNode(root_val)
        postorder_idx -= 1

        # Find the split point in the inorder array
        root_in_idx = inorder_index_map[root_val]

        # IMPORTANT: Build the RIGHT subtree first.
        # In postorder (Left, Right, Root), when traversing backwards, 
        # we encounter Root, then Right, then Left.
        root.right = build_subtree(root_in_idx + 1, in_end)
        root.left = build_subtree(in_start, root_in_idx - 1)

        return root

    return build_subtree(0, len(inorder) - 1)
