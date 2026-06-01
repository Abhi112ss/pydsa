METADATA = {
    "id": 1973,
    "name": "Count Nodes Equal to Sum of Descendants",
    "slug": "count-nodes-equal-to-sum-of-descendants",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "trees", "binary-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Count the number of nodes in a binary tree whose value is equal to the sum of all its descendants.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Counts the number of nodes in a binary tree whose value equals the sum of its descendants.

    Args:
        root: The root of the binary tree.

    Returns:
        The count of nodes satisfying the condition.

    Examples:
        >>> root = TreeNode(10, TreeNode(4, TreeNode(2), TreeNode(2)), TreeNode(6, TreeNode(1), TreeNode(5)))
        >>> solve(root)
        1
    """
    count = 0

    def post_order_traversal(node: TreeNode | None) -> int:
        """
        Performs a post-order DFS to calculate the sum of descendants.
        
        Args:
            node: The current node being visited.
            
        Returns:
            The sum of the current node and all its descendants.
        """
        nonlocal count
        if not node:
            return 0

        # Recursively get the sum of descendants for left and right subtrees
        left_sum = post_order_traversal(node.left)
        right_sum = post_order_traversal(node.right)
        
        # The sum of descendants is the sum of the left and right subtree totals
        descendant_sum = left_sum + right_sum

        # Check if the current node's value matches the sum of its descendants
        if node.val == descendant_sum:
            count += 1

        # Return the total sum of this subtree (node value + its descendants) to the parent
        return node.val + descendant_sum

    post_order_traversal(root)
    return count
