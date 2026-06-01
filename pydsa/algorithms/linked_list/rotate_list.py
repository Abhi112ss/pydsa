METADATA = {
    "id": 61,
    "name": "Rotate List",
    "slug": "rotate-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["two_pointer", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Rotate a linked list to the right by k places.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None, k: int) -> ListNode | None:
    """
    Rotates a linked list to the right by k places.

    Args:
        head: The head of the singly-linked list.
        k: The number of positions to rotate the list to the right.

    Returns:
        The new head of the rotated linked list.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> k = 2
        >>> solve(head, k).val
        4
    """
    if not head or not head.next or k == 0:
        return head

    # Step 1: Calculate the length of the list and find the current tail
    length = 1
    current_tail = head
    while current_tail.next:
        current_tail = current_tail.next
        length += 1

    # Step 2: Handle cases where k >= length
    k = k % length
    if k == 0:
        return head

    # Step 3: Connect the tail to the head to form a circular list
    current_tail.next = head

    # Step 4: Find the new tail. 
    # The new tail is at position (length - k - 1) from the start.
    # The new head is the node immediately following the new tail.
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    
    # Step 5: Break the circular connection
    new_tail.next = None

    return new_head