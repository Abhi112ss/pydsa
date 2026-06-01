from typing import Optional

METADATA = {
    "id": 173,
    "name": "Binary Search Tree Iterator",
    "slug": "binary_search_tree_iterator",
    "category": "tree",
    "aliases": ["BST Iterator"],
    "tags": ["stack", "tree", "design", "binary-search-tree", "iterator"],
    "difficulty": "medium",
    "time_complexity": "O(1) average",
    "space_complexity": "O(h)",
    "description": "Implement an iterator over a binary search tree (BST) that returns nodes in in-order traversal using a stack to simulate recursion.",
}


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    """
    Iterator for binary search tree in-order traversal.
    
    Maintains a stack of nodes representing the left-most path from the current root.
    """

    def __init__(self, root: Optional[TreeNode]):
        """
        Initializes the iterator with the root of the BST.
        
        Args:
            root: The root node of the binary search tree.
        """
        self.stack: list[TreeNode] = []
        # Initialize the stack with the left-most path from the root
        self._push_left_path(root)

    def _push_left_path(self, node: Optional[TreeNode]) -> None:
        """
        Helper function to push all left children of a node onto the stack.
        
        Args:
            node: The starting node to traverse left from.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Returns the next smallest element in the BST.
        
        Returns:
            The value of the next smallest node.
        """
        # The top of the stack is the next smallest element
        node = self.stack.pop()
        
        # If the node has a right child, we must process its left-most path
        if node.right:
            self._push_left_path(node.right)
            
        return node.val

    def hasNext(self) -> bool:
        """
        Checks whether there are more elements in the BST.
        
        Returns:
            True if there are more elements, False otherwise.
        """
        return len(self.stack) > 0


def solve() -> type[BSTIterator]:
    """
    Returns the BSTIterator class implementation.

    Returns:
        The BSTIterator class.

    Examples:
        >>> root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        >>> iterator = BSTIterator(root)
        >>> iterator.next()
        3
        >>> iterator.next()
        7
        >>> iterator.hasNext()
        True
        >>> iterator.next()
        9
        >>> iterator.hasNext()
        True
        >>> iterator.next()
        15
        >>> iterator.hasNext()
        True
        >>> iterator.next()
        20
        >>> iterator.hasNext()
        False
    """
    return BSTIterator