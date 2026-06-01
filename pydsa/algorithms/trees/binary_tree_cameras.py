METADATA = {
    "id": 968,
    "name": "Binary Tree Cameras",
    "slug": "binary-tree-cameras",
    "category": "Trees",
    "aliases": [],
    "tags": ["dp", "greedy", "dfs"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the minimum number of cameras needed to monitor all nodes in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Calculates the minimum number of cameras needed to monitor all nodes in a binary tree.
    
    The algorithm uses a greedy post-order traversal. Each node can be in one of 
    three states:
    0: Node is NOT covered.
    1: Node HAS a camera.
    2: Node IS covered (but has no camera).

    Args:
        root: The root of the binary tree.

    Returns:
        The minimum number of cameras required.

    Examples:
        >>> root = TreeNode(0)
        >>> solve(root)
        1
        >>> root = TreeNode(0, TreeNode(1), TreeNode(2))
        >>> solve(root)
        1
    """
    camera_count = 0

    def dfs(node: TreeNode) -> int:
        nonlocal camera_count

        if not node:
            # Base case: An empty node is considered 'covered' so it doesn't 
            # force its parent to place a camera.
            return 2

        left_state = dfs(node.left)
        right_state = dfs(node.right)

        # If any child is NOT covered, the current node MUST have a camera.
        if left_state == 0 or right_state == 0:
            camera_count += 1
            return 1

        # If any child has a camera, the current node is now covered.
        if left_state == 1 or right_state == 1:
            return 2

        # If both children are covered but have no cameras, the current node 
        # is now 'uncovered' and needs its parent to provide coverage.
        return 0

    # If the root itself ends up uncovered, we must place a camera on it.
    if dfs(root) == 0:
        camera_count += 1

    return camera_count
