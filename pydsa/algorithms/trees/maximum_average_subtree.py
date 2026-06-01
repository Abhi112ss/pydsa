METADATA = {
    "id": 1120,
    "name": "Maximum Average Subtree",
    "slug": "maximum-average-subtree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "binary-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the maximum average value among all subtrees of a given binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> float:
    """
    Calculates the maximum average value of any subtree in the given binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The maximum average value found among all subtrees.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        2.0
        >>> root = TreeNode(4, TreeNode(5, TreeNode(6), TreeNode(7)), TreeNode(3))
        >>> solve(root)
        4.25
    """
    max_avg = 0.0

    def dfs(node: TreeNode) -> tuple[float, int]:
        """
        A post-order traversal that returns (sum_of_subtree, count_of_nodes).

        Args:
            node: The current node being visited.

        Returns:
            A tuple containing the sum of values in the subtree and the number of nodes.
        """
        nonlocal max_avg

        if not node:
            return 0.0, 0

        # Recursively get sum and count from left and right children
        left_sum, left_count = dfs(node.left)
        right_sum, right_count = dfs(node.right)

        # Calculate current subtree metrics
        current_sum = left_sum + right_sum + node.val
        current_count = left_count + right_count + 1

        # Update the global maximum average found so far
        current_avg = current_sum / current_count
        if current_avg > max_avg:
            max_avg = current_avg

        return current_sum, current_count

    dfs(root)
    return max_avg
