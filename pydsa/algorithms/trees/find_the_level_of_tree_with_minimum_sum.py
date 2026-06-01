METADATA = {
    "id": 3157,
    "name": "Find the Level of Tree with Minimum Sum",
    "slug": "find-the-level-of-tree-with-minimum-sum",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the level index (starting from 0) of the tree that has the minimum sum of node values using BFS.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Finds the level index of the tree with the minimum sum of node values.

    Args:
        root: The root node of the binary tree.

    Returns:
        The 0-indexed level with the minimum sum. If multiple levels have 
        the same minimum sum, the smallest level index is returned.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        0
        >>> root = TreeNode(1, TreeNode(-5), TreeNode(3, TreeNode(10), TreeNode(-20)))
        >>> solve(root)
        2
    """
    if not root:
        return -1

    # Initialize tracking for the minimum sum found and its corresponding level
    min_sum = float('inf')
    min_level_index = 0
    
    # Queue for BFS: stores nodes at the current level
    queue = [root]
    current_level_index = 0

    while queue:
        level_size = len(queue)
        current_level_sum = 0
        next_level_queue = []

        # Process all nodes at the current level
        for i in range(level_size):
            node = queue[i]
            current_level_sum += node.val
            
            # Prepare children for the next level
            if node.left:
                next_level_queue.append(node.left)
            if node.right:
                next_level_queue.append(node.right)

        # Update the global minimum sum and its level index
        # We use '<' to ensure we keep the smallest index in case of ties
        if current_level_sum < min_sum:
            min_sum = current_level_sum
            min_level_index = current_level_index

        # Move to the next level
        queue = next_level_queue
        current_level_index += 1

    return min_level_index
