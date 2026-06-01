METADATA = {
    "id": 889,
    "name": "Construct Binary Tree from Preorder and Postorder Traversal",
    "slug": "construct-binary-tree-from-preorder-and-postorder-traversal",
    "category": "Trees",
    "aliases": [],
    "tags": ["recursion", "divide_and_conquer", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a binary tree from its preorder and postorder traversal arrays.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(preorder: list[int], postorder: list[int]) -> TreeNode:
    """
    Constructs a binary tree from preorder and postorder traversal arrays.

    Args:
        preorder: A list of integers representing the preorder traversal.
        postorder: A list of integers representing the postorder traversal.

    Returns:
        The root of the constructed binary tree.

    Examples:
        >>> preorder = [1, 2, 4, 5, 3, 6, 7]
        >>> postorder = [4, 5, 2, 6, 7, 3, 1]
        >>> root = solve(preorder, postorder)
        >>> root.val
        1
    """
    # Map values to their indices in postorder for O(1) lookup
    postorder_index_map = {val: i for i, val in enumerate(postorder)}

    def build_tree(pre_start: int, pre_end: int, post_start: int, post_end: int) -> TreeNode | None:
        # Base case: no elements to process
        if pre_start > pre_end:
            return None

        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        # If there is only one node, it's a leaf
        if pre_start == pre_end:
            return root

        # The next element in preorder is the root of the left subtree
        left_root_val = preorder[pre_start + 1]
        
        # Find the index of the left subtree's root in postorder to determine subtree size
        # Everything in postorder from post_start to left_root_idx belongs to the left subtree
        left_root_post_idx = postorder_index_map[left_root_val]
        left_subtree_size = left_root_post_idx - post_start + 1

        # Recursively construct the left subtree
        # Preorder: skip current root, take 'size' elements
        # Postorder: take 'size' elements from the current start
        root.left = build_tree(
            pre_start + 1, 
            pre_start + left_subtree_size, 
            post_start, 
            left_root_post_idx
        )

        # Recursively construct the right subtree
        # Preorder: skip current root and the entire left subtree
        # Postorder: elements after the left subtree, up to the element before current root
        root.right = build_tree(
            pre_start + left_subtree_size + 1, 
            pre_end, 
            left_root_post_idx + 1, 
            post_end - 1
        )

        return root

    return build_tree(0, len(preorder) - 1, 0, len(postorder) - 1)