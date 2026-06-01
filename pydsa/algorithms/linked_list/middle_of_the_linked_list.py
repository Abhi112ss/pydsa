METADATA = {
    "id": 876,
    "name": "Middle of the Linked List",
    "slug": "middle_of_the_linked_list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["two_pointer", "fast_slow_pointers"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the middle node of a singly linked list.",
}


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val = val
        self.next = next


def solve(head: ListNode | None) -> ListNode | None:
    """Find the middle node of a singly linked list using fast and slow pointers.

    Args:
        head: The head node of the singly linked list. May be None for an empty list.

    Returns:
        The middle node. If the list has an even number of nodes, returns the second
        of the two middle nodes, as defined by the problem statement.

    Examples:
        >>> # List: 1 -> 2 -> 3 -> 4 -> 5
        >>> node5 = ListNode(5)
        >>> node4 = ListNode(4, node5)
        >>> node3 = ListNode(3, node4)
        >>> node2 = ListNode(2, node3)
        >>> head = ListNode(1, node2)
        >>> middle = solve(head)
        >>> middle.val
        3

        >>> # List: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        >>> node6 = ListNode(6)
        >>> node5 = ListNode(5, node6)
        >>> node4 = ListNode(4, node5)
        >>> node3 = ListNode(3, node4)
        >>> node2 = ListNode(2, node3)
        >>> head = ListNode(1, node2)
        >>> middle = solve(head)
        >>> middle.val
        4
    """
    if head is None:
        return None

    slow_pointer = head
    fast_pointer = head

    # Move fast_pointer two steps and slow_pointer one step each iteration.
    while fast_pointer.next is not None and fast_pointer.next.next is not None:
        slow_pointer = slow_pointer.next  # type: ignore[assignment]
        fast_pointer = fast_pointer.next.next

    # When fast_pointer reaches the end, slow_pointer is at the middle.
    return slow_pointer