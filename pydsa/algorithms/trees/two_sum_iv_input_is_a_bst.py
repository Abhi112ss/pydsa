METADATA = {
    "id": 653,
    "name": "Two Sum IV - Input is a BST",
    "slug": "two-sum-iv-input-is-a-bst",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "hash_set", "dfs", "bfs"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if there exist two elements in a Binary Search Tree such that their sum equals a given target.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, target: int) -> bool:
    """
    Args:
        root: The root of the binary search tree.
        target: The target sum to find.

    Returns:
        True if two nodes exist such that their values sum to target, False otherwise.
    """
    visited_values = set()
    stack = [root]

    while stack:
        current_node = stack.pop()
        
        if current_node:
            complement = target - current_node.val
            if complement in visited_values:
                return True
            
            visited_values.add(current_node.val)
            stack.append(current_node.right)
            stack.append(current_node.left)

    return False