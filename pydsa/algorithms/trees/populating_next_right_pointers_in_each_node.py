METADATA = {
    "id": 116,
    "name": "Populating Next Right Pointers in Each Node",
    "slug": "populating-next-right-pointers-in-each-node",
    "category": "Trees",
    "aliases": [],
    "tags": ["binary tree", "breadth-first search", "pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Connect each node to its next right neighbor in a perfect binary tree using existing next pointers.",
}

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def solve(root: Node | None) -> Node | None:
    """
    Populates the next pointers for a perfect binary tree.

    Args:
        root: The root of the perfect binary tree.

    Returns:
        The root of the modified tree where each node's next pointer 
        points to its immediate right neighbor on the same level.

    Examples:
        >>> root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        >>> solve(root)
        Node(1, next=None, left=Node(2, next=Node(3), ...), ...)
    """
    if not root:
        return None

    # Start with the root node as the first node of the current level
    leftmost = root

    # Since it's a perfect binary tree, we can iterate level by level
    # until we reach the leaf level.
    while leftmost.left:
        # 'current' acts as a cursor to traverse the current level
        # and connect the children of the next level.
        current = leftmost
        
        while current:
            # Connection 1: Connect the left child to the right child of the same parent
            current.left.next = current.right

            # Connection 2: Connect the right child of the current node 
            # to the left child of the current node's next neighbor.
            if current.next:
                current.right.next = current.next.left
            
            # Move to the next node in the current level
            current = current.next
        
        # Move down to the next level's leftmost node
        leftmost = leftmost.left

    return root