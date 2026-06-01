METADATA = {
    "id": 2095,
    "name": "Delete the Middle Node of a Linked List",
    "slug": "delete-the-middle-node-of-a-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Delete the middle node of a linked list and return its head.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Args:
        head: The head of the singly linked list.

    Returns:
        The head of the modified linked list after deleting the middle node.
    """
    if not head or not head.next:
        return None

    slow = head
    fast = head
    predecessor = None

    while fast and fast.next:
        predecessor = slow
        slow = slow.next
        fast = fast.next.next

    predecessor.next = slow.next

    return head