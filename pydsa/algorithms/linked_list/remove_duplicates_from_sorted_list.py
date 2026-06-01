METADATA = {
    "id": 83,
    "name": "Remove Duplicates from Sorted List",
    "slug": "remove-duplicates-from-sorted-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked-list", "sorted"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given the head of a sorted linked list, delete all duplicates such that each element appears only once.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Removes duplicate values from a sorted linked list in-place.

    Args:
        head: The head node of a sorted singly-linked list.

    Returns:
        The head of the modified linked list where each element is unique.

    Examples:
        >>> head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
        >>> solve(head).val == 1 and solve(head).next.val == 2
        True
    """
    if not head:
        return None

    current_node = head

    # Traverse the list until the end
    while current_node and current_node.next:
        # Since the list is sorted, duplicates are always adjacent
        if current_node.val == current_node.next.val:
            # Skip the next node by pointing to the one after it
            current_node.next = current_node.next.next
        else:
            # Move to the next node only if no duplicate was found/removed
            current_node = current_node.next

    return head
