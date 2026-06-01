METADATA = {
    "id": 109,
    "name": "Convert Sorted List to Binary Search Tree",
    "slug": "convert-sorted-list-to-binary-search-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "linked_list", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(log n)",
    "description": "Convert a sorted singly linked list to a height-balanced binary search tree.",
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(head: ListNode) -> TreeNode:
    """
    Converts a sorted singly linked list into a height-balanced BST.

    The algorithm uses the slow and fast pointer technique to find the middle 
    element of the linked list, which becomes the root of the current subtree. 
    This process is applied recursively to the left and right halves.

    Args:
        head: The head of the sorted singly linked list.

    Returns:
        The root of the converted height-balanced binary search tree.

    Examples:
        >>> head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(10)))))
        >>> root = solve(head)
        >>> # root.val is 0, root.left.val is -3, root.right.val is 5
    """
    if not head:
        return None
    
    if not head.next:
        return TreeNode(head.val)

    # Use slow and fast pointers to find the middle of the linked list
    # 'prev' is used to disconnect the left half from the middle node
    prev = None
    slow = head
    fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # 'slow' is now the middle node. Disconnect the left half.
    if prev:
        prev.next = None

    # Create the root node from the middle element
    root = TreeNode(slow.val)

    # Recursively build the left subtree using the head (now truncated)
    root.left = solve(head)
    
    # Recursively build the right subtree using the node after the middle
    root.right = solve(slow.next)

    return root