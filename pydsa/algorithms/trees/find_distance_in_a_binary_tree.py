METADATA = {
    "id": 1740,
    "name": "Find Distance in a Binary Tree",
    "slug": "find-distance-in-a-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "lowest common ancestor"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the distance between two nodes in a binary tree by finding their lowest common ancestor.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, p: TreeNode, q: TreeNode) -> int:
    """
    Calculates the distance between two nodes in a binary tree.

    The distance is calculated as: dist(p, q) = dist(root, p) + dist(root, q) - 2 * dist(root, LCA(p, q)).
    Alternatively, it is the sum of distances from p to LCA and q to LCA.

    Args:
        root: The root of the binary tree.
        p: The first node.
        q: The second node.

    Returns:
        The integer distance between node p and node q.

    Examples:
        >>> root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(4))
        >>> p = root.left # node 5
        >>> q = root.right # node 4
        >>> solve(root, p, q)
        2
    """

    def find_lca(node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Finds the Lowest Common Ancestor of nodes p and q."""
        if not node or node == p or node == q:
            return node

        left = find_lca(node.left, p, q)
        right = find_lca(node.right, p, q)

        # If both left and right calls return a non-null value, current node is LCA
        if left and right:
            return node
        
        return left if left else right

    def get_distance_from_ancestor(ancestor: TreeNode, target: TreeNode) -> int:
        """Calculates the distance from a given ancestor to a target node using DFS."""
        if not ancestor:
            return -1
        
        if ancestor == target:
            return 0

        # Search in left subtree
        left_dist = get_distance_from_ancestor(ancestor.left, target)
        if left_dist != -1:
            return left_dist + 1

        # Search in right subtree
        right_dist = get_distance_from_ancestor(ancestor.right, target)
        if right_dist != -1:
            return right_dist + 1

        return -1

    # Step 1: Find the Lowest Common Ancestor (LCA)
    lca = find_lca(root, p, q)

    # Step 2: The distance is the sum of distances from LCA to p and LCA to q
    # Since LCA is an ancestor of both p and q, we can use a simple DFS
    dist_p = get_distance_from_ancestor(lca, p)
    dist_q = get_distance_from_ancestor(lca, q)

    return dist_p + dist_q