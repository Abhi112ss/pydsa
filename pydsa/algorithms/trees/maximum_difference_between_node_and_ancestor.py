METADATA = {
    "id": 1026,
    "name": "Maximum Difference Between Node and Ancestor",
    "slug": "maximum-difference-between-node-and-ancestor",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the maximum absolute difference between a node and any of its ancestors in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Calculates the maximum absolute difference between a node and its ancestor.

    The algorithm uses Depth First Search (DFS) to traverse the tree. For each path,
    we maintain the minimum and maximum values encountered so far. The maximum 
    difference for any node is the difference between the max and min values 
    found on the path from the root to that node.

    Args:
        root: The root node of the binary tree.

    Returns:
        The maximum absolute difference between a node and its ancestor.

    Examples:
        >>> root = TreeNode(5, TreeNode(0, TreeNode(12), TreeNode(6)), TreeNode(13, TreeNode(7), TreeNode(10)))
        >>> solve(root)
        12
    """
    if not root:
        return 0

    def dfs(node: TreeNode, current_min: int, current_max: int) -> int:
        if not node:
            # Base case: return the difference found on this path
            return current_max - current_min

        # Update the running min and max for the current path
        current_min = min(current_min, node.val)
        current_max = max(current_max, node.val)

        # Recursively find the max difference in left and right subtrees
        left_diff = dfs(node.left, current_min, current_max)
        right_diff = dfs(node.right, current_min, current_max)

        # Return the maximum difference found in either branch
        return max(left_diff, right_diff)

    # Start DFS with the root's value as both min and max
    return dfs(root, root.val, root.val)
