METADATA = {
    "id": 538,
    "name": "Convert BST to Greater Tree",
    "slug": "convert-bst-to-greater-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "reverse_in_order_traversal", "binary-search-tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Transform a Binary Search Tree such that each node's value is replaced by the sum of all nodes greater than or equal to the original value.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> TreeNode | None:
    """
    Converts a Binary Search Tree (BST) into a Greater Tree.
    
    In a Greater Tree, every node's value is replaced by the sum of all 
    values in the original BST that are greater than or equal to the 
    original value of that node.

    Args:
        root: The root node of the Binary Search Tree.

    Returns:
        The root of the modified tree.

    Examples:
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
        >>> solve(root)
        TreeNode(val=13, left=TreeNode(val=6, left=TreeNode(val=3, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=6)), right=TreeNode(val=6))
        # Note: The example output structure depends on the specific tree shape.
    """
    # running_sum tracks the cumulative sum of all nodes visited so far
    # in a reverse in-order traversal (Right -> Root -> Left).
    running_sum = 0

    def reverse_in_order(node: TreeNode | None) -> None:
        nonlocal running_sum
        if not node:
            return

        # 1. Traverse the right subtree first (contains larger values)
        reverse_in_order(node.right)

        # 2. Process the current node: update running sum and update node value
        running_sum += node.val
        node.val = running_sum

        # 3. Traverse the left subtree (contains smaller values)
        reverse_in_order(node.left)

    reverse_in_order(root)
    return root
