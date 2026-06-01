METADATA = {
    "id": 314,
    "name": "Binary Tree Vertical Order Traversal",
    "slug": "binary-tree-vertical-order-traversal",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "hash_map", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the vertical order traversal of nodes' values in a binary tree.",
}

from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> list[list[int]]:
    """
    Performs a vertical order traversal of a binary tree using BFS.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of lists, where each sub-list contains the values of nodes 
        at a specific vertical column, ordered from top to bottom.

    Examples:
        >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        >>> solve(root)
        [[9], [3], [20], [15, 7]]
    """
    if not root:
        return []

    # column_map stores {horizontal_distance: [node_values]}
    column_map = defaultdict(list)
    
    # Queue stores tuples of (node, horizontal_distance)
    # BFS ensures we process nodes level by level (top to bottom)
    queue = deque([(root, 0)])
    
    # Track min and max column indices to avoid sorting keys later
    min_col = max_col = 0

    while queue:
        current_node, column = queue.popleft()

        if current_node:
            column_map[column].append(current_node.val)
            
            # Update the range of columns encountered
            min_col = min(min_col, column)
            max_col = max(max_col, column)

            # Left child has distance - 1, Right child has distance + 1
            if current_node.left:
                queue.append((current_node.left, column - 1))
            if current_node.right:
                queue.append((current_node.right, column + 1))

    # Construct the result list using the tracked column range
    # This is O(k) where k is the number of columns, effectively O(n)
    result = []
    for col in range(min_col, max_col + 1):
        result.append(column_map[col])

    return result