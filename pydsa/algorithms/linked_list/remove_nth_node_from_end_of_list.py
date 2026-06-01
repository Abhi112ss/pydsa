METADATA = {
    "id": 19,
    "name": "Remove Nth Node From End of List",
    "slug": "remove-nth-node-from-end-of-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Remove the nth node from the end of a linked list and return its head.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

def solve(head: ListNode, n: int) -> ListNode:
    """
    Removes the nth node from the end of a singly linked list using the two-pointer technique.

    Args:
        head: The head of the singly linked list.
        n: The position of the node to be removed from the end (1-indexed).

    Returns:
        The head of the modified linked list.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> solve(head, 2)
        1 -> 2 -> 3 -> 5
    """
    # Use a dummy node to handle edge cases like removing the head node
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    # Move the fast pointer n steps ahead
    # This creates a gap of n nodes between slow and fast
    for _ in range(n):
        fast = fast.next

    # Move both pointers until fast reaches the last node
    # When fast.next is None, slow will be at the node immediately preceding the target
    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    # slow.next is the node to be removed
    slow.next = slow.next.next

    return dummy.next
