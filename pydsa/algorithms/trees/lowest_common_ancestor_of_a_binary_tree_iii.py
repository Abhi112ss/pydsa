METADATA = {
    "id": 1650,
    "name": "Lowest Common Ancestor of a Binary Tree III",
    "slug": "lowest-common-ancestor-of-a-binary-tree-iii",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(h)",
    "space_complexity": "O(1)",
    "description": "Find the lowest common ancestor of two nodes in a binary tree where each node has a pointer to its parent.",
}

class TreeNode:
    def __init__(self, x, parent=None):
        self.val = x
        self.left = None
        self.right = None
        self.parent = parent

def solve(p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor of two nodes in a binary tree where 
    each node has a pointer to its parent.

    This problem is mathematically equivalent to finding the intersection 
    point of two linked lists. By traversing upwards and switching paths 
    once a pointer reaches the root, both pointers will eventually meet 
    at the LCA after at most two traversals.

    Args:
        p (TreeNode): The first node.
        q (TreeNode): The second node.

    Returns:
        TreeNode: The lowest common ancestor node.

    Examples:
        >>> # Assuming a tree structure where p and q are nodes
        >>> solve(p, q)
        <TreeNode object>
    """
    pointer_a = p
    pointer_b = q

    # We use the two-pointer technique for finding the intersection of two linked lists.
    # When pointer_a reaches the root (None), we redirect it to the start of q.
    # When pointer_b reaches the root (None), we redirect it to the start of p.
    # They will meet at the LCA because both will have traveled the same total distance:
    # distance(p to root) + distance(q to root).
    while pointer_a != pointer_b:
        # Move to parent, or switch to the other starting node if root is reached
        pointer_a = pointer_a.parent if pointer_a.parent is not None else q
        pointer_b = pointer_b.parent if pointer_b.parent is not None else p
        
        # Note: In the specific case where the tree is not guaranteed to have a common 
        # ancestor, this loop could run infinitely. However, per problem constraints, 
        # a common ancestor is guaranteed.
        
        # To handle the logic correctly for the 'switch' to avoid infinite loops 
        # in non-existent ancestor scenarios, we use a slightly more robust 
        # version of the intersection logic:
        # If we reach the end of both paths, they meet at None.
        # But since the problem guarantees an ancestor, the logic above works.
        
        # Re-implementing the standard intersection logic to be safer:
        # We use a different approach to avoid the 'None' vs 'Root' ambiguity.
        pass

    # Corrected implementation of the two-pointer intersection logic
    ptr1 = p
    ptr2 = q
    
    while ptr1 != ptr2:
        # If ptr1 reaches the top, jump to q, else move to parent
        ptr1 = ptr1.parent if ptr1.parent else q
        # If ptr2 reaches the top, jump to p, else move to parent
        ptr2 = ptr2.parent if ptr2.parent else p
        
    return ptr1

# Redefining solve to ensure the logic is clean and follows the standard intersection pattern
def solve(p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor of two nodes in a binary tree where 
    each node has a pointer to its parent.

    Args:
        p (TreeNode): The first node.
        q (TreeNode): The second node.

    Returns:
        TreeNode: The lowest common ancestor node.
    """
    a, b = p, q
    
    # The two-pointer approach:
    # Path 1: p -> root -> q
    # Path 2: q -> root -> p
    # Both paths have length: depth(p) + depth(q) + 1 (if we count the None/null step)
    # They are guaranteed to meet at the LCA.
    while a != b:
        # Move to parent, if at root, switch to the other node's starting position
        a = a.parent if a.parent else q
        b = b.parent if b.parent else p
        
    return a