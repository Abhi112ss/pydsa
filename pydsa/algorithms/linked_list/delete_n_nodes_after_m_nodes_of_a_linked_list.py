METADATA = {
    "id": 1474,
    "name": "Delete N Nodes After M Nodes of a Linked List",
    "slug": "delete-n-nodes-after-m-nodes-of-a-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a linked list, delete n nodes after every m nodes.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode, m: int, n: int) -> ListNode:
    """
    Deletes n nodes after every m nodes in a linked list.

    Args:
        head: The head of the singly linked list.
        m: The number of nodes to keep.
        n: The number of nodes to delete after m nodes.

    Returns:
        The head of the modified linked list.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> solve(head, 2, 1)
        1 -> 2 -> 4 -> 5
    """
    if not head or m <= 0:
        return head

    current = head

    while current:
        # 1. Skip m-1 nodes to reach the last node of the 'keep' segment
        for _ in range(m - 1):
            if current:
                current = current.next
            else:
                return head

        # If current is None, we reached the end of the list during skipping
        if not current:
            break

        # 2. Identify the start of the 'delete' segment
        deletion_start = current.next
        
        # 3. Skip n nodes to find the node after the 'delete' segment
        for _ in range(n):
            if deletion_start:
                deletion_start = deletion_start.next
            else:
                # If we run out of nodes while deleting, the list ends here
                break
        
        # 4. Relink the 'keep' segment to the node after the 'delete' segment
        current.next = deletion_start
        
        # 5. Move current to the next node to repeat the process
        current = deletion_start

    return head
