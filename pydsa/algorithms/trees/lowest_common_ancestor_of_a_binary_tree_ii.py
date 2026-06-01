METADATA = {
    "id": 1644,
    "name": "Lowest Common Ancestor of a Binary Tree II",
    "slug": "lowest-common-ancestor-of-a-binary-tree-ii",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lowest common ancestor of two nodes in a binary tree, ensuring both nodes actually exist in the tree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, p: TreeNode | None, q: TreeNode | None) -> TreeNode | None:
    """
    Finds the lowest common ancestor of two nodes p and q in a binary tree.
    Unlike the standard LCA problem, this version requires verifying that both 
    p and q exist in the tree.

    Args:
        root: The root of the binary tree.
        p: The first node.
        q: The second node.

    Returns:
        The lowest common ancestor node if both p and q exist, otherwise None.

    Examples:
        >>> root = TreeNode(3, TreeNode(5), TreeNode(1))
        >>> p = TreeNode(5)
        >>> q = TreeNode(1)
        >>> solve(root, p, q)
        <TreeNode object at ...> (the node with value 3)
    """
    if not root or not p or not q:
        return None

    # We need to track if we actually found both nodes to handle the case
    # where one node might be an ancestor of the other but the other doesn't exist.
    found_p = False
    found_q = False

    def find_lca(current_node: TreeNode | None) -> TreeNode | None:
        nonlocal found_p, found_q
        
        if not current_node:
            return None

        # Post-order traversal: visit children first
        left_res = find_lca(current_node.left)
        right_res = find_lca(current_node.right)

        # Check if current node is one of the targets
        if current_node == p:
            found_p = True
            return current_node
        if current_node == q:
            found_q = True
            return current_node

        # If both left and right subtrees returned a non-None value, 
        # then current_node is the LCA.
        if left_res and right_res:
            return current_node

        # Otherwise, return the non-None result from children
        return left_res if left_res else right_res

    # Note: The standard LCA logic returns 'p' if 'p' is an ancestor of 'q'.
    # However, if 'q' doesn't exist in the tree at all, the standard logic 
    # would incorrectly return 'p'. We must verify existence.
    
    # To handle the "existence" requirement correctly while maintaining O(n),
    # we can't just run LCA and then a separate search. 
    # We must ensure the traversal covers the whole tree or use a flag.
    
    # Re-implementing with a more robust existence check:
    # We use a helper that returns (lca_candidate, found_p, found_q)
    
    def robust_dfs(node: TreeNode | None) -> tuple[TreeNode | None, bool, bool]:
        if not node:
            return None, False, False
        
        is_p = (node == p)
        is_q = (node == q)
        
        left_lca, left_p, left_q = robust_dfs(node.left)
        right_lca, right_p, right_q = robust_dfs(node.right)
        
        # Current node's status
        current_p = is_p or left_p or right_p
        current_q = is_q or left_q or right_q
        
        # Determine LCA candidate
        # 1. If LCA found in subtrees, propagate it up
        if left_lca:
            return left_lca, current_p, current_q
        if right_lca:
            return right_lca, current_p, current_q
        
        # 2. If current node is p and q is in a subtree, or vice versa
        if (is_p and (left_q or right_q)) or (is_q and (left_p or right_p)):
            return node, current_p, current_q
            
        # 3. If p is in one subtree and q is in the other
        if (left_p and right_q) or (left_q and right_p):
            return node, current_p, current_q
            
        # 4. If current node is p or q, it's a potential LCA candidate
        if is_p or is_q:
            return node, current_p, current_q
            
        return None, current_p, current_q

    lca_candidate, p_exists, q_exists = robust_dfs(root)
    
    # Only return the candidate if both nodes were confirmed to exist
    return lca_candidate if (p_exists and q_exists) else None