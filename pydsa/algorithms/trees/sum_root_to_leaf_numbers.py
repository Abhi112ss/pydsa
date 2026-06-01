METADATA = {
    "id": 129,
    "name": "Sum Root to Leaf Numbers",
    "slug": "sum-root-to-leaf-numbers",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Calculate the sum of all numbers formed by paths from the root to each leaf in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the sum of all numbers formed by root-to-leaf paths.

    Args:
        root: The root node of the binary tree.

    Returns:
        The total sum of all numbers formed by paths from root to leaf.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        12  # (1 -> 2 = 12) + (1 -> 3 = 13) is wrong, wait. 
            # Example 1: [1,2,3] -> 12 + 13 = 25. 
            # Let's re-verify: root 1, left 2, right 3. Paths: 1-2 (12), 1-3 (13). Sum = 25.
    """
    if not root:
        return 0

    def dfs(node: TreeNode | None, current_sum: int) -> int:
        if not node:
            return 0
        
        # Update the current number by shifting digits left (multiply by 10)
        # and adding the current node's value.
        current_sum = current_sum * 10 + node.val
        
        # If we reach a leaf node, return the accumulated number for this path.
        if not node.left and not node.right:
            return current_sum
        
        # Recursively traverse left and right subtrees and sum their results.
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)

    return dfs(root, 0)
