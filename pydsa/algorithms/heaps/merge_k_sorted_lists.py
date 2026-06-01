METADATA = {
    "id": 23,
    "name": "Merge k Sorted Lists",
    "slug": "merge-k-sorted-lists",
    "category": "Linked List",
    "aliases": [],
    "tags": ["heap", "priority_queue", "linked_list", "divide_and_conquer"],
    "difficulty": "hard",
    "time_complexity": "O(N log k)",
    "space_complexity": "O(k)",
    "description": "Merge k sorted linked lists into one sorted linked list.",
}

from typing import Optional, Any
import heapq

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __lt__(self, other: Any) -> bool:
        """Helper to allow ListNode comparison in the priority queue."""
        return self.val < other.val

def solve(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists into one sorted linked list using a min-heap.

    Args:
        lists: A list of the head nodes of k sorted linked lists.

    Returns:
        The head node of the merged sorted linked list.

    Examples:
        >>> l1 = ListNode(1, ListNode(4, ListNode(5)))
        >>> l2 = ListNode(1, ListNode(3, ListNode(4)))
        >>> l3 = ListNode(2, ListNode(6))
        >>> merged = solve([l1, l2, l3])
        >>> # merged represents 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
    """
    min_heap = []

    # Initialize the heap with the head of each non-empty list.
    # We store a tuple (node.val, id(node), node) to handle cases where 
    # multiple nodes have the same value, preventing the heap from 
    # attempting to compare ListNode objects directly if __lt__ wasn't defined.
    for head in lists:
        if head:
            heapq.heappush(min_heap, (head.val, id(head), head))

    dummy_head = ListNode(0)
    current_tail = dummy_head

    while min_heap:
        # Extract the smallest element currently in the heap.
        val, _, smallest_node = heapq.heappop(min_heap)
        
        # Append the smallest node to our result list.
        current_tail.next = smallest_node
        current_tail = current_tail.next

        # If the extracted node has a next node, push it into the heap.
        if smallest_node.next:
            next_node = smallest_node.next
            heapq.heappush(min_heap, (next_node.val, id(next_node), next_node))

    return dummy_head.next
