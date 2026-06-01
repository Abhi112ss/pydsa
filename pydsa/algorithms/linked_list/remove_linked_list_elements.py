METADATA = {
    "id": 203,
    "name": "Remove Linked List Elements",
    "slug": "remove_linked_list_elements",
    "category": "Linked List",
    "aliases": ["remove_elements", "delete_nodes"],
    "tags": ["linked_list", "recursion"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Remove all nodes from a linked list that have a specific value.",
}

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def solve(head: ListNode, val: int) -> ListNode:
    """
    Remove all nodes from the linked list that have the given value.

    Uses a dummy head node to simplify edge cases where the head itself
    needs to be removed. Iterates through the list, skipping nodes
    whose value matches the target.

    Args:
        head: The head node of the singly-linked list.
        val: The integer value to remove from the list.

    Returns:
        The head of the modified linked list after removals.

    Examples:
        >>> # List: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6, val = 6
        >>> nodes = [ListNode(v) for v in [1,2,6,3,4,5,6]]
        >>> for i in range(len(nodes)-1): nodes[i].next = nodes[i+1]
        >>> result = solve(nodes[0], 6)
        >>> output = []
        >>> while result: output.append(result.val); result = result.next
        >>> output
        [1, 2, 3, 4, 5]

        >>> # List: 7 -> 7 -> 7 -> 7, val = 7
        >>> nodes = [ListNode(7) for _ in range(4)]
        >>> for i in range(len(nodes)-1): nodes[i].next = nodes[i+1]
        >>> result = solve(nodes[0], 7)
        >>> result is None
        True

        >>> # Empty list
        >>> solve(None, 1) is None
        True
    """
    # Create a dummy node pointing to head — handles head-removal edge case
    dummy = ListNode(0)
    dummy.next = head

    current = dummy

    # Traverse the list; skip nodes whose val matches the target
    while current.next is not None:
        if current.next.val == val:
            # Bypass the node with the target value
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next