METADATA = {
    "id": 508,
    "name": "Most Frequent Subtree Sum",
    "slug": "most-frequent-subtree-sum",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "hash_map", "recursion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the subtree sum that occurs most frequently in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Args:
        root: The root of the binary tree.

    Returns:
        The most frequent subtree sum.
    """
    frequency_map = {}

    def calculate_subtree_sums(node: TreeNode) -> int:
        if not node:
            return 0
        
        left_sum = calculate_subtree_sums(node.left)
        right_sum = calculate_subtree_sums(node.right)
        current_sum = node.val + left_sum + right_sum
        
        frequency_map[current_sum] = frequency_map.get(current_sum, 0) + 1
        return current_sum

    calculate_subtree_sums(root)

    max_frequency = 0
    result_sum = 0

    for subtree_sum, count in frequency_map.items():
        if count > max_frequency:
            max_frequency = count
            result_sum = subtree_sum
        elif count == max_frequency:
            if subtree_sum < result_sum:
                result_sum = subtree_sum

    return result_sum