METADATA = {
    "id": 776,
    "name": "Split BST",
    "slug": "split_bst",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "recursion", "binary_search_tree"],
    "difficulty": "medium",
    "time_complexity": "O(h)",
    "space_complexity": "O(h)",
    "description": "Split a binary search tree into two separate BSTs such that one contains all nodes less than or equal to a target value, and the other contains all nodes greater than the target value.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, target: int) -> tuple[TreeNode | None, TreeNode | None]:
    """
    Splits a Binary Search Tree into two BSTs based on a target value.

    Args:
        root: The root node of the original Binary Search Tree.
        target: The value used to split the tree. Nodes <= target go to the first tree.

    Returns:
        A tuple containing (left_tree_root, right_tree_root).

    Examples:
        >>> root = TreeNode(2, TreeNode(1), TreeNode(3))
        >>> solve(root, 2)
        (TreeNode(2, TreeNode(1), None), TreeNode(3))
    """
    if not root:
        return None, None

    if root.val <= target:
        # If current node is <= target, the entire left subtree and the current node
        # belong to the 'small' tree. We only need to split the right subtree.
        small_tree, large_tree = solve(root.right, target)
        
        # Re-attach the split right child to the current node's right
        root.right = small_tree
        return root, large_tree
    else:
        # If current node is > target, the entire right subtree and the current node
        # belong to the 'large' tree. We only need to split the left subtree.
        small_tree, large_tree = solve(root.left, target)
        
        # Re-attach the split left child to the current node's left
        root.left = large_tree
        return small_tree, root