METADATA = {
    "id": 700,
    "name": "Search in a Binary Search Tree",
    "slug": "search-in-a-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["binary_search_tree", "recursion"],
    "difficulty": "easy",
    "time_complexity": "O(h)",
    "space_complexity": "O(h)",
    "description": "Search for a node with a specific value in a binary search tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, val: int) -> TreeNode:
    """
    Args:
        root: The root node of the binary search tree.
        val: The integer value to search for.

    Returns:
        The TreeNode containing the value if found, otherwise None.
    """
    current_node = root
    while current_node is not None:
        if current_node.val == val:
            return current_node
        elif val < current_node.val:
            current_node = current_node.left
        else:
            current_node = current_node.right
    return None