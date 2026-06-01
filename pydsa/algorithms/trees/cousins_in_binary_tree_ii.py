METADATA = {
    "id": 2641,
    "name": "Cousins in Binary Tree II",
    "slug": "cousins-in-binary-tree-ii",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "tree_traversal", "level_order"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given the root of a binary tree, return an array of integers representing the number of cousins for each node.",
}

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> list[int]:
    """
    Calculates the number of cousins for each node in a binary tree.
    
    Two nodes are cousins if they are at the same depth but have different parents.
    The result is an array where the i-th element corresponds to the i-th node 
    in a level-order traversal (including the root).

    Args:
        root: The root of the binary tree.

    Returns:
        A list of integers where each integer is the count of cousins for the 
        corresponding node in the level-order traversal.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        >>> solve(root)
        [0, 1, 1, 0, 0, 0, 0]
    """
    if not root:
        return []

    # To store the final result in level-order sequence
    # We need to track nodes in the order they are visited to map results correctly
    nodes_in_order = []
    # Map node value to its cousin count
    cousin_counts = {}
    
    # Queue stores tuples of (node, parent_value)
    # Using parent_value to distinguish siblings from cousins
    queue = deque([(root, None)])
    
    while queue:
        level_size = len(queue)
        current_level_nodes = []
        
        # First pass: collect all nodes at this level and their parents
        for _ in range(level_size):
            node, parent_val = queue.popleft()
            current_level_nodes.append((node, parent_val))
            nodes_in_order.append(node)
            
            if node.left:
                queue.append((node.left, node.val))
            if node.right:
                queue.append((node.right, node.val))
        
        # Second pass: calculate cousins for the current level
        # Cousins = (Total nodes in level) - (Nodes sharing the same parent)
        level_total = len(current_level_nodes)
        parent_counts = {}
        for node, parent_val in current_level_nodes:
            parent_counts[parent_val] = parent_counts.get(parent_val, 0) + 1
            
        for node, parent_val in current_level_nodes:
            # Number of cousins = total nodes in level - nodes that are siblings (including self)
            # Note: siblings share the same parent.
            # If parent_val is None (root), it has no siblings/cousins.
            if parent_val is None:
                cousin_counts[node.val] = 0
            else:
                # Siblings are nodes with the same parent. 
                # Cousins are nodes at same level but different parent.
                cousin_counts[node.val] = level_total - parent_counts[parent_val]

    # Construct the result list based on the level-order traversal sequence
    return [cousin_counts[node.val] for node in nodes_in_order]
