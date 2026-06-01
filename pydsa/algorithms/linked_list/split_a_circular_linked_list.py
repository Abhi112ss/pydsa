METADATA = {
    "id": 2674,
    "name": "Split a Circular Linked List",
    "slug": "split-a-circular-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Split a circular linked list into two halves, where the second half is also a circular linked list.",
}

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> tuple[ListNode | None, ListNode | None]:
    """
    Splits a circular linked list into two halves.

    The first half will contain ceil(n/2) nodes, and the second half 
    will contain the remaining nodes. Both resulting lists will be circular.

    Args:
        head: The head of the circular linked list.

    Returns:
        A tuple containing (head_of_first_half, head_of_second_half).
        Returns (None, None) if the input head is None.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
        >>> # (Simulating circularity manually for example)
        >>> head.next.next.next.next = head
        >>> h1, h2 = solve(head)
        >>> # h1: 1 -> 2 -> (back to 1), h2: 3 -> 4 -> (back to 3)
    """
    if not head:
        return None, None

    # If there is only one node, the split results in one list with 1 node 
    # and one empty list. However, per problem constraints, we handle 
    # the circularity.
    if head.next == head:
        return head, None

    slow = head
    fast = head

    # Use fast and slow pointers to find the midpoint.
    # For a circular list, we check fast.next and fast.next.next 
    # to ensure we don't overshoot the loop.
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # If fast.next.next is head, it means we have an even number of nodes.
    # We need to move fast to the last node to close the second circle.
    if fast.next.next == head:
        fast = fast.next

    # head2 starts after the midpoint (slow)
    head2 = slow.next
    
    # Break the first circle: connect the end of the first half back to head
    slow.next = head
    
    # Break the second circle: connect the end of the second half back to head2
    fast.next = head2

    return head, head2
