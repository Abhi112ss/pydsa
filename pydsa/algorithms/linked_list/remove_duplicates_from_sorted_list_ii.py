METADATA = {
    "id": 82,
    "name": "Remove Duplicates from Sorted List II",
    "slug": "remove-duplicates-from-sorted-list-ii",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Removes all nodes that have duplicate values from a sorted linked list.

    Args:
        head: The head of a sorted linked list.

    Returns:
        The head of the modified linked list containing only unique elements.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
        >>> solve(head)
        ListNode(1) -> ListNode(2) -> ListNode(5)
    """
    # Use a dummy node to handle cases where the head itself is a duplicate
    dummy = ListNode(0, head)
    
    # 'predecessor' is the last node known to be part of the distinct list
    predecessor = dummy
    
    current = head
    
    while current:
        # Check if current node is the start of a duplicate sequence
        if current.next and current.val == current.next.val:
            # Move current to the end of the duplicate sequence
            while current.next and current.val == current.next.val:
                current = current.next
            
            # Skip all nodes in the duplicate sequence by linking predecessor to the node after current
            predecessor.next = current.next
        else:
            # If no duplicate was found, move the predecessor forward
            predecessor = predecessor.next
            
        # Move to the next node in the original list
        current = current.next
        
    return dummy.next
