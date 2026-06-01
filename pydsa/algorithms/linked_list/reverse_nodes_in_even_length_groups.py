METADATA = {
    "id": 2074,
    "name": "Reverse Nodes in Even Length Groups",
    "slug": "reverse-nodes-in-even-length-groups",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverse nodes in groups of increasing size, but only if the group size is even.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Reverses nodes in groups of increasing size (1, 2, 3...) only if the group size is even.

    Args:
        head: The head of the singly linked list.

    Returns:
        The head of the modified linked list.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        >>> solve(head)
        1 -> 3 -> 2 -> 4 -> 6 -> 5
    """
    if not head:
        return None

    dummy = ListNode(0, head)
    prev_group_end = dummy
    current_node = head
    group_size = 1

    while current_node:
        # 1. Identify the current group and check its actual length
        group_start = current_node
        count = 0
        temp = current_node
        
        # Traverse to find the end of the current group of size 'group_size'
        while temp and count < group_size:
            temp = temp.next
            count += 1
        
        # 'temp' now points to the start of the next group
        # 'count' is the actual number of nodes available in this group
        
        if count % 2 == 0:
            # 2. If group size is even, reverse the nodes in this group
            prev = temp  # Connect the tail of the reversed group to the next group
            curr = group_start
            for _ in range(count):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            # Connect the previous group's end to the new head of this reversed group
            prev_group_end.next = prev
            # The original start of the group is now the end of the group
            prev_group_end = group_start
            current_node = temp
        else:
            # 3. If group size is odd, do not reverse. Just skip over the group.
            # We need to find the last node of this group to update prev_group_end
            last_node = group_start
            for _ in range(count - 1):
                last_node = last_node.next
            
            prev_group_end = last_node
            current_node = temp
            
        group_size += 1

    return dummy.next
