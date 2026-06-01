METADATA = {
    "id": 1516,
    "name": "Move Sub-Tree of N-Ary Tree",
    "slug": "move_sub_tree_of_n_ary_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "hash_map", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Move a subtree from its current parent to a new parent in an N-ary tree.",
}

class Node:
    def __init__(self, val: int = None, children: list["Node"] = None):
        self.val = val
        self.children = children if children is not None else []

def solve(root: Node, subtree_val: int, new_parent_val: int) -> Node:
    """
    Moves a subtree identified by its root value to a new parent identified by its value.

    Args:
        root: The root of the N-ary tree.
        subtree_val: The value of the root node of the subtree to be moved.
        new_parent_val: The value of the node that will become the new parent.

    Returns:
        The root of the modified N-ary tree.

    Examples:
        >>> # Example structure: 1 -> [2, 3, 4], 2 -> [5, 6], 3 -> [7]
        >>> # Move subtree starting at 2 to be a child of 3.
        >>> # Result: 1 -> [3, 4], 3 -> [7, 2], 2 -> [5, 6]
        >>> root = Node(1, [Node(2, [Node(5), Node(6)]), Node(3, [Node(7)]), Node(4)])
        >>> new_root = solve(root, 2, 3)
    """
    if not root:
        return None

    target_node = None
    old_parent = None
    new_parent_node = None

    # We need to find three things: the subtree root, its current parent, and the new parent.
    # We use a simple BFS or DFS to locate these nodes.
    stack = [(root, None)]
    
    while stack:
        current, parent = stack.pop()
        
        if current.val == subtree_val:
            target_node = current
            old_parent = parent
        
        if current.val == new_parent_val:
            new_parent_node = current
            
        # If we found all three, we can stop searching early
        if target_node and new_parent_node and old_parent:
            break
            
        for child in current.children:
            stack.append((child, current))

    # Edge case: If the subtree to move is the root itself, the problem definition 
    # usually implies the tree structure changes fundamentally or is invalid.
    # However, based on standard LeetCode constraints, we assume subtree_val != root.val.
    if not target_node or not new_parent_node or not old_parent:
        return root

    # 1. Remove the target_node from its old parent's children list
    old_parent.children.remove(target_node)

    # 2. Add the target_node to the new parent's children list
    new_parent_node.children.append(target_node)

    return root
