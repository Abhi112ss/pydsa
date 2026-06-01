METADATA = {
    "id": 2487,
    "name": "Remove Nodes From Linked List",
    "slug": "remove-nodes-from-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "stack", "monotonic_stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove every node that has a node with a strictly greater value anywhere to its right in the linked list.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Removes nodes from a linked list that have a strictly greater value to their right.

    The algorithm uses a monotonic stack approach to keep track of nodes that 
    should be kept. We traverse the list and maintain a stack of nodes in 
    strictly non-increasing order of their values.

    Args:
        head: The head of the singly-linked list.

    Returns:
        The head of the modified linked list.

    Examples:
        >>> head = ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))
        >>> solve(head).val
        13
    """
    if not head:
        return None

    # We use a stack to keep track of nodes that are part of the final list.
    # A node is kept if no node to its right has a larger value.
    # This is equivalent to maintaining a monotonic decreasing stack.
    stack: list[ListNode] = []
    current = head

    while current:
        # While the current node's value is greater than the value of the node 
        # at the top of the stack, the top node must be removed because 
        # it has a larger value to its right.
        while stack and stack[-1].val < current.val:
            stack.pop()
        
        stack.append(current)
        current = current.next

    # Reconstruct the linked list using the nodes remaining in the stack.
    # The stack now contains nodes in strictly non-increasing order.
    for i in range(len(stack) - 1):
        stack[i].next = stack[i + 1]
    
    # The last node in the stack must point to None to terminate the list.
    stack[-1].next = None

    return stack[0]
