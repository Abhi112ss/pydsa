METADATA = {
    "id": 1214,
    "name": "Two Sum BSTs",
    "slug": "two-sum-bsts",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "binary_search_tree", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(h1 + h2)",
    "description": "Determine if there exist two nodes, one from each of two binary search trees, such that their values sum to a target value.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root1: TreeNode, root2: TreeNode, target: int) -> bool:
    """
    Args:
        root1: The root of the first binary search tree.
        root2: The root of the second binary search tree.
        target: The target sum to find.

    Returns:
        True if a pair of nodes exists such that their values sum to target, False otherwise.
    """
    def find_value(node: TreeNode, value: int) -> bool:
        current = node
        while current:
            if current.val == value:
                return True
            elif value < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def traverse_and_search(node: TreeNode) -> bool:
        if not node:
            return False
        
        complement = target - node.val
        if find_value(root2, complement):
            return True
            
        return traverse_and_search(node.left) or traverse_and_search(node.right)

    return traverse_and_search(root1)