METADATA = {
    "id": 138,
    "name": "Copy List with Random Pointer",
    "slug": "copy_list_with_random_pointer",
    "category": "Linked List",
    "aliases": [],
    "tags": ["hash_map", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Create a deep copy of a linked list where each node contains an additional random pointer.",
}

class Node:
    """Definition for a Node."""
    def __init__(self, val: int = 0, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

def solve(head: Node | None) -> Node | None:
    """
    Creates a deep copy of a linked list with random pointers using a hash map.

    Args:
        head: The head of the original linked list.

    Returns:
        The head of the newly created deep-copied linked list.

    Examples:
        >>> # Example 1
        >>> node1 = Node(7)
        >>> node2 = Node(13)
        >>> node1.next = node2
        >>> node1.random = node2
        >>> node2.random = node2
        >>> new_head = solve(node1)
        >>> new_head.val == 7 and new_head.next.val == 13
        True
    """
    if not head:
        return None

    # Map to store the relationship between original nodes and their copies
    # Key: Original Node, Value: Copied Node
    old_to_new_map: dict[Node, Node] = {}

    # First pass: Create all nodes and store them in the map
    # We only set the values here; pointers are handled in the second pass
    current = head
    while current:
        old_to_new_map[current] = Node(current.val)
        current = current.next

    # Second pass: Assign next and random pointers using the map
    current = head
    while current:
        copy_node = old_to_new_map[current]
        
        # Link the next pointer of the copy to the copy of the original's next
        if current.next:
            copy_node.next = old_to_new_map[current.next]
        
        # Link the random pointer of the copy to the copy of the original's random
        if current.random:
            copy_node.random = old_to_new_map[current.random]
            
        current = current.next

    return old_to_new_map[head]
