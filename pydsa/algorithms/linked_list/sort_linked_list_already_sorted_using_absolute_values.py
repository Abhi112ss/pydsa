METADATA = {
    "id": 2046,
    "name": "Sort Linked List by Absolute Value",
    "slug": "sort-linked-list-by-absolute-value",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Sort a linked list such that the absolute values of the nodes are in non-decreasing order.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Sorts a linked list based on the absolute values of its elements.
    
    The implementation uses a Merge Sort algorithm adapted for linked lists 
    to achieve O(n log n) time complexity and O(1) auxiliary space (excluding recursion stack).

    Args:
        head: The head of the singly linked list.

    Returns:
        The head of the sorted linked list.

    Examples:
        >>> head = ListNode(1, ListNode(-2, ListNode(3, ListNode(-4))))
        >>> solve(head)
        ListNode(1) -> ListNode(-2) -> ListNode(3) -> ListNode(-4) (sorted by abs)
    """
    if not head or not head.next:
        return head

    # Step 1: Split the list into two halves using slow and fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None  # Break the list into two parts

    # Step 2: Recursively sort both halves
    left = solve(head)
    right = solve(mid)

    # Step 3: Merge the two sorted halves based on absolute value
    return merge(left, right)

def merge(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    Merges two sorted linked lists based on the absolute value of nodes.

    Args:
        l1: Head of the first sorted linked list.
        l2: Head of the second sorted linked list.

    Returns:
        Head of the merged sorted linked list.
    """
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        # Compare absolute values to determine the order
        if abs(l1.val) <= abs(l2.val):
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    # Attach the remaining nodes
    current.next = l1 if l1 else l2
    
    return dummy.next