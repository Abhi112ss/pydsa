METADATA = {
    "id": 1080,
    "name": "Insufficient Nodes in Root to Leaf Paths",
    "slug": "insufficient-nodes-in-root-to-leaf-paths",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Remove all nodes that do not belong to any path from root to leaf with a sum greater than or equal to targetSum.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, target_sum: int) -> TreeNode | None:
    """
    Removes nodes from a binary tree that are not part of any root-to-leaf path 
    with a sum >= target_sum.

    Args:
        root: The root of the binary tree.
        target_sum: The minimum required sum for a root-to-leaf path.

    Returns:
        The root of the modified tree, or None if the entire tree is removed.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root, 4)
        <TreeNode object at ...> (Path 1->3 is 4, path 1->2 is 3, so 2 is removed)
    """
    
    def dfs(node: TreeNode | None, current_sum: int) -> TreeNode | None:
        if not node:
            return None

        # Update the running sum for the current path
        current_sum += node.val

        # If it's a leaf node, check if the path sum meets the requirement
        if not node.left and not node.right:
            return node if current_sum >= target_sum else None

        # Post-order traversal: process children first to prune from bottom up
        node.left = dfs(node.left, current_sum)
        node.right = dfs(node.right, current_sum)

        # After pruning children, if this node has no children left, 
        # it means it's no longer part of a valid path.
        if not node.left and not node.right:
            return None

        return node

    return dfs(root, 0)
