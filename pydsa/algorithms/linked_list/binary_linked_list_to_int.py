METADATA = {
    "id": 1290,
    "name": "Convert Binary Number in a Linked List to Integer",
    "slug": "convert_binary_number_in_a_linked_list_to_integer",
    "category": "linked_list",
    "aliases": [],
    "tags": ["linked_list", "math", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Convert a binary number represented by a linked list into its integer value.",
}

from typing import Optional


class ListNode:
    """Singly-linked list node used by LeetCode."""
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = next


def solve(head: Optional[ListNode]) -> int:
    """Convert a binary number stored in a linked list to an integer.

    Args:
        head: The head node of a singly-linked list where each node's value
              is either 0 or 1, representing bits from most‑significant to
              least‑significant.

    Returns:
        The integer value of the binary number.

    Examples:
        >>> # binary 101 (5)
        >>> node3 = ListNode(1)
        >>> node2 = ListNode(0, node3)
        >>> node1 = ListNode(1, node2)
        >>> solve(node1)
        5

        >>> # binary 0 (0)
        >>> solve(ListNode(0))
        0
    """
    integer_value: int = 0
    current_node: Optional[ListNode] = head

    while current_node is not None:
        # Shift left to make room for the next bit, then add current bit.
        integer_value = (integer_value << 1) | current_node.val
        current_node = current_node.next

    return integer_value