METADATA = {
    "id": 1506,
    "name": "Find Root of N-Ary Tree",
    "slug": "find_root_of_n_ary_tree",
    "category": "tree",
    "aliases": [],
    "tags": ["trees", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the root node of an N-ary tree given all its nodes.",
}

class Node:
    """Definition for a Node in an N-ary tree."""
    def __init__(self, val: int = 0, children: list['Node'] | None = None):
        self.val: int = val
        self.children: list[Node] = children if children is not None else []

def solve(tree: list[Node]) -> Node:
    """Find the root node of an N-ary tree.

    Args:
        tree: A list containing all nodes of the N-ary tree. Each node has a
            unique integer value and a list of its child nodes.

    Returns:
        The root node of the tree.

    Examples:
        >>> a = Node(1)
        >>> b = Node(2)
        >>> c = Node(3)
        >>> a.children = [b, c]
        >>> root = solve([a, b, c])
        >>> root.val
        1
    """
    # Map each node value to its node instance for O(1) lookup.
    value_to_node: dict[int, Node] = {node.val: node for node in tree}

    # Collect all values that appear as children.
    child_values: set[int] = set()
    for parent_node in tree:
        for child_node in parent_node.children:
            child_values.add(child_node.val)

    # The root is the node whose value never appears as a child.
    for candidate_value, candidate_node in value_to_node.items():
        if candidate_value not in child_values:
            return candidate_node

    raise ValueError("Root node could not be determined from the given tree.")