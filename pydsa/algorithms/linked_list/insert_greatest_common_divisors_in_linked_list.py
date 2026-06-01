METADATA = {
    "id": 2807,
    "name": "Insert Greatest Common Divisors in Linked List",
    "slug": "insert-greatest-common-divisors-in-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * log(max_val))",
    "space_complexity": "O(1)",
    "description": "Insert a new node with the GCD of two adjacent nodes between them in a singly linked list.",
}

import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Traverses the linked list and inserts a new node containing the GCD 
    of the current node and the next node between them.

    Args:
        head: The head of the singly linked list.

    Returns:
        The head of the modified linked list.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> solve(head)
        1 -> 1 -> 2 -> 1 -> 3
    """
    if not head or not head.next:
        return head

    current = head
    
    # Iterate until we reach the last node
    while current and current.next:
        # Calculate the Greatest Common Divisor of current and next node values
        gcd_value = math.gcd(current.val, current.next.val)
        
        # Create the new node to be inserted
        new_node = ListNode(gcd_value)
        
        # Insert the new node between current and current.next
        new_node.next = current.next
        current.next = new_node
        
        # Move current pointer two steps forward to skip the newly inserted node
        current = new_node.next
        
    return head
