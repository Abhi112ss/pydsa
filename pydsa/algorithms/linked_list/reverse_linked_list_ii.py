METADATA = {
    "id": 92,
    "name": "Reverse Linked List II",
    "slug": "reverse-linked-list-ii",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverse a portion of a singly linked list from position left to right.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

def solve(head: ListNode | None, left: int, right: int) -> ListNode | None:
    """
    Reverses a sub-segment of a linked list from position 'left' to 'right'.

    Args:
        head: The head of the singly linked list.
        left: The starting position (1-indexed) of the segment to reverse.
        right: The ending position (1-indexed) of the segment to reverse.

    Returns:
        The head of the modified linked list.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> solve(head, 2, 4)
        1 -> 4 -> 3 -> 2 -> 5
    """
    if not head or left == right:
        return head

    # Use a dummy node to handle cases where 'left' is the head of the list
    dummy = ListNode(0, head)
    before_segment = dummy

    # Step 1: Move 'before_segment' to the node immediately preceding the reversal range
    for _ in range(left - 1):
        before_segment = before_segment.next

    # 'current' will be the first node of the segment to be reversed
    # It will eventually become the last node of the reversed segment
    current = before_segment.next

    # Step 2: Perform the reversal using the 'insertion' method.
    # We take the node after 'current' (called 'next_node') and move it 
    # to the position immediately after 'before_segment'.
    for _ in range(right - left):
        next_node = current.next
        
        # Remove next_node from its current position
        current.next = next_node.next
        
        # Insert next_node between before_segment and before_segment.next
        next_node.next = before_segment.next
        before_segment.next = next_node

    return dummy.next
