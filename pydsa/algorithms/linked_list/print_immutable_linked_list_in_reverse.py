METADATA = {
    "id": 1265,
    "name": "Print Immutable Linked List in Reverse",
    "slug": "print_immutable_linked_list_in_reverse",
    "category": "Linked List",
    "aliases": [],
    "tags": ["recursion", "stack", "linked-list"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Print the values of an immutable linked list in reverse order using recursion.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> None:
    """
    Traverses a linked list and prints its values in reverse order.

    Args:
        head: The head node of the immutable linked list.

    Returns:
        None. Prints to stdout.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> solve(head)
        3
        2
        1
    """
    def reverse_print_recursive(node: ListNode | None) -> None:
        if not node:
            return
        
        # Recurse to the end of the list first
        reverse_print_recursive(node.next)
        
        # Print the value as the recursion stack unwinds
        print(node.val)

    reverse_print_recursive(head)
