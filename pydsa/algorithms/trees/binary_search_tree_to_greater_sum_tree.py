METADATA = {
    "id": 1038,
    "name": "Binary Search Tree to Greater Sum Tree",
    "slug": "binary-search-tree-to-greater-sum-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "bst", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Transform a Binary Search Tree such that every node's value is replaced by the sum of all nodes greater than or equal to the original value.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> TreeNode | None:
    """
    Transforms a BST into a Greater Sum Tree using reverse in-order traversal.

    In a BST, the nodes in descending order can be visited by performing 
    a Right -> Root -> Left traversal. By maintaining a running sum of 
    visited nodes, we can update each node's value in a single pass.

    Args:
        root: The root of the binary search tree.

    Returns:
        The root of the transformed binary search tree.

    Examples:
        >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
        >>> solve(root).val
        6
    """
    running_sum = 0

    def traverse(node: TreeNode | None) -> None:
        nonlocal running_sum
        if not node:
            return

        # 1. Traverse the right subtree first (contains larger values)
        traverse(node.right)

        # 2. Process the current node: update running sum and node value
        running_sum += node.val
        node.val = running_sum

        # 3. Traverse the left subtree (contains smaller values)
        traverse(node.left)

    traverse(root)
    return root
