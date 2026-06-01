METADATA = {
    "id": 979,
    "name": "Distribute Coins in Binary Tree",
    "slug": "distribute-coins-in-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Calculate the minimum number of moves to distribute coins such that every node has exactly one coin.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Calculates the minimum number of moves to distribute coins in a binary tree.
    
    The core idea is that for any subtree, the number of coins that must cross 
    the edge connecting this subtree to its parent is the absolute difference 
    between the total coins in the subtree and the number of nodes in the subtree.

    Args:
        root: The root node of the binary tree.

    Returns:
        The minimum number of moves required to distribute the coins.

    Examples:
        >>> root = TreeNode(3, TreeNode(0), TreeNode(0))
        >>> solve(root)
        2
        >>> root = TreeNode(0, TreeNode(0), TreeNode(3))
        >>> solve(root)
        2
    """
    total_moves = 0

    def dfs(node: TreeNode) -> int:
        """
        Post-order traversal to calculate the balance of coins in subtrees.
        
        Args:
            node: The current node being visited.
            
        Returns:
            The net balance of coins in the subtree rooted at 'node'.
            A positive balance means excess coins; negative means deficit.
        """
        nonlocal total_moves
        
        if not node:
            return 0

        # Calculate the balance of the left and right subtrees.
        # A balance of -1 means the subtree needs 1 coin.
        # A balance of 1 means the subtree has 1 extra coin to give.
        left_balance = dfs(node.left)
        right_balance = dfs(node.right)

        # The number of moves passing through the edge to the parent is 
        # the absolute value of the sum of balances from children.
        # If left_balance is -1 and right_balance is 1, the node itself 
        # acts as a conduit, but the net flow to the parent is 0.
        total_moves += abs(left_balance) + abs(right_balance)

        # Return the net balance of this node: 
        # (current node's coins) + (left subtree balance) + (right subtree balance)
        # Since every node starts with 1 coin, we use node.val (which is 1 or 0).
        # Note: The problem states every node starts with 1 coin, but the input 
        # tree values represent the initial coins at each node.
        return node.val + left_balance + right_balance

    dfs(root)
    return total_moves
