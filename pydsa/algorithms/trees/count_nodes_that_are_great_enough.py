METADATA = {
    "id": 2792,
    "name": "Count Nodes That Are Great Enough",
    "slug": "count-nodes-that-are-great-enough",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Count the number of nodes in a binary tree where the node's value is greater than or equal to the maximum value in its subtree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Counts the number of nodes in a binary tree that are 'great enough'.
    A node is great enough if its value is greater than or equal to the 
    maximum value in its subtree.

    Args:
        root: The root of the binary tree.

    Returns:
        The total count of 'great enough' nodes.

    Examples:
        >>> root = TreeNode(1, TreeNode(3, TreeNode(3), TreeNode(3)), TreeNode(1, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(1)))
        >>> solve(root)
        4
    """
    count = 0

    def post_order_traversal(node: TreeNode) -> int:
        """
        Performs a post-order traversal to find the maximum value in subtrees.
        
        Args:
            node: The current node being visited.
            
        Returns:
            The maximum value found in the subtree rooted at 'node'.
        """
        nonlocal count

        if not node:
            # Return a very small value for null nodes so they don't affect max()
            return float('-inf')

        # Recursively find the maximum value in the left and right subtrees
        left_max = post_order_traversal(node.left)
        right_max = post_order_traversal(node.right)

        # The maximum value in the current subtree is the max of (node.val, left_max, right_max)
        current_subtree_max = max(node.val, left_max, right_max)

        # A node is 'great enough' if its value is >= the max of its children's subtrees
        # Note: current_subtree_max is the max of the whole subtree including the node itself.
        # If node.val == current_subtree_max, it means node.val is >= all values in its subtree.
        if node.val == current_subtree_max:
            count += 1

        return current_subtree_max

    post_order_traversal(root)
    return count
