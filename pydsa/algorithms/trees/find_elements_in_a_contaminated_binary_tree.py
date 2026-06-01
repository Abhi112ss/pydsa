METADATA = {
    "id": 1261,
    "name": "Find Elements in a Contaminated Binary Tree",
    "slug": "find_elements_in_a_contaminated_binary_tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "hash_set", "tree_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reconstruct the set of unique values present in a binary tree using depth-first search.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> set[int]:
    """
    Traverses a binary tree to collect all unique node values into a set.

    Args:
        root: The root node of the binary tree. Can be None.

    Returns:
        A set containing all unique integer values found in the tree.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        {1, 2, 3}
        >>> solve(None)
        set()
    """
    if not root:
        return set()

    unique_elements = set()
    # Use an explicit stack for iterative DFS to avoid recursion depth issues
    stack = [root]

    while stack:
        current_node = stack.pop()
        
        if current_node:
            # Add the current node's value to our collection
            unique_elements.add(current_node.val)
            
            # Push children to the stack to continue traversal
            # Order (right then left) ensures left is processed first in DFS
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

    return unique_elements
