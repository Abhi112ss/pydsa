METADATA = {
    "id": 3217,
    "name": "Delete Nodes From Linked List Present in Array",
    "slug": "delete-nodes-from-linked-list-present-in-array",
    "category": "Linked List",
    "aliases": [],
    "tags": ["hash_map", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Remove all nodes from a linked list whose values are present in a given integer array.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode, values: list[int]) -> ListNode:
    """
    Args:
        head: The head of a singly linked list.
        values: A list of integers representing values to be removed.

    Returns:
        The head of the modified linked list.
    """
    forbidden_values = set(values)
    dummy_node = ListNode(0)
    dummy_node.next = head
    current_node = dummy_node

    while current_node.next:
        if current_node.next.val in forbidden_values:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

    return dummy_node.next