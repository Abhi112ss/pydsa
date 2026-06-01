METADATA = {
    "id": 669,
    "name": "Trim a Binary Search Tree",
    "slug": "trim-a-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["recursion", "bst", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Given the root of a binary search tree and a range [low, high], trim the tree so that all its elements lie in the range.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, low: int, high: int) -> TreeNode | None:
    """
    Trims a Binary Search Tree so that all nodes fall within the range [low, high].

    Args:
        root: The root node of the binary search tree.
        low: The lower bound of the range (inclusive).
        high: The upper bound of the range (inclusive).

    Returns:
        The root of the trimmed binary search tree.

    Examples:
        >>> root = TreeNode(3, TreeNode(0, TreeNode(-1), TreeNode(2)), TreeNode(4, TreeNode(None, None, TreeNode(1)), TreeNode(5)))
        >>> new_root = solve(root, 1, 3)
        >>> new_root.val
        3
    """
    if not root:
        return None

    # If the current node's value is less than the low bound, 
    # then this node and its entire left subtree are out of range.
    # We discard them and move to the right subtree.
    if root.val < low:
        return solve(root.right, low, high)

    # If the current node's value is greater than the high bound,
    # then this node and its entire right subtree are out of range.
    # We discard them and move to the left subtree.
    if root.val > high:
        return solve(root.left, low, high)

    # If the current node is within the range, we recursively trim
    # its left and right children and then link them back.
    root.left = solve(root.left, low, high)
    root.right = solve(root.right, low, high)

    return root