METADATA = {
    "id": 3294,
    "name": "Convert Doubly Linked List to Array II",
    "slug": "convert-doubly-linked-list-to-array-ii",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "array", "traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a doubly linked list into an array by traversing the nodes sequentially.",
}

class DoublyLinkedListNode:
    """Definition for a doubly-linked list node."""
    def __init__(self, val: int = 0, prev: 'DoublyLinkedListNode' = None, next: 'DoublyLinkedListNode' = None):
        self.val = val
        self.prev = prev
        self.next = next

def solve(head: DoublyLinkedListNode | None) -> list[int]:
    """
    Converts a doubly linked list into a Python list (array).

    Args:
        head: The head node of the doubly linked list.

    Returns:
        A list of integers containing the values of the nodes in order.

    Examples:
        >>> node3 = DoublyLinkedListNode(3)
        >>> node2 = DoublyLinkedListNode(2, next=node3)
        >>> node1 = DoublyLinkedListNode(1, next=node2)
        >>> node2.prev = node1
        >>> node3.prev = node2
        >>> solve(node1)
        [1, 2, 3]
    """
    result: list[int] = []
    current_node = head

    # Traverse the list until the end is reached
    while current_node is not None:
        # Append the current node's value to the result list
        result.append(current_node.val)
        # Move to the next node in the sequence
        current_node = current_node.next

    return result