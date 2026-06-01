METADATA = {
    "id": 24,
    "name": "Swap Nodes in Pairs",
    "slug": "swap-nodes-in-pairs",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "recursion", "pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a linked list, swap every two adjacent nodes and return its head.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Swaps every two adjacent nodes in a linked list iteratively.

    Args:
        head: The head of the singly-linked list.

    Returns:
        The head of the modified linked list after swapping pairs.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        >>> solve(head).val
        2
    """
    # Use a dummy node to simplify edge cases like swapping the head
    dummy = ListNode(0)
    dummy.next = head
    current_prev = dummy

    # Iterate as long as there is a pair of nodes available to swap
    while current_prev.next and current_prev.next.next:
        # Identify the two nodes to be swapped
        first_node = current_prev.next
        second_node = current_prev.next.next

        # Perform the swap by adjusting pointers
        # 1. Point first node to the node after the pair
        first_node.next = second_node.next
        # 2. Point second node to the first node
        second_node.next = first_node
        # 3. Connect the previous part of the list to the new first node of the pair
        current_prev.next = second_node

        # Move the pointer forward by two nodes for the next iteration
        current_prev = first_node

    return dummy.next
