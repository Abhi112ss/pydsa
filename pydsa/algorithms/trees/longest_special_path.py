METADATA = {
    "id": 3425,
    "name": "Longest Special Path",
    "slug": "longest_special_path",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "dfs", "depth_first_search"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the longest path in a tree where no two nodes in the path have the same value.",
}

class TreeNode:
    def __init__(self, val: int = 0, children: list["TreeNode"] = None):
        self.val = val
        self.children = children if children is not None else []

def solve(root: TreeNode) -> int:
    """
    Finds the length of the longest path in a tree such that all nodes in the path 
    have distinct values.

    Args:
        root: The root of the tree.

    Returns:
        The maximum number of edges in a valid path.

    Examples:
        >>> root = TreeNode(1, [TreeNode(2), TreeNode(1)])
        >>> solve(root)
        1
    """
    max_path_length = 0
    # last_seen_depth maps a node value to the depth at which it was last encountered
    # in the current DFS path.
    last_seen_depth = {}

    def dfs(node: TreeNode, current_depth: int) -> None:
        nonlocal max_path_length
        
        # Store the previous depth of this value to restore it after backtracking
        prev_depth = last_seen_depth.get(node.val, -1)
        
        # The 'valid_start_depth' is the depth of the highest ancestor that 
        # would cause a duplicate value if included in the path.
        # We use a local variable to track the constraint for the current subtree.
        # However, to handle the path correctly, we need to know the depth of the 
        # most recent duplicate ancestor.
        
        # We use a stack-like approach via the recursion to find the nearest 
        # ancestor with the same value.
        # To find the longest path ending at 'node', we need to know the depth 
        # of the nearest ancestor with the same value.
        
        # We'll use a list to keep track of the 'effective' starting depth 
        # for the current path to avoid duplicates.
        # Since we need to pass this constraint down, we'll use a helper.
        pass

    # Re-implementing with a more robust approach for the constraint tracking
    max_len = 0
    # depth_map stores the depth of the last occurrence of a value in the current path
    depth_map = {}

    def traverse(node: TreeNode, depth: int, constraint_depth: int) -> None:
        nonlocal max_len
        
        # If this value was seen before in the current path, 
        # the new constraint depth is the maximum of the current constraint 
        # and the depth of that previous occurrence.
        new_constraint_depth = constraint_depth
        if node.val in depth_map:
            new_constraint_depth = max(new_constraint_depth, depth_map[node.val])
        
        # The length of the valid path ending at this node is (current_depth - constraint_depth)
        # Note: constraint_depth is the depth of the ancestor that violates the rule.
        # If constraint_depth is 0, it means no ancestor violates the rule (using 1-based depth logic).
        # Let's use 0-based depth and treat constraint_depth as the depth of the "bad" node.
        # If no bad node, constraint_depth = -1.
        
        # Update max length: current depth minus the depth of the nearest invalid ancestor.
        # If constraint_depth is -1, path length is depth - (-1) - 1 = depth.
        # Wait, if depth is 0 and constraint is -1, length is 0. Correct.
        max_len = max(max_len, depth - new_constraint_depth - 1)
        
        # Save old depth to restore after DFS (backtracking)
        old_depth = depth_map.get(node.val, -1)
        depth_map[node.val] = depth
        
        for child in node.children:
            traverse(child, depth + 1, new_constraint_depth)
            
        # Backtrack: restore the previous depth of this value
        if old_depth == -1:
            del depth_map[node.val]
        else:
            depth_map[node.val] = old_depth

    # Start DFS: depth 0, constraint_depth -1
    traverse(root, 0, -1)
    return max_len

# The problem description implies a tree structure. 
# The logic above uses a DFS to maintain a path and a hash map to track 
# the depth of the most recent occurrence of each value.
# The 'constraint_depth' ensures that for any node, we only consider 
# the segment of the path that contains unique values.
