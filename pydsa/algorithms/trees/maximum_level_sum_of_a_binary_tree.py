METADATA = {
    "id": 1161,
    "name": "Maximum Level Sum of a Binary Tree",
    "slug": "maximum-level-sum-of-a-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
    "description": "Find the level in a binary tree that has the maximum sum of node values, returning the smallest level index in case of ties.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Finds the level with the maximum sum in a binary tree using Breadth-First Search.

    Args:
        root: The root node of the binary tree.

    Returns:
        The 1-based index of the level with the maximum sum. If multiple levels 
        have the same maximum sum, the smallest level index is returned.

    Examples:
        >>> root = TreeNode(1, TreeNode(7, TreeNode(0, TreeNode(-8))), TreeNode(3, TreeNode(2, TreeNode(5), TreeNode(-1)), TreeNode(4)))
        >>> solve(root)
        4
    """
    if not root:
        return 0

    max_sum = float('-inf')
    max_level = 1
    current_level = 1
    
    # Use a queue for level-order traversal (BFS)
    queue = [root]

    while queue:
        level_sum = 0
        level_size = len(queue)
        
        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Update max_sum and max_level if a strictly greater sum is found
        # This naturally handles the "smallest level index" requirement for ties
        if level_sum > max_sum:
            max_sum = level_sum
            max_level = current_level
            
        current_level += 1

    return max_level
