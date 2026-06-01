METADATA = {
    "id": 206,
    "name": "Reverse Linked List",
    "slug": "reverse-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "recursion", "iterative"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverse a singly linked list such that each node points to its previous node.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Args:
        head: The head of a singly linked list.

    Returns:
        The new head of the reversed linked list.
    """
    previous_node = None
    current_node = head

    while current_node is not None:
        next_temp_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_temp_node

    return previous_node