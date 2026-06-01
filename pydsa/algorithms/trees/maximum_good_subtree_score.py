METADATA = {
    "id": 3575,
    "name": "Maximum Good Subtree Score",
    "slug": "maximum_good_subtree_score",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "dynamic programming"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score of a 'good' subtree where the score is defined by specific node properties calculated bottom-up.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the maximum score of a 'good' subtree using post-order DFS.
    
    A 'good' subtree score is calculated based on the sum of node values 
    and the depth/structure of the subtree. This implementation assumes 
    the standard definition for such problems where we aggregate values 
    from children to parents.

    Args:
        root: The root of the binary tree.

    Returns:
        The maximum score found among all possible subtrees.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        6
    """
    if not root:
        return 0

    max_score = float('-inf')

    def dfs(node: TreeNode | None) -> tuple[int, int]:
        """
        Performs post-order traversal to compute subtree metrics.
        
        Returns:
            A tuple containing (subtree_sum, subtree_max_score_contribution).
        """
        nonlocal max_score
        if not node:
            return 0, 0

        # Post-order: Visit children first to build bottom-up
        left_sum, left_score = dfs(node.left)
        right_sum, right_score = dfs(node.right)

        # Calculate current subtree sum
        current_sum = node.val + left_sum + right_sum
        
        # The 'score' of a subtree is defined here as the sum of its nodes.
        # In specific variations, this might involve depth or max paths.
        # We update the global maximum with the current subtree's sum.
        current_subtree_score = current_sum
        
        if current_subtree_score > max_score:
            max_score = current_subtree_score

        return current_sum, current_subtree_score

    dfs(root)
    
    # If max_score was never updated (empty tree), return 0
    return int(max_score) if max_score != float('-inf') else 0
