METADATA = {
    "id": 987,
    "name": "Vertical Order Traversal of a Binary Tree",
    "slug": "vertical-order-traversal-of-a-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "bfs", "sorting", "hash_map"],
    "difficulty": "hard",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Return the vertical order traversal of a binary tree where nodes are sorted by column, then row, then value.",
}

from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Performs a vertical order traversal of a binary tree.

    The traversal follows these rules:
    1. Nodes are grouped by their column index.
    2. Within each column, nodes are sorted by their row index.
    3. If two nodes have the same column and row, they are sorted by their value.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of lists, where each inner list contains the values of nodes in a specific column,
        ordered from leftmost column to rightmost column.

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        [[9], [3], [20, 15, 7]]

        >>> root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(6)), TreeNode(7))
        >>> solve(root)
        [[4], [2], [1, 3, 6], [5, 7]]
    """
    if not root:
        return []

    # List to store tuples of (column, row, value)
    # We use (col, row, val) to allow a single sort operation to handle all requirements
    node_coordinates: List[tuple[int, int, int]] = []

    # Use a stack for iterative DFS to collect coordinates
    # Stack stores (node, column, row)
    stack: List[tuple[TreeNode, int, int]] = [(root, 0, 0)]

    while stack:
        current_node, col, row = stack.pop()
        
        if current_node:
            node_coordinates.append((col, row, current_node.val))
            
            # Push right child first so left child is processed first (standard DFS)
            # However, since we collect all and sort later, order of traversal doesn't strictly matter
            if current_node.right:
                stack.append((current_node.right, col + 1, row + 1))
            if current_node.left:
                stack.append((current_node.left, col - 1, row + 1))

    # Sort primarily by column, then by row, then by value
    # Python's Timsort is stable and handles tuple comparison lexicographically
    node_coordinates.sort()

    # Group the sorted values by their column index
    result: List[List[int]] = []
    if not node_coordinates:
        return result

    # Since the list is sorted by column, we can group them linearly
    current_col_idx = node_coordinates[0][0]
    current_col_values: List[int] = []

    for col, row, val in node_coordinates:
        if col == current_col_idx:
            current_col_values.append(val)
        else:
            # New column encountered, push the previous column's list to result
            result.append(current_col_values)
            current_col_idx = col
            current_col_values = [val]

    # Append the final column
    result.append(current_col_values)

    return result
