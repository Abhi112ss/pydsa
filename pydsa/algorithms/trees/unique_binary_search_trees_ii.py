METADATA = {
    "id": 95,
    "name": "Unique Binary Search Trees II",
    "slug": "unique-binary-search-trees-ii",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "backtracking", "dynamic programming"],
    "difficulty": "medium",
    "time_complexity": "O(4^n / n^(3/2))",
    "space_complexity": "O(4^n / n^(3/2))",
    "description": "Given an integer n, return all structurally unique Binary Search Trees (BSTs) that consist of nodes with values from 1 to n.",
}

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(n: int) -> list[Optional[TreeNode]]:
    """
    Generates all structurally unique BSTs containing values from 1 to n.

    Args:
        n: The number of nodes in the BST.

    Returns:
        A list of root nodes of all unique BSTs.

    Examples:
        >>> solve(1)
        [TreeNode(1)]
        >>> solve(2)
        [TreeNode(1, None, TreeNode(2)), TreeNode(2, TreeNode(1))]
    """
    # Memoization dictionary to store results for a given range (start, end)
    memo: dict[tuple[int, int], list[Optional[TreeNode]]] = {}

    def build_trees(start: int, end: int) -> list[Optional[TreeNode]]:
        """
        Recursive helper to build all BSTs using values in the range [start, end].
        """
        # Base case: if start > end, the range is empty, return a list containing None
        if start > end:
            return [None]

        # Return cached result if available
        if (start, end) in memo:
            return memo[(start, end)]

        all_trees: list[Optional[TreeNode]] = []

        # Iterate through every number in the range to act as the root
        for root_val in range(start, end + 1):
            # Recursively generate all possible left subtrees using values < root_val
            left_subtrees = build_trees(start, root_val - 1)
            
            # Recursively generate all possible right subtrees using values > root_val
            right_subtrees = build_trees(root_val + 1, end)

            # Combine every left subtree with every right subtree for the current root
            for left in left_subtrees:
                for right in right_subtrees:
                    root_node = TreeNode(root_val)
                    root_node.left = left
                    root_node.right = right
                    all_trees.append(root_node)

        memo[(start, end)] = all_trees
        return all_trees

    return build_trees(1, n)
