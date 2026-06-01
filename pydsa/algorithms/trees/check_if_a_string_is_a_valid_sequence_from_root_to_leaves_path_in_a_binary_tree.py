METADATA = {
    "id": 1430,
    "name": "Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree",
    "slug": "check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "binary tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if a given string represents a valid sequence of node values from the root to a leaf in a binary tree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, sequence: list[int]) -> bool:
    """
    Checks if the sequence of integers exists as a path from root to leaf.

    Args:
        root: The root node of the binary tree.
        sequence: A list of integers representing the target path.

    Returns:
        True if the sequence is a valid root-to-leaf path, False otherwise.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
        >>> solve(root, [1, 2, 3])
        True
        >>> solve(root, [1, 2, 4])
        True
        >>> solve(root, [1, 5])
        True
        >>> solve(root, [1, 2])
        False
    """
    n = len(sequence)

    def dfs(node: TreeNode, index: int) -> bool:
        # Base case: if node is null, this path is invalid
        if not node:
            return False

        # Check if current node value matches the sequence value at current index
        if node.val != sequence[index]:
            return False

        # If we reached the end of the sequence, check if current node is a leaf
        if index == n - 1:
            return node.left is None and node.right is None

        # If we haven't reached the end of the sequence, continue DFS to children
        # We only proceed if there is a next element in the sequence
        if index + 1 < n:
            # Try left child first, then right child
            return dfs(node.left, index + 1) or dfs(node.right, index + 1)
        
        return False

    return dfs(root, 0)
