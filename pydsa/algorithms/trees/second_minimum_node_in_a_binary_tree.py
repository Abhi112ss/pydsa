METADATA = {
    "id": 671,
    "name": "Second Minimum Node In a Binary Tree",
    "slug": "second_minimum_node_in_a_binary_tree",
    "category": "Tree",
    "aliases": ["find second minimum value in special binary tree"],
    "tags": ["dfs", "recursion"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the second minimum value in a special binary tree where each node has exactly two or zero children and the root value is the minimum.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode) -> int:
    """
    Find the second minimum value in a special binary tree where each node has exactly
    two or zero children and the root value is the minimum.

    Args:
        root: The root of the special binary tree.

    Returns:
        The second minimum value in the tree, or -1 if it doesn't exist.

    Examples:
        >>> solve(TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
        5
        >>> solve(TreeNode(2, TreeNode(2), TreeNode(2)))
        -1
    """
    if not root:
        return -1

    # The root is always the minimum in this special tree
    min_val = root.val
    second_min = float('inf')

    def dfs(node: TreeNode) -> None:
        nonlocal second_min
        if not node:
            return

        # If current node value is greater than root, it's a candidate for second minimum
        if node.val > min_val:
            second_min = min(second_min, node.val)
            # No need to explore children since they are >= current node.val
            return

        # If current node equals root value, explore children
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return second_min if second_min != float('inf') else -1
