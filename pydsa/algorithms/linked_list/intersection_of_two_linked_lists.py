METADATA = {
    "id": 160,
    "name": "Intersection of Two Linked Lists",
    "slug": "intersection-of-two-linked-lists",
    "category": "Linked List",
    "aliases": [],
    "tags": ["two_pointers", "linked_list"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(1)",
    "description": "Find the node where two singly linked lists intersect.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, x: int):
        self.val = x
        self.next = None

def solve(head_a: ListNode | None, head_b: ListNode | None) -> ListNode | None:
    """
    Finds the intersection node of two singly linked lists using the two-pointer technique.

    The algorithm works by having two pointers traverse both lists. When a pointer 
    reaches the end of one list, it jumps to the head of the other list. This 
    ensures that both pointers travel the same total distance (length_a + length_b), 
    causing them to meet at the intersection point or at None if no intersection exists.

    Args:
        head_a: The head of the first linked list.
        head_b: The head of the second linked list.

    Returns:
        The node where the two lists intersect, or None if there is no intersection.

    Examples:
        >>> # Example 1: Intersection exists
        >>> a1 = ListNode(4); a2 = ListNode(1); a3 = ListNode(8); a4 = ListNode(4); a5 = ListNode(5)
        >>> b1 = ListNode(5); b2 = ListNode(0); b3 = ListNode(1); b4 = ListNode(8); b5 = ListNode(4); b6 = ListNode(5)
        >>> a1.next = a2; a2.next = a3; a3.next = a4; a4.next = a5
        >>> b1.next = b2; b2.next = b3; b3.next = b4; b4.next = b5; b5.next = b6
        >>> # Connect a3 to b4 to create intersection at node with val 8
        >>> a3.next = b4
        >>> solve(a1, b1) # Returns b4 (the node with val 8)

        >>> # Example 2: No intersection
        >>> solve(a1, ListNode(10)) # Returns None
    """
    if not head_a or not head_b:
        return None

    pointer_a = head_a
    pointer_b = head_b

    # If the lists intersect, the pointers will meet at the intersection node.
    # If they don't intersect, they will both eventually become None at the same time
    # after completing one full cycle of (length_a + length_b).
    while pointer_a is not pointer_b:
        # Move to the next node, or switch to the head of the other list
        pointer_a = pointer_a.next if pointer_a else head_b
        pointer_b = pointer_b.next if pointer_b else head_a

    return pointer_a