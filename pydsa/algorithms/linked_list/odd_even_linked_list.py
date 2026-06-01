METADATA = {
    "id": 328,
    "name": "Odd Even Linked List",
    "slug": "odd-even-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Group all nodes with odd indices together followed by the nodes with even indices.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Rearranges the linked list such that all nodes at odd positions are followed by nodes at even positions.

    Args:
        head: The head of the singly linked list.

    Returns:
        The head of the rearranged linked list.
    """
    if not head or not head.next:
        return head

    odd_head = head
    even_head = head.next
    odd_pointer = odd_head
    even_pointer = even_head

    while even_pointer and even_pointer.next:
        odd_pointer.next = even_pointer.next
        odd_pointer = odd_pointer.next
        even_pointer.next = odd_pointer.next
        even_pointer = even_pointer.next

    odd_pointer.next = even_head
    return odd_head