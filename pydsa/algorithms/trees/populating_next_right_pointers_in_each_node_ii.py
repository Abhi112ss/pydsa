METADATA = {
    "id": 117,
    "name": "Populating Next Right Pointers in Each Node II",
    "slug": "populating-next-right-pointers-in-each-node-ii",
    "category": "Trees",
    "aliases": [],
    "tags": ["binary tree", "breadth-first search", "linked list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Populate each node's next pointer to point to its next right neighbor in a perfect binary tree, using constant extra space.",
}

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def solve(root: Node | None) -> Node | None:
    """
    Populates the next pointers for each node in a binary tree.

    The algorithm uses a level-order traversal approach without an explicit queue.
    Instead, it treats the current level as a linked list (using the 'next' pointers)
    to build the linked list for the next level.

    Args:
        root: The root of the binary tree.

    Returns:
        The root of the modified tree where each node's next pointer points to its 
        immediate right neighbor on the same level.

    Examples:
        >>> root = Node(1, Node(2), Node(3), None)
        >>> solve(root)
        Node(1, next=Node(3), left=Node(2, next=None), right=Node(3, next=None))
    """
    if not root:
        return None

    # 'current_level_head' tracks the start of the level we are currently processing
    current_level_head = root

    while current_level_head:
        # dummy_node acts as a placeholder to build the linked list for the next level
        dummy_node = Node(0)
        # 'tail' will be used to append nodes to the next level's linked list
        tail = dummy_node
        
        # Traverse the current level using the 'next' pointers established in the previous pass
        curr = current_level_head
        while curr:
            # If the current node has a left child, link it to the next level's list
            if curr.left:
                tail.next = curr.left
                tail = tail.next
            
            # If the current node has a right child, link it to the next level's list
            if curr.right:
                tail.next = curr.right
                tail = tail.next
            
            # Move to the next node in the current level
            curr = curr.next
        
        # Move to the start of the next level (the first node attached to dummy_node)
        current_level_head = dummy_node.next

    return root