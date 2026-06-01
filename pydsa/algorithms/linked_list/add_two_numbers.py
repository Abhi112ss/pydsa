METADATA = {
    "id": 2,
    "name": "Add Two Numbers",
    "slug": "add-two-numbers",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "math"],
    "difficulty": "medium",
    "time_complexity": "O(max(m, n))",
    "space_complexity": "O(max(m, n))",
    "description": "Add two numbers represented by linked lists where each node contains a single digit and digits are stored in reverse order.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

def solve(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Adds two numbers represented by linked lists.

    Args:
        l1: The head of the first linked list.
        l2: The head of the second linked list.

    Returns:
        The head of a new linked list representing the sum of the two numbers.

    Examples:
        >>> l1 = ListNode(2, ListNode(4, ListNode(3)))
        >>> l2 = ListNode(5, ListNode(6, ListNode(4)))
        >>> solve(l1, l2)
        # Resulting list: 7 -> 0 -> 8 (representing 807)
    """
    dummy_head = ListNode(0)
    current_node = dummy_head
    carry = 0

    # Iterate as long as there are nodes in either list or a remaining carry
    while l1 is not None or l2 is not None or carry != 0:
        # Extract values from current nodes, defaulting to 0 if list is exhausted
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and the new carry
        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        digit = total_sum % 10

        # Create new node with the single digit result
        current_node.next = ListNode(digit)
        current_node = current_node.next

        # Advance the input pointers
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next