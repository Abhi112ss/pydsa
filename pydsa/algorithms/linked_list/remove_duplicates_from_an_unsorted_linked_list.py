METADATA = {
    "id": 1836,
    "name": "Remove Duplicates From an Unsorted Linked List",
    "slug": "remove-duplicates-from-an-unsorted-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["hash_set", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove all nodes from an unsorted linked list that have duplicate values, leaving only the first occurrence of each value.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Removes duplicate values from an unsorted linked list.
    
    Only the first occurrence of each value is kept. Subsequent nodes 
    with values already seen in the list are removed.

    Args:
        head: The head of the unsorted linked list.

    Returns:
        The head of the modified linked list with duplicates removed.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(1, ListNode(3))))
        >>> solve(head).val == 1 and solve(head).next.val == 2
        True
    """
    if not head:
        return None

    # Use a set to track values we have already encountered
    seen_values = set()
    
    # We use a dummy node to simplify edge cases, though not strictly 
    # necessary here since we aren't deleting the head itself, 
    # but it's good practice for linked list manipulation.
    dummy = ListNode(0)
    dummy.next = head
    
    current = head
    previous = dummy
    
    while current:
        if current.val in seen_values:
            # If value is a duplicate, skip the current node by 
            # linking the previous node to the next node.
            previous.next = current.next
        else:
            # If value is new, add it to the set and move the 
            # 'previous' pointer forward.
            seen_values.add(current.val)
            previous = current
            
        # Move to the next node in the original list
        current = current.next
        
    return dummy.next
