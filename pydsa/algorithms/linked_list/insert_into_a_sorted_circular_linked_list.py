METADATA = {
    "id": 708,
    "name": "Insert into a Sorted Circular Linked List",
    "slug": "insert-into-a-sorted-circular-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Insert a new node into a sorted circular linked list while maintaining its sorted order.",
}

class Node:
    def __init__(self, val: int = None, next: 'Node' = None):
        self.val = val
        self.next = next

def solve(head: Node | None, insertVal: int) -> Node:
    """
    Inserts a new node with insertVal into a sorted circular linked list.

    Args:
        head: The head of the sorted circular linked list.
        insertVal: The integer value to be inserted.

    Returns:
        The head of the modified circular linked list.

    Examples:
        >>> head = Node(3, Node(4, Node(1)) # Circular: 3 -> 4 -> 1 -> 3
        >>> solve(head, 2)
        3 -> 4 -> 1 -> 2 -> 3
    """
    new_node = Node(insertVal)

    # Case 1: Empty list
    if not head:
        new_node.next = new_node
        return new_node

    prev = head
    curr = head.next
    inserted = False

    while True:
        # Case 2: Standard insertion between two nodes (prev.val <= insertVal <= curr.val)
        if prev.val <= insertVal <= curr.val:
            inserted = True
        
        # Case 3: Insertion at the wrap-around point (max -> min)
        elif prev.val > curr.val:
            # If insertVal is the new maximum or the new minimum
            if insertVal >= prev.val or insertVal <= curr.val:
                inserted = True
        
        if inserted:
            prev.next = new_node
            new_node.next = curr
            return head

        prev, curr = curr, curr.next

        # Case 4: We have traversed the entire list and returned to head without finding a spot
        # This happens if all nodes in the list have the same value
        if prev == head:
            break

    # If we reached here, it means all values are the same or we completed a full loop
    prev.next = new_node
    new_node.next = curr
    return head
