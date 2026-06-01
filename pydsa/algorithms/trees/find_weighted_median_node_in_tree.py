METADATA = {
    "id": 3585,
    "name": "Find Weighted Median Node in Tree",
    "slug": "find_weighted_median_node_in_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "binary search", "prefix sum"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the node in a tree such that the sum of weights of nodes in its subtree is at least half of the total weight, following a specific median definition.",
}

class TreeNode:
    def __init__(self, val: int, weight: int):
        self.val = val
        self.weight = weight
        self.children: list["TreeNode"] = []

def solve(root: TreeNode) -> int:
    """
    Finds the weighted median node in a tree.
    
    The weighted median node is defined as the node where the sum of weights 
    in its subtree is the smallest value that is greater than or equal to 
    half of the total weight of all nodes in the tree.

    Args:
        root: The root node of the tree.

    Returns:
        The value of the weighted median node.

    Examples:
        >>> root = TreeNode(1, 10)
        >>> root.children = [TreeNode(2, 20), TreeNode(3, 30)]
        >>> solve(root)
        3
    """
    if not root:
        return -1

    # Map to store the total weight of the subtree rooted at each node
    subtree_weights: dict[int, int] = {}
    # List to store (subtree_weight, node_value) pairs for sorting
    weight_pairs: list[tuple[int, int]] = []

    def calculate_subtree_weights(node: TreeNode) -> int:
        """DFS to calculate the sum of weights for every subtree."""
        current_weight = node.weight
        for child in node.children:
            current_weight += calculate_subtree_weights(child)
        
        subtree_weights[node.val] = current_weight
        weight_pairs.append((current_weight, node.val))
        return current_weight

    # Step 1: Perform DFS to aggregate weights
    total_weight = calculate_subtree_weights(root)
    
    # Step 2: Sort the subtree weights to find the median threshold
    # We sort by weight to find the first node that satisfies the condition
    weight_pairs.sort()

    # The target is the smallest weight >= total_weight / 2
    # Note: In some definitions of weighted median, we look for the 
    # element that splits the total weight.
    target = (total_weight + 1) // 2
    
    # Step 3: Binary search or linear scan to find the first weight >= target
    # Since we need the node whose subtree weight is the smallest value >= target
    # and we have sorted the pairs, we can use binary search.
    import bisect
    
    # Extract only the weights for bisect_left
    sorted_weights = [pair[0] for pair in weight_pairs]
    idx = bisect.bisect_left(sorted_weights, target)
    
    # Return the value of the node at that index
    return weight_pairs[idx][1]
