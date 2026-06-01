METADATA = {
    "id": 25,
    "name": "Reverse Nodes in k-Group",
    "slug": "reverse-nodes-in-k-group",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "recursion", "two-pointers"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverse the nodes of a linked list k at a time and return its modified list.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

def solve(head: ListNode, k: int) -> ListNode:
    """
    Reverses nodes of a linked list k at a time. If the number of nodes is not a 
    multiple of k, the left-out nodes at the end remain in their original order.

    Args:
        head: The head of the singly-linked list.
        k: The size of the groups to be reversed.

    Returns:
        The head of the modified linked list.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> k = 2
        >>> solve(head, k)
        # Returns list: 2 -> 1 -> 4 -> 3 -> 5
    """
    if not head or k == 1:
        return head

    # Dummy node helps handle the head change gracefully
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy

    while True:
        # 1. Check if there are at least k nodes left to reverse
        kth_node = group_prev
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next

        # 2. Identify the boundaries of the segment to reverse
        group_next = kth_node.next
        prev = group_next
        curr = group_prev.next
        
        # 3. Standard iterative reversal for the k nodes
        # We initialize 'prev' as 'group_next' so the tail of the reversed 
        # segment automatically points to the start of the next segment.
        for _ in range(k):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        # 4. Connect the previous part of the list to the new head of this segment
        # and move group_prev to the end of the reversed segment
        new_group_end = group_prev.next
        group_prev.next = kth_node
        group_prev = new_group_end

    return dummy.next
