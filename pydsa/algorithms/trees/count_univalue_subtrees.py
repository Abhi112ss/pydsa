METADATA = {
    "id": 250,
    "name": "Count Univalue Subtrees",
    "slug": "count-univalue-subtrees",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "recursion", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Count the number of subtrees that have all nodes with the same value.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Counts the number of univalue subtrees in a binary tree.
    
    A univalue subtree is a subtree where all nodes have the same value.

    Args:
        root: The root node of the binary tree.

    Returns:
        The total count of univalue subtrees.

    Examples:
        >>> root = TreeNode(5, TreeNode(1, TreeNode(5), TreeNode(5)), TreeNode(5))
        >>> solve(root)
        4
    """
    count = 0

    def is_univalue(node: TreeNode | None) -> bool:
        nonlocal count
        
        # Base case: an empty node is technically univalue for its parent's check
        if not node:
            return True

        # Post-order traversal: check children first
        left_is_unival = is_univalue(node.left)
        right_is_unival = is_univalue(node.right)

        # If either child is not a univalue subtree, this node cannot be one
        if not left_is_unival or not right_is_unival:
            return False

        # Check if left child exists and has a different value
        if node.left and node.left.val != node.val:
            return False

        # Check if right child exists and has a different value
        if node.right and node.right.val != node.val:
            return False

        # If all conditions met, this node is the root of a univalue subtree
        count += 1
        return True

    is_univalue(root)
    return count
