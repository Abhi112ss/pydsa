METADATA = {
    "id": 938,
    "name": "Range Sum of BST",
    "slug": "range-sum-of-bst",
    "category": "Trees",
    "aliases": [],
    "tags": ["binary_search_tree", "dfs", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Calculate the sum of values of all nodes in a binary search tree that fall within a given range [low, high].",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, low: int, high: int) -> int:
    """
    Args:
        root: The root node of the binary search tree.
        low: The lower bound of the range.
        high: The upper bound of the range.

    Returns:
        The sum of all node values within the range [low, high].
    """
    if not root:
        return 0

    if root.val < low:
        return solve(root.right, low, high)

    if root.val > high:
        return solve(root.left, low, high)

    return root.val + solve(root.left, low, high) + solve(root.right, low, high)