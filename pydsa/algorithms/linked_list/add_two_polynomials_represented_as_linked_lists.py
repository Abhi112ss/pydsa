METADATA = {
    "id": 1634,
    "name": "Add Two Polynomials Represented as Linked Lists",
    "slug": "add-two-polynomials-represented-as-linked-lists",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Add two polynomials represented by linked lists where each node contains a coefficient and an exponent.",
}

class ListNode:
    def __init__(self, coeff: int, exp: int, next_node: 'ListNode' = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next_node

def solve(poly1: ListNode, poly2: ListNode) -> ListNode:
    """
    Adds two polynomials represented as linked lists.

    Args:
        poly1: The head of the first linked list representing the first polynomial.
        poly2: The head of the second linked list representing the second polynomial.

    Returns:
        The head of a new linked list representing the sum of the two polynomials.
    """
    dummy_head = ListNode(0, 0)
    current_node = dummy_head
    
    pointer1 = poly1
    pointer2 = poly2

    while pointer1 is not None or pointer2 is not None:
        if pointer1 is not None and pointer2 is not None:
            if pointer1.exp == pointer2.exp:
                new_coeff = pointer1.coeff + pointer2.coeff
                if new_coeff != 0:
                    current_node.next = ListNode(new_coeff, pointer1.exp)
                    current_node = current_node.next
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            elif pointer1.exp > pointer2.exp:
                current_node.next = ListNode(pointer1.coeff, pointer1.exp)
                current_node = current_node.next
                pointer1 = pointer1.next
            else:
                current_node.next = ListNode(pointer2.coeff, pointer2.exp)
                current_node = current_node.next
                pointer2 = pointer2.next
        elif pointer1 is not None:
            current_node.next = ListNode(pointer1.coeff, pointer1.exp)
            current_node = current_node.next
            pointer1 = pointer1.next
        else:
            current_node.next = ListNode(pointer2.coeff, pointer2.exp)
            current_node = current_node.next
            pointer2 = pointer2.next

    return dummy_head.next