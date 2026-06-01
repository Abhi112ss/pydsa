METADATA = {
    "id": 1676,
    "name": "Lowest Common Ancestor of a Binary Tree IV",
    "slug": "lowest-common-ancestor-of-a-binary-tree-iv",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lowest common ancestor of a given set of nodes in a binary tree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, values: list[int]) -> TreeNode:
    """
    Finds the lowest common ancestor (LCA) of a set of nodes in a binary tree.

    The LCA is defined as the deepest node in the tree that has all the 
    given values in its subtree.

    Args:
        root: The root of the binary tree.
        values: A list of integers representing the values of the target nodes.

    Returns:
        The TreeNode that is the lowest common ancestor, or None if no LCA exists.

    Examples:
        >>> root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
        >>> solve(root, [2, 8])
        <TreeNode: 2>
    """
    # Convert values to a set for O(1) lookup
    target_values = set(values)
    
    def dfs(current_node: TreeNode) -> TreeNode:
        """
        Recursive helper to traverse the tree and find the LCA.
        
        Returns:
            The node that is either a target node, an LCA, or None.
        """
        if not current_node:
            return None

        # Post-order traversal: visit children first
        left_res = dfs(current_node.left)
        right_res = dfs(current_node.right)

        # If current node is one of the targets, it is a potential LCA candidate
        # for its ancestors, but we must still check its children.
        if current_node.val in target_values:
            return current_node

        # If one target is found in the left subtree and another in the right,
        # then the current node is the lowest common ancestor.
        if left_res and right_res:
            return current_node

        # Otherwise, return the non-null result from either subtree
        return left_res if left_res else right_res

    return dfs(root)
