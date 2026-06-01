METADATA = {
    "id": 545,
    "name": "Boundary of Binary Tree",
    "slug": "boundary-of-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree_traversal"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Return the boundary nodes of a binary tree in anti-clockwise order.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode | None) -> list[int]:
    """
    Finds the boundary nodes of a binary tree in anti-clockwise order.
    
    The boundary is defined as:
    1. The root node.
    2. The left boundary (excluding leaves).
    3. All leaf nodes (from left to right).
    4. The right boundary (excluding leaves, in reverse order).

    Args:
        root: The root of the binary tree.

    Returns:
        A list of integers representing the boundary nodes in anti-clockwise order.

    Examples:
        >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        >>> solve(root)
        [1, 2, 4, 5, 3]
    """
    if not root:
        return []

    def is_leaf(node: TreeNode) -> bool:
        return not node.left and not node.right

    boundary = []

    # 1. Add the root (if it's not a leaf, leaves are handled separately)
    if not is_leaf(root):
        boundary.append(root.val)
    else:
        return [root.val]

    # 2. Traverse Left Boundary (top-down, excluding leaves)
    curr = root.left
    while curr:
        if not is_leaf(curr):
            boundary.append(curr.val)
        # Prioritize left child, otherwise go right
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

    # 3. Traverse all Leaves (left-to-right using DFS)
    def add_leaves(node: TreeNode):
        if not node:
            return
        if is_leaf(node):
            boundary.append(node.val)
            return
        add_leaves(node.left)
        add_leaves(node.right)

    add_leaves(root)

    # 4. Traverse Right Boundary (bottom-up, excluding leaves and root)
    right_boundary = []
    curr = root.right
    while curr:
        if not is_leaf(curr):
            right_boundary.append(curr.val)
        # Prioritize right child, otherwise go left
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    
    # Add right boundary in reverse order to maintain anti-clockwise flow
    boundary.extend(reversed(right_boundary))

    return boundary