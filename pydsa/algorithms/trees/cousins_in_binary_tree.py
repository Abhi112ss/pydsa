METADATA = {
    "id": 993,
    "name": "Cousins in Binary Tree",
    "slug": "cousins-in-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "dfs", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if two nodes in a binary tree are cousins by checking if they share the same depth but have different parents.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None, x: int, y: int) -> bool:
    """
    Determines if two nodes x and y are cousins in a binary tree.
    Cousins share the same depth but have different parents.

    Args:
        root: The root of the binary tree.
        x: The value of the first node.
        y: The value of the second node.

    Returns:
        True if x and y are cousins, False otherwise.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        >>> solve(root, 5, 4)
        False
        >>> solve(root, 5, 3)
        False
        >>> solve(root, 4, 5)
        False
    """
    if not root:
        return False

    # We need to track (depth, parent_value) for both target nodes
    # target_info will store {value: (depth, parent_val)}
    target_info: dict[int, tuple[int, int]] = {}

    def dfs(node: TreeNode | None, parent_val: int, depth: int) -> None:
        if not node:
            return

        # If we found one of the target values, record its depth and parent
        if node.val == x or node.val == y:
            target_info[node.val] = (depth, parent_val)

        # Optimization: if both are found, we can stop early (though standard DFS continues)
        if len(target_info) == 2:
            return

        dfs(node.left, node.val, depth + 1)
        dfs(node.right, node.val, depth + 1)

    # Start DFS from root with depth 0 and no parent (using -1 or None)
    dfs(root, -1, 0)

    # Check if both nodes were found in the tree
    if x not in target_info or y not in target_info:
        return False

    depth_x, parent_x = target_info[x]
    depth_y, parent_y = target_info[y]

    # Cousins must have the same depth but different parents
    return depth_x == depth_y and parent_x != parent_y