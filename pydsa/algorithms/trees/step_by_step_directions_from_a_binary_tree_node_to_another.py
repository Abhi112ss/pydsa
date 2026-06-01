METADATA = {
    "id": 2096,
    "name": "Step-By-Step Directions From a Binary Tree Node to Another",
    "slug": "step-by-step-directions-from-a-binary-tree-node-to-another",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "binary tree", "lca"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the shortest path from a source node to a destination node in a binary tree using 'U' for up and 'L'/'R' for left/right moves.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, startValue: int, destValue: int) -> str:
    """
    Finds the shortest path from startValue to destValue in a binary tree.

    The algorithm finds the path from the root to both the start and destination nodes.
    By removing the common prefix (the path to the Lowest Common Ancestor), we obtain
    the path from the start node to the LCA (all 'U' moves) and from the LCA to the
    destination node (the remaining 'L'/'R' moves).

    Args:
        root: The root of the binary tree.
        startValue: The value of the starting node.
        destValue: The value of the destination node.

    Returns:
        A string representing the directions ('U', 'L', 'R').

    Examples:
        >>> root = TreeNode(0, TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(4, TreeNode(5), TreeNode(6)))
        >>> solve(root, 3, 6)
        'UUR'
        >>> solve(root, 1, 4)
        'UULR'
    """
    
    def find_path(node: TreeNode, target: int, path: list[str]) -> bool:
        """Helper function to perform DFS and record the path to a target value."""
        if not node:
            return False
        
        if node.val == target:
            return True
        
        # Try moving left
        path.append('L')
        if find_path(node.left, target, path):
            return True
        path.pop()  # Backtrack
        
        # Try moving right
        path.append('R')
        if find_path(node.right, target, path):
            return True
        path.pop()  # Backtrack
        
        return False

    start_path = []
    dest_path = []

    # Step 1: Find paths from root to both nodes
    find_path(root, startValue, start_path)
    find_path(root, destValue, dest_path)

    # Step 2: Find the Lowest Common Ancestor (LCA) by skipping the common prefix
    common_idx = 0
    max_possible_common = min(len(start_path), len(dest_path))
    while (common_idx < max_possible_common and 
           start_path[common_idx] == dest_path[common_idx]):
        common_idx += 1

    # Step 3: Construct the result
    # For every step in start_path that is not in the common prefix, 
    # we must move 'Up' from the start node to reach the LCA.
    up_moves = len(start_path) - common_idx
    
    # The remaining steps in dest_path from the LCA to the destination are the directions.
    down_moves = dest_path[common_idx:]
    
    return ('U' * up_moves) + "".join(down_moves)
