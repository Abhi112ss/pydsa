METADATA = {
    "id": 1339,
    "name": "Maximum Product of Splitted Binary Tree",
    "slug": "maximum-product-of-splitted-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Split a binary tree into two subtrees such that the product of their sums is maximized.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Calculates the maximum product of the sums of two subtrees formed by splitting the tree.

    Args:
        root: The root of the binary tree.

    Returns:
        The maximum product of the sums of the two subtrees.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        6
    """
    if not root:
        return 0

    # We need to store all possible subtree sums to find the best split point.
    # A split occurs by removing an edge, which effectively isolates a subtree.
    subtree_sums = []

    def calculate_subtree_sum(node: TreeNode) -> int:
        """
        Post-order traversal to calculate the sum of each subtree.
        
        Args:
            node: The current node being processed.
            
        Returns:
            The sum of the subtree rooted at 'node'.
        """
        if not node:
            return 0
        
        # Recursively calculate sums of left and right children
        current_sum = (
            node.val + 
            calculate_subtree_sum(node.left) + 
            calculate_subtree_sum(node.right)
        )
        
        # Store the sum of the subtree rooted at the current node
        # Note: The root's sum will be the total sum of the entire tree.
        subtree_sums.append(current_sum)
        return current_sum

    # First pass: Calculate all subtree sums and identify the total sum
    total_sum = calculate_subtree_sum(root)
    
    max_product = 0
    
    # Second pass: Iterate through all collected subtree sums (except the total sum itself)
    # to find the split that maximizes sum * (total_sum - sum).
    for s in subtree_sums:
        # We cannot split the tree at the root itself (that would result in a sum of 0)
        if s == total_sum:
            continue
            
        current_product = s * (total_sum - s)
        if current_product > max_product:
            max_product = current_product
            
    return max_product
