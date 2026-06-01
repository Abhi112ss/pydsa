METADATA = {
    "id": 1379,
    "name": "Find a Corresponding Node of a Binary Tree in a Clone of That Tree",
    "slug": "find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find a node in a cloned tree that has the same value as a target node in the original tree, based on their structural positions.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(original: TreeNode | None, cloned: TreeNode | None, target_val: int) -> TreeNode | None:
    """
    Finds the node in the cloned tree that corresponds to the node with target_val in the original tree.

    The correspondence is defined by the node's position in the tree structure. 
    We traverse both trees simultaneously to ensure we are looking at the same relative position.

    Args:
        original: The root of the original binary tree.
        cloned: The root of the cloned binary tree.
        target_val: The value of the node we are looking for in the original tree.

    Returns:
        The corresponding node in the cloned tree, or None if not found.

    Examples:
        >>> original = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        >>> cloned = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        >>> solve(original, cloned, 1)
        <TreeNode object at ...> (the node with value 1)
    """
    if not original or not cloned:
        return None

    # If the current node in the original tree matches the target value,
    # then the current node in the cloned tree is the corresponding node.
    if original.val == target_val:
        return cloned

    # Recursively search in the left subtree.
    # We must traverse both trees in lock-step to maintain structural correspondence.
    left_result = solve(original.left, cloned.left, target_val)
    if left_result:
        return left_result

    # If not found in the left subtree, search in the right subtree.
    return solve(original.right, cloned.right, target_val)

# Note: While the prompt mentions hash_map in tags, the optimal approach 
# for this specific problem is a simultaneous DFS traversal which avoids 
# the extra space of a hash map for storing paths, though both are O(n).