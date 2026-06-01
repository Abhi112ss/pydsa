METADATA = {
    "id": 919,
    "name": "Complete Binary Tree Inserter",
    "slug": "complete-binary-tree-inserter",
    "category": "Design",
    "aliases": [],
    "tags": ["binary_tree", "bfs", "design", "queue"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a data structure that supports inserting nodes into a complete binary tree.",
}

from collections import deque


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class CompleteBinaryTreeInserter:
    """
    A class to manage a complete binary tree with O(1) insertion.
    
    The class maintains a queue of nodes that have at least one empty child slot.
    This allows us to find the next insertion point in constant time.
    """

    def __init__(self, init_val: int):
        """
        Initializes the tree with a single root node.

        Args:
            init_val (int): The value of the root node.
        """
        self.root = TreeNode(init_val)
        # The queue stores nodes that are candidates for having children added.
        # A node is a candidate if it has 0 or 1 child.
        self.available_nodes = deque([self.root])

    def insert(self, val: int) -> bool:
        """
        Inserts a new node into the complete binary tree.

        Args:
            val (int): The value to be inserted.

        Returns:
            bool: True if the insertion was successful, False otherwise.
            (In this specific problem, it always returns True as long as 
            the tree is complete and we follow the queue logic).

        Examples:
            >>> cbt = CompleteBinaryTreeInserter(1)
            >>> cbt.insert(2)
            True
            >>> cbt.insert(3)
            True
        """
        # Get the first node in the queue that can accept a child
        parent = self.available_nodes[0]

        # Create the new node
        new_node = TreeNode(val)

        # Fill the left child if available
        if parent.left is None:
            parent.left = new_node
        # Otherwise, fill the right child
        elif parent.right is None:
            parent.right = new_node
            # Once the right child is filled, this parent can no longer accept children
            self.available_nodes.popleft()
        else:
            # This case should not be reachable if the queue is maintained correctly
            return False

        # If the newly added node has no children, it is a candidate for future insertions
        self.available_nodes.append(new_node)

        return True


def solve():
    """
    Example usage of the CompleteBinaryTreeInserter.
    """
    cbt = CompleteBinaryTreeInserter(1)
    print(f"Insert 2: {cbt.insert(2)}")  # True
    print(f"Insert 3: {cbt.insert(3)}")  # True
    print(f"Insert 4: {cbt.insert(4)}")  # True
    print(f"Insert 5: {cbt.insert(5)}")  # True
