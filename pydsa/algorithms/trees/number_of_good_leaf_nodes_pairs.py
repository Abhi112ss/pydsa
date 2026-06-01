METADATA = {
    "id": 1530,
    "name": "Number of Good Leaf Nodes Pairs",
    "slug": "number-of-good-leaf-nodes-pairs",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Count pairs of leaf nodes that have the same value and share a common ancestor with a different value.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Counts the number of pairs of leaf nodes that have the same value and 
    share a common ancestor with a different value.

    Args:
        root: The root of the binary tree.

    Returns:
        The total number of good leaf node pairs.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(2), TreeNode(2)), TreeNode(2))
        >>> solve(root)
        3
    """
    total_good_pairs = 0
    # Dictionary to store counts of leaf values encountered so far, 
    # grouped by the value of their nearest different ancestor.
    # Structure: {ancestor_val: {leaf_val: count}}
    leaf_counts_by_ancestor = {}

    def dfs(node: TreeNode, last_different_ancestor_val: int | None) -> None:
        nonlocal total_good_pairs

        if not node:
            return

        # Check if current node is a leaf
        if not node.left and not node.right:
            current_val = node.val
            if last_different_ancestor_val is not None:
                # If we have a different ancestor, check how many leaves 
                # with the same value were seen under this specific ancestor value
                if last_different_ancestor_val in leaf_counts_by_ancestor:
                    counts = leaf_counts_by_ancestor[last_different_ancestor_val]
                    total_good_pairs += counts.get(current_val, 0)
                
                # Register this leaf under the current different ancestor
                if last_different_ancestor_val not in leaf_counts_by_ancestor:
                    leaf_counts_by_ancestor[last_different_ancestor_val] = {}
                
                counts = leaf_counts_by_ancestor[last_different_ancestor_val]
                counts[current_val] = counts.get(current_val, 0) + 1
            return

        # Determine the value to pass down to children.
        # If the current node's value is different from the ancestor's, 
        # the current node becomes the new 'last_different_ancestor'.
        new_ancestor_val = last_different_ancestor_val
        if last_different_ancestor_val is None or node.val != last_different_ancestor_val:
            new_ancestor_val = node.val

        dfs(node.left, new_ancestor_val)
        dfs(node.right, new_ancestor_val)

    # Start DFS with None as the initial different ancestor
    dfs(root, None)
    return total_good_pairs
