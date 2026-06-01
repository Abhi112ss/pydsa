METADATA = {
    "id": 701,
    "name": "Insert into a Binary Search Tree",
    "slug": "insert-into-a-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["binary_search_tree", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(H)",
    "space_complexity": "O(H)",
    "description": "Insert a value into a binary search tree and return the root of the modified tree.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, val: int) -> TreeNode | None:
    """
    Inserts a value into a Binary Search Tree (BST) while maintaining BST properties.

    Args:
        root: The root node of the binary search tree.
        val: The integer value to be inserted into the tree.

    Returns:
        The root node of the modified binary search tree.

    Examples:
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        >>> new_root = solve(root, 5)
        >>> new_root.val == 4
        True
    """
    # Base case: if we reach a null position, we've found the insertion point
    if not root:
        return TreeNode(val)

    # If the value is less than the current node, traverse the left subtree
    if val < root.val:
        root.left = solve(root.left, val)
    # If the value is greater than the current node, traverse the right subtree
    else:
        root.right = solve(root.right, val)

    # Return the (potentially modified) current node to its parent
    return root

def solve_iterative(root: TreeNode | None, val: int) -> TreeNode | None:
    """
    An iterative implementation of the insertion algorithm to achieve O(1) space complexity.

    Args:
        root: The root node of the binary search tree.
        val: The integer value to be inserted into the tree.

    Returns:
        The root node of the modified binary search tree.
    """
    new_node = TreeNode(val)
    if not root:
        return new_node

    current = root
    while True:
        # Decide whether to go left or right
        if val < current.val:
            if current.left:
                current = current.left
            else:
                # Found the insertion point
                current.left = new_node
                break
        else:
            if current.right:
                current = current.right
            else:
                # Found the insertion point
                current.right = new_node
                break
                
    return root