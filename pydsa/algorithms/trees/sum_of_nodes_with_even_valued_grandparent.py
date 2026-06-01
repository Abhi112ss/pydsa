METADATA = {
    "id": 1315,
    "name": "Sum of Nodes with Even-Valued Grandparent",
    "slug": "sum-of-nodes-with-even-valued-grandparent",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "bfs", "binary_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Calculate the sum of all nodes in a binary tree that have an even-valued grandparent.",
}

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode) -> int:
    """
    Args:
        root: The root of the binary tree.

    Returns:
        The sum of all nodes that have an even-valued grandparent.
    """
    total_sum = 0

    def traverse(node: TreeNode, parent_val: int, grandparent_val: int) -> None:
        nonlocal total_sum
        if not node:
            return

        if grandparent_val is not None and grandparent_val % 2 == 0:
            total_sum += node.val

        traverse(node.left, node.val, parent_val)
        traverse(node.right, node.val, parent_val)

    traverse(root, None, None)
    return total_sum

def solve_iterative(root: TreeNode) -> int:
    """
    Args:
        root: The root of the binary tree.

    Returns:
        The sum of all nodes that have an even-valued grandparent.
    """
    if not root:
        return 0

    total_sum = 0
    stack = [(root, None, None)]

    while stack:
        current_node, parent_val, grandparent_val = stack.pop()

        if grandparent_val is not None and grandparent_val % 2 == 0:
            total_sum += current_node.val

        if current_node.right:
            stack.append((current_node.right, current_node.val, parent_val))
        if current_node.left:
            stack.append((current_node.left, current_node.val, parent_val))

    return total_sum

def solve(root: TreeNode) -> int:
    """
    Args:
        root: The root of the binary tree.

    Returns:
        The sum of all nodes that have an even-valued grandparent.
    """
    if not root:
        return 0

    total_sum = 0
    stack = [(root, None, None)]

    while stack:
        current_node, parent_val, grandparent_val = stack.pop()

        if grandparent_val is not None and grandparent_val % 2 == 0:
            total_sum += current_node.val

        if current_node.right:
            stack.append((current_node.right, current_node.val, parent_val))
        if current_node.left:
            stack.append((current_node.left, current_node.val, parent_val))

    return total_sum