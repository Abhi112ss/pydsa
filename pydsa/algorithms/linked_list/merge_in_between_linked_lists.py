METADATA = {
    "id": 1669,
    "name": "Merge In Between Linked Lists",
    "slug": "merge-in-between-linked-lists",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Remove a range of nodes from the first linked list and replace them with the second linked list.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(list1: ListNode, list2: ListNode, a: int, b: int) -> ListNode:
    """
    Removes nodes from index 'a' to 'b' in list1 and inserts list2 in their place.

    Args:
        list1: The head of the first linked list.
        list2: The head of the second linked list.
        a: The starting index of the range to remove (0-indexed).
        b: The ending index of the range to remove (0-indexed).

    Returns:
        The head of the modified linked list.

    Examples:
        >>> l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> l2 = ListNode(6, ListNode(7))
        >>> solve(l1, l2, 2, 4)
        1 -> 2 -> 6 -> 7
    """
    # Dummy node to handle edge cases where 'a' might be 0
    dummy = ListNode(0, list1)
    
    # Pointer to find the node immediately before the removal range (index a-1)
    before_range = dummy
    for _ in range(a):
        before_range = before_range.next
        
    # Pointer to find the node immediately after the removal range (index b+1)
    after_range = before_range.next
    for _ in range(b - a + 1):
        after_range = after_range.next
        
    # Link the node before the range to the head of the second list
    before_range.next = list2
    
    # Traverse to the end of the second list
    current = list2
    while current.next:
        current = current.next
        
    # Link the end of the second list to the node after the range
    current.next = after_range
    
    return dummy.next