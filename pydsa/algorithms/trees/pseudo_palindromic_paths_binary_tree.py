METADATA = {
    "id": 1457,
    "name": "Pseudo-Palindromic Paths in a Binary Tree",
    "slug": "pseudo_palindromic_paths_in_a_binary_tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "bit_manipulation", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Count the number of paths from root to leaf that can be rearranged into a palindrome.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Counts the number of pseudo-palindromic paths from the root to any leaf.
    
    A path is pseudo-palindromic if it can be rearranged into a palindrome.
    This is true if and only if at most one digit appears an odd number of times.

    Args:
        root: The root of the binary tree.

    Returns:
        The total number of pseudo-palindromic paths.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(2), TreeNode(3)), TreeNode(2, TreeNode(2), TreeNode(3)))
        >>> solve(root)
        3
    """
    if not root:
        return 0

    def dfs(node: TreeNode, bitmask: int) -> int:
        # Toggle the bit corresponding to the current node's value.
        # If the bit is 0, it becomes 1 (odd frequency). If 1, it becomes 0 (even frequency).
        bitmask ^= (1 << node.val)

        # Check if we reached a leaf node
        if not node.left and not node.right:
            # A path is pseudo-palindromic if at most one bit is set in the mask.
            # (bitmask & (bitmask - 1)) == 0 is a trick to check if zero or one bit is set.
            return 1 if (bitmask & (bitmask - 1)) == 0 else 0

        count = 0
        if node.left:
            count += dfs(node.left, bitmask)
        if node.right:
            count += dfs(node.right, bitmask)
            
        return count

    return dfs(root, 0)
