METADATA = {
    "id": 147,
    "name": "Insertion Sort List",
    "slug": "insertion-sort-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["sorting", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Sort a singly linked list using the insertion sort algorithm.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Sorts a singly linked list using the insertion sort algorithm.

    Args:
        head: The head of the singly linked list.

    Returns:
        The head of the sorted singly linked list.

    Examples:
        >>> head = ListNode(4, ListNode(2, ListNode(1, ListNode(3)))
        >>> sorted_head = solve(head)
        >>> # sorted_head represents 1 -> 2 -> 3 -> 4
    """
    if not head or not head.next:
        return head

    # Dummy node acts as the head of the sorted list to simplify insertions
    dummy = ListNode(0)
    current = head

    while current:
        # Store the next node to process before we detach 'current'
        next_node = current.next
        
        # Find the correct position in the sorted part (starting from dummy)
        # We look for the node after which 'current' should be inserted
        prev = dummy
        while prev.next and prev.next.val < current.val:
            prev = prev.next
        
        # Insert 'current' between 'prev' and 'prev.next'
        current.next = prev.next
        prev.next = current
        
        # Move to the next node in the original unsorted list
        current = next_node

    return dummy.next
