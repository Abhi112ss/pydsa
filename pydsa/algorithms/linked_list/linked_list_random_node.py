METADATA = {
    "id": 382,
    "name": "Linked List Random Node",
    "slug": "linked-list-random-node",
    "category": "Random",
    "aliases": [],
    "tags": ["reservoir_sampling", "randomized", "linked-list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a linked list, return a random node from the list such that each node has an equal probability of being chosen.",
}

import random

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode) -> ListNode:
    """
    Selects a random node from a linked list using Reservoir Sampling.
    
    This algorithm ensures that each node in the list has a 1/n probability 
    of being selected, where n is the total number of nodes, without 
    knowing the length of the list in advance.

    Args:
        head: The head of the singly-linked list.

    Returns:
        A reference to a randomly selected ListNode.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> node = solve(head)
        >>> node.val in [1, 2, 3]
        True
    """
    if not head:
        return None

    result_node = head
    current_node = head
    count = 0

    # Iterate through the list once
    while current_node:
        count += 1
        
        # For the i-th node (1-indexed), replace the current result 
        # with the current node with probability 1/i.
        # random.randint(1, count) == 1 has a 1/count probability.
        if random.randint(1, count) == 1:
            result_node = current_node
            
        current_node = current_node.next

    return result_node
