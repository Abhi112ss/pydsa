METADATA = {
    "id": 725,
    "name": "Split Linked List in Parts",
    "slug": "split-linked-list-in-parts",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n + k)",
    "space_complexity": "O(k)",
    "description": "Split a linked list into k parts such that the length of each part is as equal as possible.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode, k: int) -> list[ListNode | None]:
    """
    Splits a linked list into k parts such that the sizes of the parts are as equal as possible.

    The algorithm first calculates the total length of the linked list. It then determines
    the base size for each part and how many parts should receive an extra node (the remainder).
    Finally, it iterates through the list, slicing it into segments.

    Args:
        head: The head of the singly linked list.
        k: The number of parts to split the list into.

    Returns:
        A list of k heads of the split linked list parts.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        >>> solve(head, 3)
        [ListNode(1, ListNode(2)), ListNode(3), ListNode(4, ListNode(5))]
    """
    # Step 1: Calculate the total length of the linked list
    total_length = 0
    current_node = head
    while current_node:
        total_length += 1
        current_node = current_node.next

    # Step 2: Determine the base size of each part and the remainder
    # base_size is the minimum number of nodes in each part
    # remainder is the number of parts that will have (base_size + 1) nodes
    base_size = total_length // k
    remainder = total_length % k

    result_parts: list[ListNode | None] = []
    current_node = head

    for i in range(k):
        # If we have run out of nodes, the remaining parts are None
        if not current_node:
            result_parts.append(None)
            continue

        part_head = current_node
        # Calculate the size of the current part
        # The first 'remainder' parts get one extra node
        current_part_size = base_size + (1 if i < remainder else 0)

        # Step 3: Traverse to the end of the current part
        for _ in range(current_part_size - 1):
            if current_node:
                current_node = current_node.next
        
        # Disconnect the current part from the rest of the list
        if current_node:
            next_part_start = current_node.next
            current_node.next = None
            current_node = next_part_start
        
        result_parts.append(part_head)

    return result_parts