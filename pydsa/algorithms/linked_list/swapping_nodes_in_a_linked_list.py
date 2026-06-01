METADATA = {
    "id": 1721,
    "name": "Swapping Nodes in a Linked List",
    "slug": "swapping_nodes_in_a_linked_list",
    "category": "linked_list",
    "aliases": [],
    "tags": ["two_pointer", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Swap the values of the kth node from the start and the kth node from the end in a singly linked list.",
}


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val: int = val
        self.next: ListNode | None = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def solve(head: ListNode | None, k: int) -> ListNode | None:
    """Swap the values of the kth node from the start and the kth node from the end.

    Args:
        head: The head of the singly linked list.
        k: 1-indexed position of the node from the start to swap.

    Returns:
        The head of the linked list after swapping the node values.

    Examples:
        >>> # List: 1->2->3->4->5, k = 2
        >>> node5 = ListNode(5)
        >>> node4 = ListNode(4, node5)
        >>> node3 = ListNode(3, node4)
        >>> node2 = ListNode(2, node3)
        >>> node1 = ListNode(1, node2)
        >>> new_head = solve(node1, 2)
        >>> [new_head.val, new_head.next.val, new_head.next.next.val,
        ...  new_head.next.next.next.val, new_head.next.next.next.next.val]
        [1, 4, 3, 2, 5]
    """
    if head is None:
        return None

    # First pointer will land on the kth node from the start.
    current_node: ListNode | None = head
    for _ in range(k - 1):
        if current_node is None:
            return head  # k is larger than list length; no change.
        current_node = current_node.next

    kth_from_start: ListNode | None = current_node

    # Use a second pointer that starts at the head and will end at the kth node from the end.
    kth_from_end: ListNode | None = head
    trailing_pointer: ListNode | None = kth_from_start

    # Advance trailing_pointer to the end, moving kth_from_end in tandem.
    while trailing_pointer is not None and trailing_pointer.next is not None:
        trailing_pointer = trailing_pointer.next
        kth_from_end = kth_from_end.next  # type: ignore[assignment]

    # Swap the values of the two identified nodes.
    if kth_from_start is not None and kth_from_end is not None:
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

    return head