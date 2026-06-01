METADATA = {
    "id": 687,
    "name": "Longest Univalue Path",
    "slug": "longest-univalue-path",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the length of the longest path in a tree where all nodes in the path have the same value.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Finds the length of the longest path in a binary tree where all nodes have the same value.

    The algorithm uses a post-order traversal (DFS). For each node, it calculates the 
    longest univalue path extending into its left and right subtrees. The global 
    maximum is updated by considering the path that passes through the current node 
    (left_leg + right_leg), while the function returns the longest single leg 
    (max(left_leg, right_leg) + 1) to its parent.

    Args:
        root: The root of the binary tree.

    Returns:
        The length of the longest univalue path.

    Examples:
        >>> root = TreeNode(5, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, TreeNode(5)))
        >>> solve(root)
        3
    """
    max_path_length = 0

    def dfs(node: TreeNode | None) -> int:
        nonlocal max_path_length
        if not node:
            return 0

        # Recursively find the longest univalue path starting from children
        left_length = dfs(node.left)
        right_length = dfs(node.right)

        # Variables to track the univalue path length extending from current node
        left_arrow = 0
        right_arrow = 0

        # If left child exists and has the same value, extend the path
        if node.left and node.left.val == node.val:
            left_arrow = left_length + 1
        
        # If right child exists and has the same value, extend the path
        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1

        # Update the global maximum with the path passing through the current node
        # This path combines the left and right univalue legs
        max_path_length = max(max_path_length, left_arrow + right_arrow)

        # Return the longest single leg to the parent node
        return max(left_arrow, right_arrow)

    dfs(root)
    return max_path_length
