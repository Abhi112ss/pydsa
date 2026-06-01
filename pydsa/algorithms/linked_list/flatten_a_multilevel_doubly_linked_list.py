METADATA = {
    "id": 430,
    "name": "Flatten a Multilevel Doubly Linked List",
    "slug": "flatten-a-multilevel-doubly-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["dfs", "stack", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Flatten a multilevel doubly linked list where nodes may have a child pointer to another doubly linked list.",
}

class Node:
    def __init__(self, val: int, prev: 'Node' = None, next: 'Node' = None, child: 'Node' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def solve(head: Node | None) -> Node | None:
    """
    Flattens a multilevel doubly linked list into a single-level doubly linked list.

    The flattening is done such that the child list is inserted between the 
    current node and its next node. This is equivalent to a pre-order 
    traversal of a tree where 'child' is the left child and 'next' is the right child.

    Args:
        head: The head of the multilevel doubly linked list.

    Returns:
        The head of the flattened doubly linked list.

    Examples:
        >>> # Example 1
        >>> # Input: 1 <-> 2 <-> 3, 2 has child 4 <-> 5
        >>> # Output: 1 <-> 2 <-> 4 <-> 5 <-> 3
        >>> head = Node(1, next=Node(2, next=Node(3)))
        >>> head.next.child = Node(4, next=Node(5))
        >>> new_head = solve(head)
        >>> new_head.next.val == 2 and new_head.next.next.val == 4
        True
    """
    if not head:
        return None

    # We use a stack to simulate DFS (pre-order traversal).
    # When we encounter a child, we want to process it before the 'next' node.
    # By pushing 'next' onto the stack first, we ensure 'child' is popped and processed first.
    stack: list[Node] = [head]
    dummy = Node(0)
    prev_node: Node | None = dummy

    while stack:
        current = stack.pop()

        # Connect the previous node with the current node
        prev_node.next = current
        current.prev = prev_node

        # If there is a next node, push it to the stack to process later
        if current.next:
            stack.append(current.next)

        # If there is a child, push it to the stack to process next (LIFO)
        if current.child:
            stack.append(current.child)
            # Crucial: clear the child pointer as per problem requirements
            current.child = None
        
        prev_node = current

    # The dummy node's next is the real head. 
    # We must detach the dummy's prev link from the actual head.
    real_head = dummy.next
    if real_head:
        real_head.prev = None
        
    return real_head
