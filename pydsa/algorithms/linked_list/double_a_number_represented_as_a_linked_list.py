METADATA = {
    "id": 2816,
    "name": "Double a Number Represented as a Linked List",
    "slug": "double-a-number-represented-as-a-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Double a number represented as a singly linked list where each node contains a single digit.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Doubles a number represented as a linked list by traversing it and handling carries.

    Args:
        head: The head of a singly linked list representing a non-negative integer.

    Returns:
        The head of the new linked list representing the doubled value.

    Examples:
        >>> head = ListNode(1, ListNode(8))
        >>> solve(head).val == 1 and solve(head).next.val == 6
        True
        >>> head = ListNode(9)
        >>> solve(head).val == 1 and solve(head).next.val == 8
        True
    """
    # Step 1: Reverse the linked list to process digits from least significant to most significant.
    # This allows us to handle carries easily in a single pass.
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # 'prev' is now the head of the reversed list.
    reversed_head = prev
    carry = 0
    current = reversed_head
    
    # Step 2: Iterate through the reversed list, doubling each digit and managing the carry.
    while current:
        new_val = current.val * 2 + carry
        current.val = new_val % 10
        carry = new_val // 10
        current = current.next
        
    # Step 3: If there is a remaining carry after the last node, create a new node.
    if carry > 0:
        new_node = ListNode(carry)
        new_node.next = reversed_head
        reversed_head = new_node
        
    # Step 4: Reverse the list back to its original order.
    prev = None
    current = reversed_head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev