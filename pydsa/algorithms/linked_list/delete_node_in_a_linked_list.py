METADATA = {
    "id": 237,
    "name": "Delete Node in a Linked List",
    "slug": "delete-node-in-a-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Delete a node from a singly linked list, given access only to that node.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None

def solve(node: ListNode) -> None:
    """
    Deletes the given node from a singly linked list by copying the next node's 
    data and skipping the next node.

    Args:
        node: The node to be deleted. The node is guaranteed not to be the tail.

    Returns:
        None. The operation is performed in-place.

    Examples:
        >>> head = ListNode(4)
        >>> head.next = ListNode(5)
        >>> head.next.next = ListNode(1)
        >>> head.next.next.next = ListNode(9)
        >>> solve(head.next) # Delete node with value 5
        >>> head.next.val
        1
    """
    # Since we don't have access to the previous node, we cannot change 
    # the 'next' pointer of the predecessor. Instead, we copy the 
    # value of the next node into the current node.
    node.val = node.next.val
    
    # We then bypass the next node by pointing the current node's 
    # 'next' pointer to the node after the next one.
    node.next = node.next.next