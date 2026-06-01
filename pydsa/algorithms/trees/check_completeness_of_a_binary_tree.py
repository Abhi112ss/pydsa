METADATA = {
    "id": 958,
    "name": "Check Completeness of a Binary Tree",
    "slug": "check-completeness-of-a-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "tree_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a binary tree is complete, meaning all levels are fully filled except possibly the last, which is filled from left to right.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> bool:
    """
    Checks if a binary tree is complete using Breadth-First Search (BFS).
    
    A complete binary tree is one where every level, except possibly the last, 
    is completely filled, and all nodes in the last level are as far left as possible.
    In a BFS traversal, once a null child is encountered, no non-null nodes 
    should appear afterwards.

    Args:
        root: The root node of the binary tree.

    Returns:
        True if the tree is complete, False otherwise.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        True
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
        >>> solve(root)
        False
    """
    if not root:
        return True

    from collections import deque

    queue = deque([root])
    # This flag tracks if we have encountered a null node during BFS.
    # Once a null is seen, any subsequent non-null node violates completeness.
    has_seen_null = False

    while queue:
        current_node = queue.popleft()

        if current_node:
            # If we previously encountered a null node but now find a real node,
            # the tree is not complete.
            if has_seen_null:
                return False
            
            # Add children to the queue (including None/null children)
            queue.append(current_node.left)
            queue.append(current_node.right)
        else:
            # Mark that we have encountered a gap in the tree structure.
            has_seen_null = True

    return True
