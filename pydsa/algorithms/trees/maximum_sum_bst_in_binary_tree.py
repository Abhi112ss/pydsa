METADATA = {
    "id": 1373,
    "name": "Maximum Sum BST in Binary Tree",
    "slug": "maximum-sum-bst-in-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "binary-search-tree"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the maximum sum of a subtree that is a valid Binary Search Tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SubtreeInfo:
    def __init__(self, is_bst: bool, min_val: float, max_val: float, total_sum: int):
        self.is_bst = is_bst
        self.min_val = min_val
        self.max_val = max_val
        self.total_sum = total_sum

def solve(root: TreeNode) -> int:
    """
    Finds the maximum sum of a subtree that is a valid Binary Search Tree.

    Args:
        root: The root of the binary tree.

    Returns:
        The maximum sum found among all valid BST subtrees. Returns 0 if no BST has a positive sum.

    Examples:
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
        >>> solve(root)
        20
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
        >>> solve(root)
        0
    """
    max_sum = 0

    def traverse(node: TreeNode | None) -> SubtreeInfo:
        nonlocal max_sum
        
        if not node:
            # Base case: An empty node is a BST with sum 0
            # We use infinity for min/max to ensure parent nodes validate correctly
            return SubtreeInfo(True, float('inf'), float('-inf'), 0)

        # Post-order traversal: process children first
        left_info = traverse(node.left)
        right_info = traverse(node.right)

        # A node is part of a BST if:
        # 1. Left and right subtrees are BSTs
        # 2. Node value is greater than the max value in the left subtree
        # 3. Node value is less than the min value in the right subtree
        if (left_info.is_bst and right_info.is_bst and 
            left_info.max_val < node.val < right_info.min_val):
            
            current_sum = left_info.total_sum + right_info.total_sum + node.val
            max_sum = max(max_sum, current_sum)
            
            # Calculate new min/max for the current subtree
            # If left is None, min is node.val; if right is None, max is node.val
            current_min = min(node.val, left_info.min_val)
            current_max = max(node.val, right_info.max_val)
            
            return SubtreeInfo(True, current_min, current_max, current_sum)
        
        # If current node is not a BST, return is_bst=False
        # Min/Max values don't matter for non-BST nodes as they won't be used by parents
        return SubtreeInfo(False, 0.0, 0.0, 0)

    traverse(root)
    return max_sum