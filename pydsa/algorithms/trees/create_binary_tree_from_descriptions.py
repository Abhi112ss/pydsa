METADATA = {
    "id": 2196,
    "name": "Create Binary Tree From Descriptions",
    "slug": "create-binary-tree-from-descriptions",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "hash_map", "design"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct a binary tree from a list of parent-child relationship descriptions.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(descriptions: list[list[int]]) -> TreeNode:
    """
    Constructs a binary tree from a list of parent-child descriptions.

    Args:
        descriptions: A list of lists where each sublist contains [parent, child].

    Returns:
        The root of the constructed binary tree.

    Examples:
        >>> solve([[1, 3], [2, 5], [4, 7], [5, 6], [5, 8], [4, 6], [2, 4], [7, 8]])
        # Returns the root of the tree structure.
    """
    if not descriptions:
        return None

    # Map to store node values to their corresponding TreeNode objects
    nodes_map: dict[int, TreeNode] = {}
    # Set to keep track of all children to identify the root later
    children_set: set[int] = set()

    for parent_val, child_val in descriptions:
        # Ensure both parent and child nodes exist in the map
        if parent_val not in nodes_map:
            nodes_map[parent_val] = TreeNode(parent_val)
        if child_val not in nodes_map:
            nodes_map[child_val] = TreeNode(child_val)
        
        parent_node = nodes_map[parent_val]
        child_node = nodes_map[child_val]

        # Assign the child to the parent's left or right slot
        if parent_node.left is None:
            parent_node.left = child_node
        else:
            parent_node.right = child_node
            
        # Mark this node as a child so it cannot be the root
        children_set.add(child_val)

    # The root is the node that exists in nodes_map but is not in children_set
    for node_val in nodes_map:
        if node_val not in children_set:
            return nodes_map[node_val]

    return None
