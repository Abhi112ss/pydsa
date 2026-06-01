METADATA = {
    "id": 2313,
    "name": "Minimum Flips in Binary Tree to Get Result",
    "slug": "minimum-flips-in-binary-tree-to-get-result",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the minimum number of flips required to make the value of every node in a binary tree equal to the target value.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, target: int) -> int:
    """
    Calculates the minimum number of flips needed to make all nodes in the tree 
    equal to the target value.

    A flip at a node affects all its descendants. We use a post-order traversal 
    to propagate the 'current' required value from the root down to the leaves.

    Args:
        root: The root of the binary tree.
        target: The target integer value (0 or 1).

    Returns:
        The minimum number of flips required.

    Examples:
        >>> root = TreeNode(1, TreeNode(0), TreeNode(1))
        >>> solve(root, 1)
        1
        >>> root = TreeNode(0, TreeNode(1), TreeNode(1))
        >>> solve(root, 1)
        3
    """
    
    def dfs(node: TreeNode, current_val: int) -> int:
        """
        Helper function to traverse the tree and count flips.

        Args:
            node: The current node being visited.
            current_val: The value this node should have based on flips 
                         performed on its ancestors.

        Returns:
            The total flips required for the subtree rooted at 'node'.
        """
        if not node:
            return 0

        flips = 0
        # If the node's value does not match the value inherited from its 
        # ancestors, we must flip this node.
        if node.val != current_val:
            flips += 1
            # After flipping, the new value for this node and its 
            # descendants becomes the opposite of the current_val.
            current_val = 1 - current_val

        # Recursively calculate flips for left and right subtrees using 
        # the updated current_val.
        flips += dfs(node.left, current_val)
        flips += dfs(node.right, current_val)
        
        return flips

    # Start DFS from the root with the initial target value.
    return dfs(root, target)
