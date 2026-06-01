METADATA = {
    "id": 1019,
    "name": "Next Greater Node In Linked List",
    "slug": "next-greater-node-in-linked-list",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the next greater element for each node in a linked list, returning -1 if no such element exists.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> list[int]:
    """
    Finds the next greater element for each node in a linked list using a monotonic stack.

    Args:
        head: The head of a singly-linked list.

    Returns:
        A list of integers where the i-th element is the value of the next greater 
        node of the i-th node in the linked list. If no next greater node exists, 
        the value is -1.

    Examples:
        >>> head = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))
        >>> solve(head)
        [7, -1, 5, 5, -1]
        
        >>> head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))) )
        >>> solve(head)
        [2, 3, 4, -1]
    """
    # Step 1: Convert the linked list to an array for O(1) random access
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    n = len(values)
    result = [-1] * n
    # The stack will store indices of elements for which we haven't found 
    # a greater element yet.
    stack: list[int] = []
    
    # Step 2: Use a monotonic decreasing stack to find the next greater element
    for i in range(n):
        # While the current value is greater than the value at the index 
        # stored at the top of the stack, we have found the next greater element.
        while stack and values[i] > values[stack[-1]]:
            index_to_update = stack.pop()
            result[index_to_update] = values[i]
        
        # Push the current index onto the stack
        stack.append(i)
        
    return result
