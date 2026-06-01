METADATA = {
    "id": 437,
    "name": "Path Sum III",
    "slug": "path-sum-iii",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "prefix_sum", "recursion", "binary-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of paths in a binary tree that sum to a given target value, where paths do not need to start or end at the root.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, target_sum: int) -> int:
    """
    Calculates the number of paths in a binary tree that sum to target_sum.
    
    The algorithm uses a prefix sum approach combined with Depth First Search (DFS).
    By maintaining a running sum from the root to the current node and storing 
    the frequency of these sums in a hash map, we can determine in O(1) if a 
    sub-path ending at the current node sums to the target.

    Args:
        root: The root of the binary tree.
        target_sum: The target sum for the paths.

    Returns:
        The total number of paths that sum to target_sum.

    Examples:
        >>> root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(2)), TreeNode(-3, TreeNode(11), TreeNode(4, TreeNode(7), TreeNode(2))))
        >>> solve(root, 8)
        3
    """
    # prefix_sums stores {running_sum: frequency}
    # We initialize with {0: 1} to account for paths that sum to target_sum 
    # starting exactly from the root.
    prefix_sums: dict[int, int] = {0: 1}

    def dfs(node: TreeNode | None, current_running_sum: int) -> int:
        if not node:
            return 0

        current_running_sum += node.val
        
        # The number of paths ending at this node that sum to target_sum is 
        # the number of times (current_running_sum - target_sum) has occurred 
        # as a prefix sum previously in this path.
        count = prefix_sums.get(current_running_sum - target_sum, 0)

        # Add current running sum to the map for child nodes to use
        prefix_sums[current_running_sum] = prefix_sums.get(current_running_sum, 0) + 1

        # Recurse to children
        count += dfs(node.left, current_running_sum)
        count += dfs(node.right, current_running_sum)

        # Backtrack: remove the current running sum from the map so it doesn't 
        # affect paths in other branches of the tree.
        prefix_sums[current_running_sum] -= 1

        return count

    return dfs(root, 0)
