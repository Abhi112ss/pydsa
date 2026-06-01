METADATA = {
    "id": 742,
    "name": "Closest Leaf in a Binary Tree",
    "slug": "closest-leaf-in-a-binary-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "bfs", "tree", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the distance to the nearest leaf node from a given node in a binary tree.",
}

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: Optional[TreeNode], target_node: TreeNode) -> int:
    """
    Finds the distance to the nearest leaf node from the target_node in a binary tree.

    The algorithm treats the binary tree as an undirected graph by mapping parent-child 
    relationships. It then performs a Breadth-First Search (BFS) starting from the 
    target_node to find the closest leaf.

    Args:
        root: The root of the binary tree.
        target_node: The node from which we want to find the distance to the nearest leaf.

    Returns:
        The minimum distance (number of edges) to a leaf node.

    Examples:
        >>> root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(2, TreeNode(7), TreeNode(4)))
        >>> target = root.left # Node with value 5
        >>> solve(root, target)
        1
    """
    if not root:
        return -1

    # Step 1: Build an adjacency list to treat the tree as an undirected graph.
    # Since we need to traverse upwards to parents, we need to know the parent of each node.
    adj_list: dict[TreeNode, list[TreeNode]] = {}

    def build_graph(node: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
        if not node:
            return
        
        if node not in adj_list:
            adj_list[node] = []
        
        if parent:
            adj_list[node].append(parent)
            adj_list[parent].append(node)
        
        build_graph(node.left, node)
        build_graph(node.right, node)

    build_graph(root, None)

    # Step 2: BFS to find the nearest leaf.
    # A leaf node is defined as a node with no children in the original tree structure.
    # Note: In the undirected graph, a leaf node will have exactly 1 neighbor (its parent),
    # UNLESS the tree only has one node, in which case it has 0 neighbors.
    
    queue: deque[tuple[TreeNode, int]] = deque([(target_node, 0)])
    visited: set[TreeNode] = {target_node}

    while queue:
        current_node, distance = queue.popleft()

        # Check if current_node is a leaf in the original binary tree structure.
        if not current_node.left and not current_node.right:
            return distance

        # Traverse neighbors in the undirected graph.
        for neighbor in adj_list.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1