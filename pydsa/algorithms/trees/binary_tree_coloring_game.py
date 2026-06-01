METADATA = {
    "id": 1145,
    "name": "Binary Tree Coloring Game",
    "slug": "binary-tree-coloring-game",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if the second player can win a coloring game on a binary tree by choosing a color for a node such that no two adjacent nodes have the same color.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> bool:
    """
    Determines if the second player can win the coloring game.
    
    The second player wins if there exists a node such that one of its 
    connected components (left subtree, right subtree, or the rest of the 
    tree via the parent) contains more than n/2 nodes.

    Args:
        root: The root of the binary tree.

    Returns:
        bool: True if the second player can win, False otherwise.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
        >>> solve(root)
        True
    """
    total_nodes = 0

    def count_nodes(node: TreeNode) -> int:
        nonlocal total_nodes
        if not node:
            return 0
        
        # Standard DFS to count nodes in subtrees
        left_count = count_nodes(node.left)
        right_count = count_nodes(node.right)
        
        # The current node's subtree size is 1 + children sizes
        current_subtree_size = 1 + left_count + right_count
        
        # The size of the component connected via the parent
        parent_component_size = total_nodes - current_subtree_size
        
        # Check if any of the three adjacent components is larger than n/2
        # If any component > n/2, the second player can win by picking 
        # a color for the current node that is different from the majority 
        # color in that component.
        if (left_count > total_nodes / 2 or 
            right_count > total_nodes / 2 or 
            parent_component_size > total_nodes / 2):
            # We use a flag or a way to signal victory. 
            # Since we need total_nodes first, we'll do this in two passes 
            # or calculate total_nodes first.
            pass 

        return current_subtree_size

    # First pass: Calculate total number of nodes in the tree
    def get_total_size(node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + get_total_size(node.left) + get_total_size(node.right)

    n = get_total_size(root)
    total_nodes = n
    can_win = False

    def check_win_condition(node: TreeNode) -> int:
        nonlocal can_win
        if not node:
            return 0
        
        left_size = check_win_condition(node.left)
        right_size = check_win_condition(node.right)
        
        # Size of the component "above" this node
        above_size = n - (left_size + right_size + 1)
        
        # If any adjacent component is strictly greater than n/2, 
        # the second player wins.
        if left_size > n / 2 or right_size > n / 2 or above_size > n / 2:
            can_win = True
            
        return left_size + right_size + 1

    check_win_condition(root)
    return can_win