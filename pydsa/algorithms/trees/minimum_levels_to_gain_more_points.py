METADATA = {
    "id": 3096,
    "name": "Minimum Levels to Gain More Points",
    "slug": "minimum-levels-to-gain-more-points",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "bfs", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of levels required to ensure the sum of values at these levels is strictly greater than the sum of values at the remaining levels.",
}

from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the minimum number of levels needed to have a sum strictly greater 
    than the sum of the remaining levels.

    Args:
        root: The root of the binary tree.

    Returns:
        The minimum number of levels (1-indexed) required.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        1
    """
    if not root:
        return 0

    level_sums = []
    queue = deque([root])

    # Perform BFS to calculate the sum of values at each level
    while queue:
        level_size = len(queue)
        current_level_sum = 0
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        level_sums.append(current_level_sum)

    total_sum = sum(level_sums)
    prefix_sum = 0
    
    # Iterate through levels and check if prefix sum > remaining sum
    # remaining_sum = total_sum - prefix_sum
    # We need: prefix_sum > total_sum - prefix_sum  => 2 * prefix_sum > total_sum
    for index, level_sum in enumerate(level_sums):
        prefix_sum += level_sum
        if 2 * prefix_sum > total_sum:
            return index + 1

    return len(level_sums)
