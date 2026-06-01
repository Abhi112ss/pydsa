METADATA = {
    "id": 2773,
    "name": "Height of Special Binary Tree",
    "slug": "height-of-special-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "recursion", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the height of a special binary tree where all leaves in a subtree must have the same depth.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the height of a special binary tree.
    
    A special binary tree is defined such that all leaves in any subtree 
    must have the same depth. If the tree is not special, the function 
    returns -1.

    Args:
        root: The root node of the binary tree.

    Returns:
        The height of the tree if it is special, otherwise -1.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        2
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        >>> solve(root)
        -1
    """
    
    def get_special_height(node: TreeNode | None) -> int:
        """
        Helper function using post-order traversal to validate the special condition.
        
        Returns:
            The height of the subtree if it satisfies the special condition,
            otherwise returns -1.
        """
        if not node:
            return 0
        
        # Base case: Leaf node has height 1
        if not node.left and not node.right:
            return 1
        
        # Recursive step: Get heights of left and right subtrees
        left_height = get_special_height(node.left)
        right_height = get_special_height(node.right)
        
        # If any subtree is invalid (returns -1), the current tree is invalid
        if left_height == -1 or right_height == -1:
            return -1
        
        # Special condition: All leaves must have the same depth.
        # In a valid special tree, the height of the left and right subtrees 
        # must be equal.
        if left_height != right_height:
            return -1
            
        # If valid, return the height of the current node
        return left_height + 1

    return get_special_height(root)
