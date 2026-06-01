METADATA = {
    "id": 1171,
    "name": "Remove Zero Sum Consecutive Nodes from Linked List",
    "slug": "remove-zero-sum-consecutive-nodes-from-linked-list",
    "category": "Linked List",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map", "linked_list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove all consecutive nodes from a linked list that sum to zero.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode | None) -> ListNode | None:
    """
    Removes all consecutive nodes from a linked list that sum to zero.

    The algorithm uses a prefix sum approach. We traverse the list and maintain
    a running sum. We store the last node encountered for every prefix sum in a 
    hash map. If we encounter the same prefix sum again, it means the nodes 
    between the previous occurrence and the current node sum to zero.

    Args:
        head: The head of the singly linked list.

    Returns:
        The head of the modified linked list with zero-sum segments removed.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1))))
        >>> solve(head)
        ListNode(3, ListNode(1))
    """
    # Create a dummy node to handle cases where the head itself is part of a zero-sum sequence
    dummy = ListNode(0)
    dummy.next = head
    
    # Map to store the last node seen for a specific prefix sum
    prefix_sum_map: dict[int, ListNode] = {}
    
    current_sum = 0
    current_node = dummy
    
    # First pass: Populate the map with the last node encountered for each prefix sum
    while current_node:
        current_sum += current_node.val
        prefix_sum_map[current_sum] = current_node
        current_node = current_node.next
        
    # Second pass: Re-traverse and link nodes to the last seen node for each prefix sum
    # This effectively skips all nodes that sum to zero between two identical prefix sums
    current_sum = 0
    current_node = dummy
    while current_node:
        current_sum += current_node.val
        # If the sum was seen before, current_node.next should skip to the node 
        # stored in the map, effectively removing the zero-sum segment.
        current_node.next = prefix_sum_map[current_sum].next
        current_node = current_node.next
        
    return dummy.next
