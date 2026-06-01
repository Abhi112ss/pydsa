METADATA = {
    "id": 1110,
    "name": "Delete Nodes And Return Forest",
    "slug": "delete-nodes-and-return-forest",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a binary tree, delete all nodes that have a value of 0 and return the resulting forest.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> list[TreeNode | None]:
    """
    Args:
        root: The root of the binary tree.

    Returns:
        A list of roots of the trees in the resulting forest.
    """
    forest = []

    def process_node(node: TreeNode | None) -> TreeNode | None:
        if not node:
            return None

        node.left = process_node(node.left)
        node.right = process_node(node.right)

        if node.val == 0:
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)
            return None

        return node

    new_root = process_node(root)
    if new_root:
        forest.insert(0, new_root)
    
    return forest