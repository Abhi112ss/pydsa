METADATA = {
    "id": 3249,
    "name": "Count the Number of Good Nodes",
    "slug": "count-the-number-of-good-nodes",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Count nodes in a tree such that no node on the path from root to that node has a value greater than the node's value.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Counts the number of 'good' nodes in a binary tree.
    A node is good if in the path from the root to that node, there are no nodes 
    with a value strictly greater than the current node's value.

    Args:
        root: The root node of the binary tree.

    Returns:
        The total count of good nodes in the tree.

    Examples:
        >>> root = TreeNode(3, TreeNode(1, TreeNode(4, TreeNode(5), TreeNode(3)), TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(1)), TreeNode(3, TreeNode(2, TreeNode(1), TreeNode(2)), TreeNode(4, TreeNode(1), TreeNode(1))))
        >>> solve(root)
        6
    """
    if not root:
        return 0

    def dfs(node: TreeNode, current_max: int) -> int:
        """
        Performs a depth-first search to count good nodes.

        Args:
            node: The current node being visited.
            current_max: The maximum value encountered on the path from the root to this node.

        Returns:
            The number of good nodes in the subtree rooted at 'node'.
        """
        if not node:
            return 0

        # A node is 'good' if its value is greater than or equal to the max value seen so far
        is_good = 1 if node.val >= current_max else 0
        
        # Update the maximum value for the next level of the recursion
        new_max = max(current_max, node.val)

        # Recursively count good nodes in left and right subtrees
        left_count = dfs(node.left, new_max)
        right_count = dfs(node.right, new_max)

        return is_good + left_count + right_count

    # Start DFS with the root's value as the initial maximum
    return dfs(root, root.val)
