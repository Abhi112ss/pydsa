METADATA = {
    "id": 1273,
    "name": "Delete Tree Nodes",
    "slug": "delete-tree-nodes",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove all nodes from a binary tree that belong to a subtree whose sum is zero.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> TreeNode | None:
    """
    Removes all nodes from a binary tree that belong to a subtree with a sum of zero.

    Args:
        root: The root of the binary tree.

    Returns:
        The root of the modified tree, or None if the entire tree is removed.

    Examples:
        >>> root = TreeNode(1, TreeNode(4, TreeNode(3), TreeNode(-7)), TreeNode(2, TreeNode(1), TreeNode(-1)))
        >>> solve(root)
        TreeNode(1, TreeNode(4, None, None), TreeNode(2, TreeNode(1), None))
    """
    
    def post_order_traversal(node: TreeNode | None) -> int:
        """
        Performs a post-order traversal to calculate subtree sums and prune nodes.
        
        Args:
            node: The current node being visited.
            
        Returns:
            The sum of the subtree rooted at 'node'.
        """
        if not node:
            return 0

        # Recursively calculate the sum of left and right subtrees
        left_sum = post_order_traversal(node.left)
        right_sum = post_order_traversal(node.right)

        # If a subtree sum is zero, prune that entire branch
        if left_sum == 0:
            node.left = None
        if right_sum == 0:
            node.right = None

        # Return the total sum of the current subtree
        return node.val + left_sum + right_sum

    if not root:
        return None

    # The root itself is removed if its total subtree sum is zero
    total_sum = post_order_traversal(root)
    return None if total_sum == 0 else root
