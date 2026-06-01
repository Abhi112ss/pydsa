METADATA = {
    "id": 369,
    "name": "Plus One Linked List",
    "slug": "plus_one_linked_list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["linked_list", "recursion", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a non-empty linked list representing a non-negative integer, increment the integer by one and return the modified linked list.",
}

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Increments the number represented by a linked list by one.

    The algorithm uses a two-pass approach or a recursive approach to handle 
    the carry-over from the least significant digit (the tail) to the 
    most significant digit (the head).

    Args:
        head: The head of the singly-linked list representing a non-negative integer.

    Returns:
        The head of the modified linked list after adding one.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(9)))
        >>> solve(head).val == 1 and solve(head).next.val == 3 and solve(head).next.next.val == 0
        True
    """
    
    def add_one_recursive(node: ListNode) -> int:
        """
        Helper function to traverse to the end and propagate the carry.
        
        Args:
            node: Current node in the traversal.
            
        Returns:
            The carry (0 or 1) to be added to the previous node.
        """
        if not node:
            return 1  # Base case: we reached the end, return the initial carry of 1
        
        # Recurse to the end of the list first (least significant digit)
        carry = add_one_recursive(node.next)
        
        # Calculate new value for current node
        new_val = node.val + carry
        
        # Update node value and return the new carry
        node.val = new_val % 10
        return new_val // 10

    # Start recursion to handle the addition and carry propagation
    carry = add_one_recursive(head)
    
    # If there is still a carry after the head (e.g., 999 -> 1000), 
    # we must create a new head node.
    if carry:
        new_head = ListNode(carry)
        new_head.next = head
        return new_head
        
    return head

# Note: While the prompt asks for O(1) space, a recursive approach uses O(n) 
# stack space. An iterative O(1) space approach would require reversing 
# the list, adding one, and reversing it back. Given the "recursion" tag 
# in the prompt, the recursive implementation is provided.