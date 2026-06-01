METADATA = {
    "id": 230,
    "name": "Kth Smallest Element in a BST",
    "slug": "kth-smallest-element-in-a-bst",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "in_order", "binary-search-tree"],
    "difficulty": "medium",
    "time_complexity": "O(H + k)",
    "space_complexity": "O(H)",
    "description": "Find the kth smallest element in a Binary Search Tree using in-order traversal.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, k: int) -> int:
    """
    Finds the kth smallest element in a Binary Search Tree.

    Args:
        root: The root node of the Binary Search Tree.
        k: The rank of the element to find (1-indexed).

    Returns:
        The value of the kth smallest element.

    Examples:
        >>> root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4, None, TreeNode(5)))
        >>> solve(root, 1)
        1
        >>> solve(root, 3)
        3
    """
    # We use an iterative approach with a stack to perform in-order traversal.
    # This allows us to stop immediately once we reach the kth element,
    # achieving O(H + k) time complexity.
    stack: list[TreeNode] = []
    current_node: TreeNode | None = root
    count = 0

    while stack or current_node:
        # Reach the leftmost node of the current subtree
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        # Process the node
        current_node = stack.pop()
        count += 1
        
        # If the current count matches k, we found our target
        if count == k:
            return current_node.val

        # Move to the right subtree
        current_node = current_node.right

    raise ValueError("k is larger than the number of nodes in the tree.")
