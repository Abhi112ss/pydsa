METADATA = {
    "id": 1382,
    "name": "Balance a Binary Search Tree",
    "slug": "balance-a-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["binary_search_tree", "dfs", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a given binary search tree into a height-balanced binary search tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> TreeNode | None:
    """
    Converts a given Binary Search Tree into a height-balanced BST.

    The algorithm works by first performing an in-order traversal to extract
    the node values in a sorted list, then recursively building a balanced
    tree by picking the middle element of the list as the root.

    Args:
        root: The root of the original binary search tree.

    Returns:
        The root of the new height-balanced binary search tree.

    Examples:
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5, TreeNode(None, None, TreeNode(3)), TreeNode(6)))
        >>> new_root = solve(root)
        >>> # new_root is a balanced BST
    """
    sorted_values: list[int] = []

    def in_order_traversal(node: TreeNode | None) -> None:
        """Extracts values from the BST in sorted order."""
        if not node:
            return
        in_order_traversal(node.left)
        sorted_values.append(node.val)
        in_order_traversal(node.right)

    def build_balanced_bst(left_index: int, right_index: int) -> TreeNode | None:
        """Recursively builds a balanced BST from a sorted list slice."""
        if left_index > right_index:
            return None

        # Pick the middle element to ensure the tree remains balanced
        mid = (left_index + right_index) // 2
        node = TreeNode(sorted_values[mid])

        # Recursively construct left and right subtrees
        node.left = build_balanced_bst(left_index, mid - 1)
        node.right = build_balanced_bst(mid + 1, right_index)
        
        return node

    # Step 1: Get sorted elements via in-order traversal
    in_order_traversal(root)

    # Step 2: Reconstruct the tree using the sorted list
    return build_balanced_bst(0, len(sorted_values) - 1)