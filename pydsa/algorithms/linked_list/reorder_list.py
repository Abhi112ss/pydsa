METADATA = {
    "id": 143,
    "name": "Reorder List",
    "slug": "reorder-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["two_pointers", "linked-list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reorder a singly linked list into a specific pattern by alternating nodes from the start and the end.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> None:
    """
    Reorders the linked list in-place to follow the pattern: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
    
    The algorithm follows three main steps:
    1. Find the middle of the linked list using slow and fast pointers.
    2. Reverse the second half of the linked list.
    3. Merge the two halves by alternating nodes.

    Args:
        head: The head of the singly linked list.

    Returns:
        None. The list is modified in-place.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        >>> solve(head)
        >>> # head is now 1 -> 4 -> 2 -> 3
    """
    if not head or not head.next:
        return

    # Step 1: Find the middle of the list
    # Using slow and fast pointers, slow will end up at the middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    # slow.next is the start of the second half
    prev, curr = None, slow.next
    slow.next = None  # Split the list into two halves
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # prev is now the head of the reversed second half
    second_half_head = prev
    first_half_head = head

    # Step 3: Merge the two halves
    # Alternatingly pick nodes from the first half and the reversed second half
    while second_half_head:
        temp_first = first_half_head.next
        temp_second = second_half_head.next

        first_half_head.next = second_half_head
        second_half_head.next = temp_first

        first_half_head = temp_first
        second_half_head = temp_second
