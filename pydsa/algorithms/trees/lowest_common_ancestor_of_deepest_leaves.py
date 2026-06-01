METADATA = {
    "id": 1123,
    "name": "Lowest Common Ancestor of Deepest Leaves",
    "slug": "lowest-common-ancestor-of-deepest-leaves",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the lowest common ancestor of all leaves that are at the maximum depth in a binary tree.",
}

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Finds the lowest common ancestor of the deepest leaves in a binary tree.

    The algorithm uses a post-order traversal (DFS) to determine the depth of 
    each subtree. For any node, if the maximum depth of its left subtree 
    equals the maximum depth of its right subtree, then this node is a 
    candidate for the LCA of the deepest leaves found so far.

    Args:
        root: The root of the binary tree.

    Returns:
        The TreeNode that is the lowest common ancestor of the deepest leaves.

    Examples:
        >>> root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(2, TreeNode(7), None))
        >>> solve(root).val
        5
    """
    if not root:
        return None

    def dfs(node: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
        """
        Helper function that returns a tuple of (depth, lca_candidate).
        
        Args:
            node: The current node being visited.
            
        Returns:
            A tuple containing the maximum depth of the subtree rooted at 'node'
            and the LCA candidate for the deepest leaves within that subtree.
        """
        if not node:
            return 0, None

        # Post-order traversal: visit children first
        left_depth, left_lca = dfs(node.left)
        right_depth, right_lca = dfs(node.right)

        # Case 1: Left subtree is deeper, LCA must be in the left subtree
        if left_depth > right_depth:
            return left_depth + 1, left_lca
        
        # Case 2: Right subtree is deeper, LCA must be in the right subtree
        if right_depth > left_depth:
            return right_depth + 1, right_lca

        # Case 3: Both subtrees have the same maximum depth.
        # This node is the lowest common ancestor for the deepest leaves 
        # found in both subtrees.
        return left_depth + 1, node

    # The second element of the returned tuple is the LCA of the deepest leaves
    _, lca_node = dfs(root)
    return lca_node
