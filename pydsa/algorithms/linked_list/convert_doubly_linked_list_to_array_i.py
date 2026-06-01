METADATA = {
    "id": 3263,
    "name": "Convert Doubly Linked List to Array I",
    "slug": "convert-doubly-linked-list-to-array-i",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a doubly linked list into an array by traversing the nodes.",
}

class ListNode:
    """Definition for a doubly-linked list node."""
    def __init__(self, val: int = 0, prev: 'ListNode' = None, next: 'ListNode' = None):
        self.val = val
        self.prev = prev
        self.next = next

def solve(head: ListNode | None) -> list[int]:
    """
    Converts a doubly linked list into a Python list (array).

    Args:
        head: The head node of the doubly linked list.

    Returns:
        A list of integers containing the values of the nodes in order.

    Examples:
        >>> head = ListNode(1, None, ListNode(2, ListNode(1)))
        >>> solve(head)
        [1, 2]
    """
    result: list[int] = []
    current_node = head

    # Traverse the list using the 'next' pointer until the end is reached
    while current_node is not None:
        # Append the current node's value to the result list
        result.append(current_node.val)
        # Move to the next node in the sequence
        current_node = current_node.next

    return result