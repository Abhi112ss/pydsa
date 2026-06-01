METADATA = {
    "id": 666,
    "name": "Path Sum IV",
    "slug": "path-sum-iv",
    "category": "Tree",
    "aliases": [],
    "tags": ["hash_map", "dfs", "math", "binary-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of paths in a binary tree that sum to a given target value, where paths must go downwards.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, target_sum: int) -> int:
    """
    Counts the number of paths in a binary tree that sum to target_sum.
    Paths must go downwards from a node to one of its descendants.

    Args:
        root: The root of the binary tree.
        target_sum: The target sum for the paths.

    Returns:
        The total number of paths that sum to target_sum.

    Examples:
        >>> root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(2)), TreeNode(-3, None, TreeNode(11, TreeNode(5), TreeNode(4))))
        >>> solve(root, 8)
        3
    """
    if not root:
        return 0

    # prefix_sums stores the frequency of cumulative sums encountered along the current path.
    # We initialize with {0: 1} to handle cases where a path starting from the root equals target_sum.
    prefix_sums: dict[int, int] = {0: 1}
    
    def dfs(node: TreeNode | None, current_running_sum: int) -> int:
        if not node:
            return 0

        # Update the running sum from the root to the current node
        current_running_sum += node.val
        
        # If (current_running_sum - target_sum) exists in prefix_sums, it means there is a 
        # sub-path ending at the current node that sums to target_sum.
        count = prefix_sums.get(current_running_sum - target_sum, 0)

        # Add current running sum to the map to allow child nodes to use it
        prefix_sums[current_running_sum] = prefix_sums.get(current_running_sum, 0) + 1

        # Recurse to children
        count += dfs(node.left, current_running_sum)
        count += dfs(node.right, current_running_sum)

        # Backtrack: remove the current running sum from the map so it doesn't affect 
        # other branches of the tree (sibling branches)
        prefix_sums[current_running_sum] -= 1

        return count

    return dfs(root, 0)
