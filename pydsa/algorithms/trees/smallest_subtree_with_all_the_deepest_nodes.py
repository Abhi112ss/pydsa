METADATA = {
    "id": 865,
    "name": "Smallest Subtree with all the Deepest Nodes",
    "slug": "smallest-subtree-with-all-the-deepest-nodes",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "recursion", "lowest_common_ancestor"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the smallest subtree that contains all the deepest nodes in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> TreeNode | None:
    """
    Finds the smallest subtree that contains all the deepest nodes in the binary tree.

    The algorithm uses a post-order traversal (DFS) to determine the maximum depth 
    of each subtree. For every node, we compare the depths of its left and right 
    children. If the depths are equal, the current node is the lowest common 
    ancestor of all deepest nodes found so far in its subtree.

    Args:
        root: The root of the binary tree.

    Returns:
        The root node of the smallest subtree containing all deepest nodes.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3, None, TreeNode(4)))
        >>> solve(root).val
        3
    """
    if not root:
        return None

    def dfs(node: TreeNode | None) -> tuple[int, TreeNode | None]:
        """
        Helper function that returns a tuple of (max_depth, candidate_node).

        Args:
            node: The current node being visited.

        Returns:
            A tuple containing the depth of the subtree and the node that 
            is the root of the smallest subtree containing all deepest nodes 
            within this subtree.
        """
        if not node:
            return 0, None

        # Post-order traversal: visit children first
        left_depth, left_candidate = dfs(node.left)
        right_depth, right_candidate = dfs(node.right)

        # Case 1: Left subtree is deeper, so the deepest nodes are only in the left
        if left_depth > right_depth:
            return left_depth + 1, left_candidate

        # Case 2: Right subtree is deeper, so the deepest nodes are only in the right
        if right_depth > left_depth:
            return right_depth + 1, right_candidate

        # Case 3: Depths are equal, meaning the deepest nodes are distributed 
        # across both subtrees (or this node is the deepest node itself).
        # Therefore, the current node is the smallest subtree root for this level.
        return left_depth + 1, node

    _, result_node = dfs(root)
    return result_node