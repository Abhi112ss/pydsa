METADATA = {
    "id": 449,
    "name": "Serialize and Deserialize BST",
    "slug": "serialize-and-deserialize-bst",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "dfs", "binary search tree", "design"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Design an algorithm to serialize and deserialize a binary search tree.",
}

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        """Serializes a tree to a single string.

        Args:
            root: The root of the BST.

        Returns:
            A string representation of the tree using preorder traversal.

        Examples:
            >>> codec = Codec()
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3))
            >>> codec.serialize(root)
            '1,2,3'
        """
        if not root:
            return ""
        
        result = []

        def preorder(node: TreeNode | None) -> None:
            if not node:
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode | None:
        """Deserializes your encoded data to tree.

        Args:
            data: The serialized string.

        Returns:
            The root of the reconstructed BST.

        Examples:
            >>> codec = Codec()
            >>> data = "1,2,3"
            >>> root = codec.deserialize(data)
            >>> root.val
            1
        """
        if not data:
            return None

        # Convert string to a list of integers for efficient access
        values = [int(x) for x in data.split(",")]
        self.index = 0

        def build_bst(lower_bound: float, upper_bound: float) -> TreeNode | None:
            # If we've exhausted values or the current value is out of BST range
            if self.index >= len(values):
                return None
            
            val = values[self.index]
            if not (lower_bound < val < upper_bound):
                return None

            # Consume the value and create the node
            self.index += 1
            root = TreeNode(val)

            # Use BST properties: left child must be < current, right child must be > current
            root.left = build_bst(lower_bound, val)
            root.right = build_bst(val, upper_bound)
            
            return root

        return build_bst(float("-inf"), float("inf"))

def solve():
    """Entry point for testing the implementation."""
    codec = Codec()
    
    # Test Case 1: Standard BST
    #      2
    #     / \
    #    1   3
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    serialized1 = codec.serialize(root1)
    deserialized1 = codec.deserialize(serialized1)
    assert deserialized1.val == 2
    assert deserialized1.left.val == 1
    assert deserialized1.right.val == 3

    # Test Case 2: Skewed Tree
    # 1 -> 2 -> 3
    root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    serialized2 = codec.serialize(root2)
    deserialized2 = codec.deserialize(serialized2)
    assert deserialized2.val == 1
    assert deserialized2.right.val == 2
    assert deserialized2.right.right.val == 3

    # Test Case 3: Empty Tree
    assert codec.deserialize(codec.serialize(None)) is None
