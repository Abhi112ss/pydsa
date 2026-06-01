METADATA = {
    "id": 549,
    "name": "Binary Tree Longest Consecutive Sequence II",
    "slug": "binary-tree-longest-consecutive-sequence-ii",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the length of the longest consecutive sequence in a binary tree where values must be strictly increasing or decreasing.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Finds the length of the longest consecutive sequence in a binary tree.
    A sequence is consecutive if each subsequent node's value is exactly 
    val + 1 or val - 1 relative to the previous node in the path.

    Args:
        root: The root of the binary tree.

    Returns:
        The length of the longest consecutive sequence.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(0))
        >>> solve(root)
        3
    """
    if not root:
        return 0

    max_length = 0

    def dfs(node: TreeNode | None) -> tuple[int, int]:
        """
        Performs a post-order traversal to calculate sequences.
        
        Returns:
            A tuple (inc_len, dec_len) where:
            inc_len: length of longest increasing sequence ending at this node.
            dec_len: length of longest decreasing sequence ending at this node.
        """
        nonlocal max_length
        if not node:
            return 0, 0

        # Post-order traversal: process children first
        left_inc, left_dec = dfs(node.left)
        right_inc, right_dec = dfs(node.right)

        # Initialize current node's sequences as length 1
        current_inc = 1
        current_dec = 1

        # Check left child for continuity
        if node.left:
            if node.left.val + 1 == node.val:
                current_inc = max(current_inc, left_inc + 1)
            elif node.left.val - 1 == node.val:
                current_dec = max(current_dec, left_dec + 1)

        # Check right child for continuity
        if node.right:
            if node.right.val + 1 == node.val:
                current_inc = max(current_inc, right_inc + 1)
            elif node.right.val - 1 == node.val:
                current_dec = max(current_dec, right_dec + 1)

        # Update the global maximum found so far
        max_length = max(max_length, current_inc, current_dec)

        return current_inc, current_dec

    dfs(root)
    return max_length
