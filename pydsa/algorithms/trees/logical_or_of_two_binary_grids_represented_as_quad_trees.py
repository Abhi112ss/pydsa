METADATA = {
    "id": 558,
    "name": "Logical OR of Two Binary Grids Represented as Quad-Trees",
    "slug": "logical-or-of-two-binary-grids-represented-as-quad-trees",
    "category": "Tree",
    "aliases": [],
    "tags": ["recursion", "quad_tree"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Perform a logical OR operation on two quad-trees representing binary grids.",
}

class Node:
    def __init__(self, is_leaf: bool, val: int = 0, topLeft: 'Node' = None, topRight: 'Node' = None, bottomLeft: 'Node' = None, bottomRight: 'Node' = None):
        self.is_leaf = is_leaf
        self.val = val
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

def solve(root1: Node, root2: Node) -> Node:
    """
    Performs a logical OR operation on two quad-trees.

    Args:
        root1: The root node of the first quad-tree.
        root2: The root node of the second quad-tree.

    Returns:
        The root node of the resulting quad-tree after the OR operation.

    Examples:
        >>> # Example 1: Both are leaves with value 0
        >>> r1 = Node(True, 0)
        >>> r2 = Node(True, 0)
        >>> solve(r1, r2).val
        0
        >>> # Example 2: One is leaf 1, other is leaf 0
        >>> r1 = Node(True, 1)
        >>> r2 = Node(True, 0)
        >>> solve(r1, r2).val
        1
    """
    # Base Case: If either node is a leaf, the OR result is determined by their values.
    # If either is a leaf with value 1, the entire subtree becomes a leaf with value 1.
    if root1.is_leaf or root2.is_leaf:
        return Node(True, val=1 if (root1.is_leaf and root1.val == 1) or (root2.is_leaf and root2.val == 1) else 0)

    # Recursive Step: Both are internal nodes, so we OR their corresponding children.
    new_top_left = solve(root1.topLeft, root2.topLeft)
    new_top_right = solve(root1.topRight, root2.topRight)
    new_bottom_left = solve(root1.bottomLeft, root2.bottomLeft)
    new_bottom_right = solve(root1.bottomRight, root2.bottomRight)

    # Optimization/Merging: If all four children are leaves and have the same value, 
    # merge them into a single leaf node to maintain the quad-tree property.
    if (new_top_left.is_leaf and new_top_right.is_leaf and 
        new_bottom_left.is_leaf and new_bottom_right.is_leaf and
        new_top_left.val == new_top_right.val == new_bottom_left.val == new_bottom_right.val):
        return Node(True, val=new_top_left.val)

    # Otherwise, return a new internal node with the computed children.
    return Node(False, val=0, 
                topLeft=new_top_left, 
                topRight=new_top_right, 
                bottomLeft=new_bottom_left, 
                bottomRight=new_bottom_right)