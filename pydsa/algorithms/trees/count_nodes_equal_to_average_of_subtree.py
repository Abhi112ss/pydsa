METADATA = {
    "id": 2265,
    "name": "Count Nodes Equal to Average of Subtree",
    "slug": "count-nodes-equal-to-average-of-subtree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Count the number of nodes in a binary tree whose value is equal to the average of all node values in its subtree.",
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
        The count of nodes whose value equals the average of their subtree.
    """
    total_count = 0

    def traverse(node: TreeNode) -> tuple[int, int]:
        nonlocal total_count
        if not node:
            return 0, 0

        left_sum, left_count = traverse(node.left)
        right_sum, right_count = traverse(node.right)

        current_sum = left_sum + right_sum + node.val
        current_count = left_count + right_count + 1

        if current_sum == node.val * current_count:
            total_count += 1

        return current_sum, current_count

    traverse(root)
    return total_count