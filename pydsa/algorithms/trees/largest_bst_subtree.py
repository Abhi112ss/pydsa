METADATA = {
    "id": 333,
    "name": "Largest BST Subtree",
    "slug": "largest-bst-subtree",
    "category": "Tree",
    "aliases": [],
    "tags": ["depth_first_search", "tree", "binary_search_tree"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the size of the largest subtree that is a valid Binary Search Tree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class SubtreeInfo:
    """Helper class to store information about a subtree during bottom-up traversal."""
    def __init__(self, is_bst: bool, size: int, min_val: float, max_val: float):
        self.is_bst = is_bst
        self.size = size
        self.min_val = min_val
        self.max_val = max_val

def solve(root: TreeNode) -> int:
    """
    Finds the size of the largest subtree that is a valid Binary Search Tree.

    Args:
        root: The root of the binary tree.

    Returns:
        The size of the largest BST subtree.

    Examples:
        >>> root = TreeNode(1, TreeNode(0, TreeNode(-1, TreeNode(None, TreeNode(2, TreeNode(3), TreeNode(4))), TreeNode(None))), TreeNode(2, TreeNode(None, TreeNode(None), TreeNode(5)), TreeNode(None)))
        >>> solve(root)
        4
    """
    max_bst_size = 0

    def traverse(node: TreeNode) -> SubtreeInfo:
        nonlocal max_bst_size

        # Base case: An empty node is a BST of size 0
        if not node:
            return SubtreeInfo(True, 0, float('inf'), float('-inf'))

        # Post-order traversal: Process children first to build bottom-up
        left_info = traverse(node.left)
        right_info = traverse(node.right)

        # A node is part of a BST if:
        # 1. Both left and right subtrees are BSTs
        # 2. The node's value is greater than the max value in the left subtree
        # 3. The node's value is less than the min value in the right subtree
        if (left_info.is_bst and right_info.is_bst and 
            left_info.max_val < node.val < right_info.min_val):
            
            current_size = left_info.size + right_info.size + 1
            max_bst_size = max(max_bst_size, current_size)
            
            # Return info for the current node to its parent
            # Min value is the min of left subtree or current node
            # Max value is the max of right subtree or current node
            return SubtreeInfo(
                is_bst=True,
                size=current_size,
                min_val=min(node.val, left_info.min_val),
                max_val=max(node.val, right_info.max_val)
            )
        else:
            # If current node is not a BST, mark it so parents cannot be BSTs
            return SubtreeInfo(False, 0, float('-inf'), float('inf'))

    traverse(root)
    return max_bst_size