METADATA = {
    "id": 3063,
    "name": "Linked List Frequency",
    "slug": "linked_list_frequency",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Traverse a linked list to count the frequency of each node value using a hash map.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> dict[int, int]:
    """
    Args:
        head: The head of a singly linked list.

    Returns:
        A dictionary mapping each unique integer value in the linked list to its frequency.
    """
    frequencies = {}
    current_node = head
    while current_node is not None:
        value = current_node.val
        if value in frequencies:
            frequencies[value] += 1
        else:
            frequencies[value] = 1
        current_node = current_node.next
    return frequencies