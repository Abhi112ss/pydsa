METADATA = {
    "id": 817,
    "name": "Linked List Components",
    "slug": "linked-list-components",
    "category": "Linked List",
    "aliases": [],
    "tags": ["hash_set", "traversal", "linked-list"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Count the number of connected components in a linked list where nodes are part of a given subset.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head: ListNode, subset: list[int]) -> int:
    """
    Counts the number of connected components in a linked list based on a subset.

    A component is defined as a maximal sequence of nodes where each node's 
    value is present in the subset.

    Args:
        head: The head of the singly linked list.
        subset: A list of integers representing the values that belong to components.

    Returns:
        The total number of connected components.

    Examples:
        >>> head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
        >>> subset = [0, 1, 3, 4]
        >>> solve(head, subset)
        2
    """
    # Convert subset to a set for O(1) average time complexity lookups
    subset_set = set(subset)
    component_count = 0
    in_component = False
    
    current_node = head
    while current_node:
        # Check if the current node's value is in the subset
        if current_node.val in subset_set:
            # If we weren't previously in a component, we just found a new one
            if not in_component:
                component_count += 1
                in_component = True
        else:
            # If the value is not in the subset, the current component (if any) has ended
            in_component = False
            
        current_node = current_node.next
        
    return component_count
