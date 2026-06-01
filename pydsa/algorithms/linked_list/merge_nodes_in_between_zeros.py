METADATA = {
    "id": 2181,
    "name": "Merge Nodes in Between Zeros",
    "slug": "merge-nodes-in-between-zeros",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "traversal", "two-pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Merge nodes in a linked list by summing values between consecutive zero nodes.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Merges nodes in a linked list by summing values between consecutive zero nodes.

    The algorithm traverses the list, skipping the initial zero, and accumulates 
    the sum of values until the next zero is encountered. Each sum is then 
    stored in a new node.

    Args:
        head: The head of the linked list.

    Returns:
        The head of the modified linked list containing the merged sums.

    Examples:
        >>> head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(0)))))))
        >>> result = solve(head)
        >>> # result represents [4, 9]
    """
    # Dummy node helps in building the new list without special handling for the head
    dummy = ListNode(0)
    current_new = dummy
    
    # Skip the first zero node
    current_old = head.next
    running_sum = 0
    
    while current_old:
        if current_old.val == 0:
            # When a zero is hit, the current segment is complete.
            # Append the accumulated sum to the new list.
            current_new.next = ListNode(running_sum)
            current_new = current_new.next
            # Reset sum for the next segment
            running_sum = 0
        else:
            # Accumulate values between zeros
            running_sum += current_old.val
            
        current_old = current_old.next
        
    return dummy.next
