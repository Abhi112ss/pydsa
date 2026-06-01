METADATA = {
    "id": 1490,
    "name": "Clone N-ary Tree",
    "slug": "clone_n_ary_tree",
    "category": "trees",
    "aliases": ["clone n ary tree", "copy n ary tree"],
    "tags": ["tree", "depth_first_search", "breadth_first_search", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a root of an N-ary tree, return a deep copy (clone) of the tree.",
}

class Node:
    def __init__(self, val: int | None = None, children: list['Node'] | None = None):
        self.val = val
        self.children = children if children is not None else []

def solve(root: Node | None) -> Node | None:
    """
    Clones an N-ary tree.
    
    Args:
        root: The root node of the original N-ary tree.
        
    Returns:
        The root node of the cloned N-ary tree.
    """
    if not root:
        return None
        
    new_root = Node(root.val)
    for child in root.children:
        new_root.children.append(solve(child))
        
    return new_root