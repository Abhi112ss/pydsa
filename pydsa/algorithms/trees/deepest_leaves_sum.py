METADATA = {
    "id": 1302,
    "name": "Deepest Leaves Sum",
    "slug": "deepest-leaves-sum",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "dfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
    "description": "Calculate the sum of the values of the deepest leaves in a binary tree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the sum of the values of the deepest leaves in a binary tree using BFS.

    Args:
        root: The root node of the binary tree.

    Returns:
        The sum of the values of the nodes located at the maximum depth.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7))), TreeNode(3, TreeNode(5, TreeNode(6))))
        >>> solve(root)
        13
    """
    if not root:
        return 0

    # Use a queue for level-order traversal (BFS)
    from collections import deque
    queue = deque([root])
    current_level_sum = 0

    while queue:
        # The sum of the current level
        level_size = len(queue)
        current_level_sum = 0
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level_sum += node.val
            
            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # After the loop, if the queue is empty, current_level_sum 
        # holds the sum of the very last level processed.
        # If there are more levels, current_level_sum will be overwritten.
        
    return current_level_sum
