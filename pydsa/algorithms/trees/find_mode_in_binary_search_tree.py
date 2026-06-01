METADATA = {
    "id": 501,
    "name": "Find Mode in Binary Search Tree",
    "slug": "find_mode_in_binary_search_tree",
    "category": "Tree",
    "aliases": ["find mode in bst"],
    "tags": ["dfs", "bst", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all the mode(s) (the most frequently occurred element) in a binary search tree.",
}


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(root: TreeNode) -> list[int]:
    """
    Find all the mode(s) (the most frequently occurred element) in a binary search tree.

    Args:
        root: The root node of the binary search tree.

    Returns:
        A list of mode values in the BST.

    Examples:
        >>> root = TreeNode(1, None, TreeNode(2, TreeNode(2)))
        >>> solve(root)
        [2]
        >>> root = TreeNode(0)
        >>> solve(root)
        [0]
    """
    if not root:
        return []

    # Use a hash map to count frequencies of each value
    frequency_map = {}

    # Perform in-order traversal to count frequencies
    def inorder(node: TreeNode) -> None:
        if not node:
            return
        inorder(node.left)
        frequency_map[node.val] = frequency_map.get(node.val, 0) + 1
        inorder(node.right)

    inorder(root)

    # Find the maximum frequency
    max_frequency = max(frequency_map.values())

    # Collect all values with the maximum frequency
    modes = [val for val, freq in frequency_map.items() if freq == max_frequency]

    return modes