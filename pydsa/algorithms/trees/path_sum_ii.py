METADATA = {
    "id": 113,
    "name": "Path Sum II",
    "slug": "path-sum-ii",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "backtracking", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(N^2)",
    "space_complexity": "O(N)",
    "description": "Find all root-to-leaf paths where the sum of the node values equals the given target sum.",
}

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    """
    Finds all root-to-leaf paths in a binary tree where the sum of values equals target_sum.

    Args:
        root: The root node of the binary tree.
        target_sum: The target integer sum to match.

    Returns:
        A list of lists, where each inner list represents a valid path of node values.

    Examples:
        >>> root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(4), TreeNode(1)))
        >>> solve(root, 22)
        [[5, 4, 11, 2], [5, 8, 4, 5]] # Note: Example values depend on tree structure
    """
    results: List[List[int]] = []
    current_path: List[int] = []

    def backtrack(node: Optional[TreeNode], remaining_sum: int) -> None:
        if not node:
            return

        # Add current node to the path
        current_path.append(node.val)

        # Check if it's a leaf node and the sum matches
        is_leaf = not node.left and not node.right
        if is_leaf and remaining_sum == node.val:
            # Append a copy of the current path to results
            results.append(list(current_path))
        else:
            # Continue exploring left and right children
            backtrack(node.left, remaining_sum - node.val)
            backtrack(node.right, remaining_sum - node.val)

        # Backtrack: remove the current node before returning to the parent
        current_path.pop()

    backtrack(root, target_sum)
    return results
