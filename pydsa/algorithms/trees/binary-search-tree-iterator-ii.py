METADATA = {
    "id": 1586,
    "name": "Binary Search Tree Iterator II",
    "slug": "binary-search-tree-iterator-ii",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "stack", "iterator", "binary-search-tree"],
    "difficulty": "medium",
    "time_complexity": "O(1) average, O(h) worst case for next()",
    "space_complexity": "O(h)",
    "description": "Implement an iterator over a binary search tree that returns the nodes' values in ascending order.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        """
        Initializes the iterator with the root of the BST.
        
        Args:
            root (TreeNode): The root node of the binary search tree.
        """
        self.stack: list[TreeNode] = []
        # Initialize the stack by pushing all left children from the root
        self._push_left_children(root)

    def _push_left_children(self, node: TreeNode) -> None:
        """Helper to push all left descendants of a node onto the stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Returns the next smallest number in the BST.

        Returns:
            int: The next smallest value.
        """
        # The top of the stack is the current smallest element
        top_node = self.stack.pop()
        
        # If the popped node has a right child, we must process its 
        # left-most descendants to maintain the in-order property
        if top_node.right:
            self._push_left_children(top_node.right)
            
        return top_node.val

    def hasNext(self) -> bool:
        """
        Returns whether we have a next smallest number.

        Returns:
            bool: True if there are more elements, False otherwise.
        """
        return len(self.stack) > 0

def solve(root: TreeNode) -> BSTIterator:
    """
    Entry point to create the iterator.

    Args:
        root (TreeNode): The root of the BST.

    Returns:
        BSTIterator: An iterator instance.
    """
    return BSTIterator(root)

# Example usage/test structure
