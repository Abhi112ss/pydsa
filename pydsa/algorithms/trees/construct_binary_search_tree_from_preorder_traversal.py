METADATA = {
    "id": 1008,
    "name": "Construct Binary Search Tree from Preorder Traversal",
    "slug": "construct-binary-search-tree-from-preorder-traversal",
    "category": "Trees",
    "aliases": [],
    "tags": ["bst", "recursion", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a binary search tree from an integer array representing its preorder traversal.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(preorder: list[int]) -> TreeNode:
    """
    Constructs a Binary Search Tree (BST) from a given preorder traversal array.

    The algorithm uses a recursive approach with a bounded range (lower and upper limits)
    to ensure each node is placed in its correct position in O(n) time.

    Args:
        preorder: A list of integers representing the preorder traversal of a BST.

    Returns:
        The root node of the constructed Binary Search Tree.

    Examples:
        >>> solve([8, 5, 1, 7, 10, 12])
        <TreeNode object at ...> (Tree structure: 8 is root, 5 is left, 10 is right, etc.)
    """
    # Pointer to track the current element in the preorder list being processed
    index = 0
    n = len(preorder)

    def build_bst(lower_bound: float, upper_bound: float) -> TreeNode | None:
        nonlocal index
        
        # Base case: if we've processed all elements or the current element 
        # violates the BST property for the current subtree
        if index == n or not (lower_bound < preorder[index] < upper_bound):
            return None

        # The current element is valid for this position
        root_val = preorder[index]
        root = TreeNode(root_val)
        index += 1

        # All elements in the left subtree must be < current root value
        root.left = build_bst(lower_bound, root_val)
        
        # All elements in the right subtree must be > current root value
        root.right = build_bst(root_val, upper_bound)

        return root

    # Start recursion with infinity bounds to allow any first element
    return build_bst(float('-inf'), float('inf'))
