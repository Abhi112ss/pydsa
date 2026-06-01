METADATA = {
    "id": 1660,
    "name": "Correct a Binary Tree",
    "slug": "correct-a-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Correct a binary tree where nodes are swapped if their value is less than their parent's value, using a greedy approach to swap the first two incorrect nodes found.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> TreeNode | None:
    """
    Corrects a binary tree where nodes might have been swapped.
    
    The problem states that a node's value should be greater than its parent's value.
    If a node is smaller than its parent, it was swapped. We find the first two 
    such nodes in a pre-order traversal and swap their values.

    Args:
        root: The root of the binary tree.

    Returns:
        The root of the corrected binary tree.

    Examples:
        >>> root = TreeNode(1, TreeNode(3, TreeNode(2)))
        >>> solve(root)
        TreeNode(1, TreeNode(2, TreeNode(3)))
    """
    if not root:
        return None

    # Stores the values of the two nodes that need to be swapped
    # We store them in a list to allow modification inside the helper function
    swappable_nodes: list[TreeNode] = []

    def find_incorrect_nodes(node: TreeNode | None, parent_val: int) -> None:
        """Performs a pre-order DFS to find nodes violating the heap property."""
        if not node:
            return

        # If current node value is less than parent, it's an incorrect node
        if node.val < parent_val:
            swappable_nodes.append(node)
            # If we found two nodes, we can stop searching
            if len(swappable_nodes) == 2:
                return

        # Continue DFS in pre-order (Left then Right)
        find_incorrect_nodes(node.left, node.val)
        if len(swappable_nodes) < 2:
            find_incorrect_nodes(node.right, node.val)

    # Start DFS from root. Root has no parent, so we pass a very small value.
    find_incorrect_nodes(root, float('-inf'))

    # If we found exactly two nodes that violate the property, swap their values
    if len(swappable_nodes) == 2:
        node1, node2 = swappable_nodes
        node1.val, node2.val = node2.val, node1.val

    return root
