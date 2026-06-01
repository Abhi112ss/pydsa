METADATA = {
    "id": 652,
    "name": "Find Duplicate Subtrees",
    "slug": "find-duplicate-subtrees",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "hash_map", "dfs"],
    "difficulty": "medium",
    "time_complexity": "O(n^2) in worst case due to string concatenation, or O(n) with tuple hashing",
    "space_complexity": "O(n)",
    "description": "Given the root of a binary tree, return all duplicate subtrees. A duplicate subtree is a subtree that has the same structure and node values as another subtree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> list[TreeNode]:
    """
    Finds all duplicate subtrees in a binary tree using subtree serialization.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of root nodes of the duplicate subtrees.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(4)), TreeNode(1))
        >>> solve(root)
        [TreeNode(4)]
    """
    if not root:
        return []

    # Map to store the frequency of each unique subtree serialization
    subtree_counts: dict[str, int] = {}
    # List to store the root nodes of identified duplicate subtrees
    duplicates: list[TreeNode] = []

    def serialize(node: TreeNode | None) -> str:
        """
        Recursively serializes the subtree into a unique string representation.
        """
        if not node:
            # Use a special character to represent null nodes to ensure uniqueness
            return "#"

        # Post-order traversal: serialize left, then right, then current node
        # We use delimiters (like ',') to prevent ambiguity between values like 1, 11 and 11, 1
        left_serialization = serialize(node.left)
        right_serialization = serialize(node.right)
        
        # Create a unique string for the current subtree
        current_serialization = f"{node.val},{left_serialization},{right_serialization}"

        # Increment the count for this specific serialization
        subtree_counts[current_serialization] = subtree_counts.get(current_serialization, 0) + 1

        # If this is the second time we've seen this exact serialization, add to results
        # We only add it when count is exactly 2 to avoid adding the same duplicate multiple times
        if subtree_counts[current_serialization] == 2:
            duplicates.append(node)

        return current_serialization

    serialize(root)
    return duplicates
