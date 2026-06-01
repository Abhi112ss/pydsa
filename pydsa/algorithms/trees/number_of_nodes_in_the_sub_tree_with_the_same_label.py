METADATA = {
    "id": 1519,
    "name": "Number of Nodes in the Sub-Tree With the Same Label",
    "slug": "number-of-nodes-in-the-sub-tree-with-the-same-label",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count how many nodes in each subtree have the same label as the root of that subtree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> int:
    """
    Calculates the total number of nodes in all subtrees that have the same label 
    as the root of their respective subtree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The total count of nodes satisfying the condition.

    Examples:
        >>> root = TreeNode(1, TreeNode(1), TreeNode(2))
        >>> solve(root)
        1
        >>> root = TreeNode(1, TreeNode(1), TreeNode(1))
        >>> solve(root)
        2
    """
    if not root:
        return 0

    total_count = 0

    def dfs(node: TreeNode | None) -> dict[int, int]:
        """
        Performs a post-order DFS to count label frequencies in subtrees.

        Args:
            node: The current node being visited.

        Returns:
            A dictionary mapping labels to their frequency in the current subtree.
        """
        nonlocal total_count
        if not node:
            return {}

        # Post-order traversal: process children first
        left_counts = dfs(node.left)
        right_counts = dfs(node.right)

        # Merge counts from left and right subtrees into the current node's map
        # We start with the current node's own label
        current_counts = {node.val: 1}
        
        # Combine counts from left child
        for label, count in left_counts.items():
            current_counts[label] = current_counts.get(label, 0) + count
            
        # Combine counts from right child
        for label, count in right_counts.items():
            current_counts[label] = current_counts.get(label, 0) + count

        # If the current node's label appears more than once in this subtree,
        # add (frequency - 1) to the total count.
        # The -1 accounts for the root node itself not being counted as its own 'duplicate'.
        if node.val in current_counts:
            total_count += current_counts[node.val] - 1

        return current_counts

    dfs(root)
    return total_count
