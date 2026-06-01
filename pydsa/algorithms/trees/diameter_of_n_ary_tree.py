METADATA = {
    "id": 1522,
    "name": "Diameter of N-Ary Tree",
    "slug": "diameter_of_n_ary_tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Find the length of the longest path between any two nodes in an N-ary tree.",
}

class Node:
    def __init__(self, val: int = 0, children: list['Node'] = None):
        self.val = val
        self.children = children if children is not None else []

def solve(root: Node | None) -> int:
    """
    Calculates the diameter of an N-ary tree.
    The diameter is the length of the longest path between any two nodes.

    Args:
        root: The root node of the N-ary tree.

    Returns:
        The diameter of the tree as an integer.

    Examples:
        >>> root = Node(1, [Node(2), Node(3), Node(4)])
        >>> solve(root)
        2
    """
    if not root:
        return 0

    max_diameter = 0

    def get_depth(current_node: Node) -> int:
        """
        Helper function to calculate the max depth of a node and 
        update the global max_diameter.
        """
        nonlocal max_diameter
        
        if not current_node.children:
            return 0

        # Collect the depths of all subtrees
        child_depths = []
        for child in current_node.children:
            # Depth is 1 (edge to child) + depth of child's subtree
            child_depths.append(1 + get_depth(child))

        # Sort depths to find the two largest values
        # This allows us to find the longest path passing through current_node
        child_depths.sort(reverse=True)

        # If there are at least two children, the longest path through this node
        # is the sum of the two largest depths.
        if len(child_depths) >= 2:
            max_diameter = max(max_diameter, child_depths[0] + child_depths[1])
        # If there is only one child, the longest path through this node
        # is just the depth of that single child.
        elif len(child_depths) == 1:
            max_diameter = max(max_diameter, child_depths[0])

        # Return the maximum depth available from this node to its parent
        return child_depths[0]

    get_depth(root)
    return max_diameter
