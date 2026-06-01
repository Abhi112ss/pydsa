METADATA = {
    "id": 426,
    "name": "Convert Binary Search Tree to Sorted Doubly Linked List",
    "slug": "convert-binary-search-tree-to-sorted-doubly-linked-list",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "in_order_traversal", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Convert a Binary Search Tree into a sorted circular doubly linked list in-place.",
}

class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Node) -> Node:
    """
    Converts a Binary Search Tree into a sorted circular doubly linked list in-place.

    The conversion is performed using an in-order traversal to ensure the 
    nodes are processed in sorted order. We maintain a reference to the 
    previously visited node to establish the bidirectional links.

    Args:
        root: The root node of the Binary Search Tree.

    Returns:
        The head node of the circular doubly linked list.

    Examples:
        >>> root = Node(4, Node(2, Node(1), Node(3)), Node(5, None, Node(6)))
        >>> head = solve(root)
        >>> head.val
        1
        >>> head.right.right.right.val
        1
    """
    if not root:
        return None

    # 'first' tracks the smallest element (head of the list)
    # 'last' tracks the most recently processed node in the in-order traversal
    first: Node = None
    last: Node = None

    def in_order_traversal(current_node: Node) -> None:
        nonlocal first, last
        if not current_node:
            return

        # Traverse left subtree
        in_order_traversal(current_node.left)

        # Process current node
        if last:
            # Link the previous node (last) with the current node
            last.right = current_node
            current_node.left = last
        else:
            # If last is None, we are at the smallest node
            first = current_node
        
        # Move the 'last' pointer to the current node
        last = current_node

        # Traverse right subtree
        in_order_traversal(current_node.right)

    # Perform the in-order traversal to link nodes linearly
    in_order_traversal(root)

    # After traversal, 'first' is the head and 'last' is the tail.
    # Connect them to make the list circular.
    last.right = first
    first.left = last

    return first