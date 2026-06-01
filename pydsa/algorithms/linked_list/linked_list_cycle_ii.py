METADATA = {
    "id": 142,
    "name": "Linked List Cycle II",
    "slug": "linked-list-cycle-ii",
    "category": "Linked List",
    "aliases": [],
    "tags": ["two_pointers", "fast_slow_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a linked list has a cycle and return the node where the cycle begins.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None

def solve(head: ListNode | None) -> ListNode | None:
    """
    Finds the node where the cycle begins in a linked list using Floyd's Cycle-Finding Algorithm.

    Args:
        head: The head of the singly-linked list.

    Returns:
        The node where the cycle begins, or None if there is no cycle.

    Examples:
        >>> head = ListNode(3)
        >>> head.next = ListNode(2)
        >>> head.next.next = ListNode(0)
        >>> head.next.next.next = ListNode.-4
        >>> head.next.next.next.next = head.next
        >>> solve(head)
        <ListNode object at ...> (the node with value 2)
    """
    if not head or not head.next:
        return None

    slow = head
    fast = head

    # Phase 1: Detect if a cycle exists using fast and slow pointers
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If pointers meet, a cycle is confirmed
        if slow == fast:
            break
    else:
        # If loop finishes without meeting, no cycle exists
        return None

    # Phase 2: Find the entry point of the cycle
    # Mathematical proof: The distance from head to cycle start is equal to 
    # the distance from the meeting point to cycle start (moving at speed 1).
    pointer_one = head
    pointer_two = slow
    
    while pointer_one != pointer_two:
        pointer_one = pointer_one.next
        pointer_two = pointer_two.next

    return pointer_one