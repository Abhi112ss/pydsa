METADATA = {
    "id": 863,
    "name": "All Nodes Distance K in Binary Tree",
    "slug": "all-nodes-distance-k-in-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["bfs", "dfs", "graph_conversion", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all nodes in a binary tree that are at a given distance K from a specific target node.",
}

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solve(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    """
    Args:
        root: The root of the binary tree.
        target: The target node in the binary tree.
        k: The distance from the target node.

    Returns:
        A list of values of nodes that are at distance k from the target node.
    """
    if not root:
        return []

    parent_map = {}

    def build_parent_map(node: TreeNode, parent: TreeNode | None):
        if node:
            parent_map[node] = parent
            build_parent_map(node.left, node)
            build_parent_map(node.right, node)

    build_parent_map(root, None)

    queue = deque([(target, 0)])
    visited = {target}
    result = []

    while queue:
        current_node, current_distance = queue.popleft()

        if current_distance == k:
            result.append(current_node.val)
        elif current_distance < k:
            for neighbor in [current_node.left, current_node.right, parent_map[current_node]]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, current_distance + 1))

    return result