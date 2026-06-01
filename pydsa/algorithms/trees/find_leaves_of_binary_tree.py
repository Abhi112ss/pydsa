METADATA = {
    "id": 366,
    "name": "Find Leaves of Binary Tree",
    "slug": "find-leaves-of-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the leaves of a binary tree in layers, where each layer contains nodes at the same distance from the bottom.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> list[list[int]]:
    """
    Finds the leaves of a binary tree in layers based on their height from the bottom.

    The algorithm uses a post-order traversal (DFS) to calculate the height of 
    each node. A leaf node has height 0, its parent has height 1, and so on.
    Nodes with the same height are grouped into the same layer.

    Args:
        root: The root of the binary tree.

    Returns:
        A list of lists, where each inner list contains the values of nodes 
        at a specific height level, starting from the bottom-most leaves.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, TreeNode(6), TreeNode(7)))
        >>> solve(root)
        [[3, 4, 6, 7], [2, 5], [1]]
    """
    if not root:
        return []

    layers: list[list[int]] = []

    def get_height(node: TreeNode | None) -> int:
        """
        Recursive helper to compute height and populate layers.
        
        Args:
            node: Current node being visited.
            
        Returns:
            The height of the node (distance to furthest leaf).
        """
        if not node:
            return -1

        # Post-order traversal: visit children first to determine height
        left_height = get_height(node.left)
        right_height = get_height(node.right)

        # Height of current node is 1 + max height of its children
        current_height = 1 + max(left_height, right_height)

        # If this is a new height level we haven't seen, add a new list to layers
        if current_height == len(layers):
            layers.append([])
        
        # Add current node value to its corresponding height layer
        layers[current_height].append(node.val)

        return current_height

    get_height(root)
    return layers
