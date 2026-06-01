METADATA = {
    "id": 1367,
    "name": "Linked List in Binary Tree",
    "slug": "linked-list-in-binary-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "linked-list"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine if a linked list can be formed by a path in a binary tree.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(root: TreeNode | None, head: ListNode | None) -> bool:
    """
    Determines if the values of a linked list can be found in a path 
    from the root to a leaf in a binary tree.

    Args:
        root: The root node of the binary tree.
        head: The head node of the linked list.

    Returns:
        True if the linked list exists as a path in the tree, False otherwise.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> solve(root, head)
        True
    """
    if not root:
        return False

    # If the current node's value doesn't match the current linked list node's value,
    # this path is invalid.
    if root.val != head.val:
        return False

    # If we have reached the end of the linked list, we must ensure 
    # the current tree node is a leaf node.
    if not head.next:
        return root.left is None and root.right is None

    # Recursively check left and right subtrees for the next node in the linked list.
    # The path must continue through one of the children.
    return solve(root.left, head.next) or solve(root.right, head.next)
