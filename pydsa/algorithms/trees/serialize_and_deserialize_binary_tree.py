METADATA = {
    "id": 297,
    "name": "Serialize and Deserialize Binary Tree",
    "slug": "serialize-and-deserialize-binary-tree",
    "category": "Design",
    "aliases": [],
    "tags": ["dfs", "bfs", "design", "tree"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Design an algorithm to serialize and deserialize a binary tree.",
}

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    """
    Encodes and decodes a binary tree using pre-order traversal.
    """

    def serialize(self, root: TreeNode | None) -> str:
        """
        Serializes a tree to a single string.

        Args:
            root: The root node of the binary tree.

        Returns:
            A string representation of the tree.

        Examples:
            >>> codec = Codec()
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
            >>> codec.serialize(root)
            '1,2,,#,#,3,4,#,#,5,#,#'
        """
        result = []

        def preorder_traversal(node: TreeNode | None) -> None:
            if not node:
                result.append("#")
                return
            
            # Append current node value and recurse left then right
            result.append(str(node.val))
            preorder_traversal(node.left)
            preorder_traversal(node.right)

        preorder_traversal(root)
        return ",".join(result)

    def deserialize(self, data: str) -> TreeNode | None:
        """
        Deserializes your encoded data to tree.

        Args:
            data: The serialized string.

        Returns:
            The root node of the reconstructed binary tree.

        Examples:
            >>> codec = Codec()
            >>> data = "1,2,#,#,3,4,#,#,5,#,#"
            >>> root = codec.deserialize(data)
            >>> root.val
            1
        """
        if not data:
            return None

        # Convert string to a list of values for efficient popping
        values = data.split(",")
        # Use an iterator to track our position in the list during reconstruction
        values_iter = iter(values)

        def build_tree() -> TreeNode | None:
            try:
                val = next(values_iter)
            except StopIteration:
                return None

            if val == "#":
                return None

            # Create the current node and recursively build children
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()

def solve():
    """
    Entry point for testing the implementation.
    """
    codec = Codec()
    
    # Test Case 1: Standard tree
    #      1
    #     / \
    #    2   3
    #       / \
    #      4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)

    # Verification
    def is_same(p: TreeNode | None, q: TreeNode | None) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)

    assert is_same(root, deserialized)
    print("Test Case 1 Passed")

    # Test Case 2: Empty tree
    assert codec.deserialize(codec.serialize(None)) is None
    print("Test Case 2 Passed")
