METADATA = {
    "id": 3593,
    "name": "Minimum Increments to Equalize Leaf Paths",
    "slug": "minimum-increments-to-equalize-leaf-paths",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "greedy", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the minimum increments needed to make all paths from root to leaf have the same sum.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the minimum increments required to make all root-to-leaf path sums equal.
    
    The strategy uses a bottom-up approach (post-order traversal). For any internal 
    node, we ensure that the maximum path sum coming from its left subtree 
    matches the maximum path sum coming from its right subtree by incrementing 
    the smaller one.

    Args:
        root: The root of the binary tree.

    Returns:
        The total number of increments performed.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        1
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        >>> solve(root)
        2
    """
    if not root:
        return 0

    total_increments = 0

    def dfs(node: TreeNode | None) -> int:
        nonlocal total_increments
        
        # Base case: If leaf node, the path sum contribution is just its value
        if not node.left and not node.right:
            return node.val
        
        # If it's a node with only one child, we treat the missing child as 0 
        # but in a real tree structure, we only traverse existing children.
        # However, the problem implies we equalize paths to existing leaves.
        
        left_sum = 0
        right_sum = 0
        
        if node.left:
            left_sum = dfs(node.left)
        if node.right:
            right_sum = dfs(node.right)
            
        # If the node has two children, we must equalize the path sums 
        # coming from both subtrees to ensure all paths through this node 
        # eventually reach the same total.
        if node.left and node.right:
            diff = abs(left_sum - right_sum)
            total_increments += diff
            # Return the maximum path sum to the parent
            return node.val + max(left_sum, right_sum)
        
        # If the node has only one child, the path sum is just node.val + child_sum
        # No increment is needed here because there is only one path direction.
        return node.val + (left_sum if node.left else right_sum)

    dfs(root)
    return total_increments
