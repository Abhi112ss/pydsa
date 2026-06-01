METADATA = {
    "id": 1609,
    "name": "Even Odd Tree",
    "slug": "even-odd-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "recursion", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Construct a binary tree where even-depth nodes have only right children and odd-depth nodes have only left children.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(n: int) -> TreeNode:
    """
    Constructs an Even Odd Tree based on the given number of nodes.

    In an even-depth node, the left child is None and the right child is the next node.
    In an odd-depth node, the right child is None and the left child is the next node.
    Depth starts at 0 (even).

    Args:
        n: The total number of nodes to create.

    Returns:
        The root of the constructed Even Odd Tree.

    Examples:
        >>> root = solve(7)
        >>> # The tree structure will follow the even/odd depth rules.
    """
    if n <= 0:
        return None

    # We use a list to keep track of the next available value to ensure 
    # it's mutable across recursive calls.
    current_val = [1]

    def build_tree(depth: int) -> TreeNode:
        """
        Recursive helper to build the tree.
        
        Args:
            depth: The current depth of the node being created.
            
        Returns:
            A TreeNode instance or None if no more nodes are available.
        """
        if current_val[0] > n:
            return None

        # Create the current node
        node = TreeNode(current_val[0])
        current_val[0] += 1

        # Even depth: only right child is allowed
        if depth % 2 == 0:
            node.right = build_tree(depth + 1)
            node.left = None
        # Odd depth: only left child is allowed
        else:
            node.left = build_tree(depth + 1)
            node.right = None

        return node

    return build_tree(0)
