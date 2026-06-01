METADATA = {
    "id": 445,
    "name": "Add Two Numbers II",
    "slug": "add-two-numbers-ii",
    "category": "Linked List",
    "aliases": [],
    "tags": ["stack", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Add two numbers represented by linked lists where digits are stored in most-significant-digit order.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Args:
        l1: The head of the first linked list.
        l2: The head of the second linked list.

    Returns:
        The head of the resulting linked list representing the sum.
    """
    stack_one = []
    stack_two = []

    current_one = l1
    while current_one:
        stack_one.append(current_one.val)
        current_one = current_one.next

    current_two = l2
    while current_two:
        stack_two.append(current_two.val)
        current_two = current_two.next

    carry = 0
    dummy_head = ListNode(0)
    current_node = dummy_head

    while stack_one or stack_two or carry:
        val_one = stack_one.pop() if stack_one else 0
        val_two = stack_two.pop() if stack_two else 0
        
        total_sum = val_one + val_two + carry
        carry = total_sum // 10
        digit = total_sum % 10
        
        current_node.next = ListNode(digit)
        current_node = current_node.next

    result_head = dummy_head.next
    
    if not result_head:
        return ListNode(0)

    previous = None
    current = result_head
    while current:
        previous = current
        current = current.next
    
    return previous.next if not result_head else reverse_list(result_head)

def reverse_list(head: ListNode) -> ListNode:
    """
    Args:
        head: The head of the linked list to reverse.

    Returns:
        The new head of the reversed linked list.
    """
    previous_node = None
    current_node = head
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node

def solve(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Args:
        l1: The head of the first linked list.
        l2: The head of the second linked list.

    Returns:
        The head of the resulting linked list representing the sum.
    """
    stack_one = []
    stack_two = []

    current_one = l1
    while current_one:
        stack_one.append(current_one.val)
        current_one = current_one.next

    current_two = l2
    while current_two:
        stack_two.append(current_two.val)
        current_two = current_two.next

    carry = 0
    dummy_head = ListNode(0)
    current_node = dummy_head

    while stack_one or stack_two or carry:
        val_one = stack_one.pop() if stack_one else 0
        val_two = stack_two.pop() if stack_two else 0
        
        total_sum = val_one + val_two + carry
        carry = total_sum // 10
        digit = total_sum % 10
        
        current_node.next = ListNode(digit)
        current_node = current_node.next

    result_head = dummy_head.next
    
    prev = None
    curr = result_head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev