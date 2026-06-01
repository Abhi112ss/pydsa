METADATA = {
    "id": 515,
    "name": "Find Largest Value in Each Tree Row",
    "slug": "find-largest-value-in-each-tree-row",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "dfs", "tree_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
    "description": "Find the largest value in each row of a binary tree using level-order traversal.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> list[int]:
    """
    Performs a level-order traversal (BFS) to find the maximum value in each row.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of integers where each element is the maximum value found in that row.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        >>> solve(root)
        [1, 3, 5]
    """
    if not root:
        return []

    result = []
    # Use a queue for Breadth-First Search (BFS)
    queue = [root]

    while queue:
        # The number of nodes currently in the queue represents the current row size
        level_size = len(queue)
        # Initialize max_val with the smallest possible integer or the first node's value
        current_row_max = float('-inf')

        for _ in range(level_size):
            # Pop the first element from the queue (simulating a deque)
            node = queue.pop(0)
            
            # Update the maximum value for the current row
            if node.val > current_row_max:
                current_row_max = node.val

            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(int(current_row_max))

    return result
