METADATA = {
    "id": 3715,
    "name": "Sum of Perfect Square Ancestors",
    "slug": "sum_of_perfect_square_ancestors",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "math"],
    "difficulty": "medium",
    "time_complexity": "O(N * sqrt(max_val))",
    "space_complexity": "O(N)",
    "description": "Calculate the sum of all ancestors of each node that are perfect squares using DFS.",
}

import math

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> dict[int, int]:
    """
    Traverses the tree to find the sum of perfect square ancestors for each node.

    Args:
        root: The root of the binary tree.

    Returns:
        A dictionary where keys are node values and values are the sum of 
        their perfect square ancestors. Note: If node values are not unique, 
        this implementation assumes unique values as per standard LeetCode 
        tree problems unless specified otherwise.

    Examples:
        >>> root = TreeNode(4, TreeNode(9), TreeNode(16))
        >>> solve(root)
        {4: 0, 9: 4, 16: 4}
    """
    if not root:
        return {}

    results: dict[int, int] = {}

    def is_perfect_square(n: int) -> bool:
        if n < 0:
            return False
        root_val = int(math.isqrt(n))
        return root_val * root_val == n

    def dfs(node: TreeNode | None, current_square_sum: int) -> None:
        if not node:
            return

        # Store the sum of perfect square ancestors for the current node
        results[node.val] = current_square_sum

        # Calculate the new sum if the current node is a perfect square
        new_sum = current_square_sum
        if is_perfect_square(node.val):
            new_sum += node.val

        # Recurse to children with the updated running sum
        dfs(node.left, new_sum)
        dfs(node.right, new_sum)

    # Start DFS with an initial sum of 0
    dfs(root, 0)
    return results
