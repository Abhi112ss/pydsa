METADATA = {
    "id": 86,
    "name": "Partition List",
    "slug": "partition-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None, x: int) -> ListNode | None:
    """
    Partitions a linked list around a value x using two dummy heads.

    Args:
        head: The head of the singly-linked list.
        x: The value to partition the list around.

    Returns:
        The head of the partitioned linked list.

    Examples:
        >>> head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))
        >>> solve(head, 3)
        1 -> 2 -> 2 -> 4 -> 3 -> 5
    """
    # Create two dummy nodes to act as the starting points for the two partitions
    # 'less_head' will store nodes with values < x
    # 'greater_head' will store nodes with values >= x
    less_head = ListNode(0)
    greater_head = ListNode(0)
    
    # Pointers to track the current tail of both partitions
    less_ptr = less_head
    greater_ptr = greater_head
    
    current = head
    while current:
        if current.val < x:
            # Append to the 'less than' list
            less_ptr.next = current
            less_ptr = less_ptr.next
        else:
            # Append to the 'greater than or equal' list
            greater_ptr.next = current
            greater_ptr = greater_ptr.next
        
        current = current.next
    
    # Crucial step: terminate the 'greater' list to avoid cycles in the linked list
    greater_ptr.next = None
    
    # Concatenate the 'less' list with the 'greater' list
    # greater_head.next skips the dummy node
    less_ptr.next = greater_head.next
    
    # Return the head of the combined list, skipping the 'less' dummy node
    return less_head.next
