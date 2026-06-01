METADATA = {
    "id": 2385,
    "name": "Amount of Time for Binary Tree to Be Infected",
    "slug": "amount-of-time-for-binary-tree-to-be-infected",
    "category": "Trees",
    "aliases": [],
    "tags": ["bfs", "trees", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the time required to infect all nodes in a binary tree starting from a specific node, treating the tree as an undirected graph.",
}

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root: TreeNode, start: int) -> int:
    """
    Calculates the time taken to infect the entire binary tree starting from a given node.

    The problem is treated as finding the maximum distance from the 'start' node 
    to any other node in an undirected graph representation of the tree.

    Args:
        root: The root of the binary tree.
        start: The value of the node where the infection begins.

    Returns:
        int: The total time (number of levels in BFS) to infect all nodes.

    Examples:
        >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        >>> solve(root, 4)
        3
    """
    if not root:
        return 0

    # Step 1: Build an adjacency list to represent the tree as an undirected graph
    # Since binary trees only have parent-child links, we need to map children to parents.
    adj_list: dict[int, list[int]] = {}

    def build_graph(node: TreeNode, parent: int | None) -> None:
        if not node:
            return
        
        if node.val not in adj_list:
            adj_list[node.val] = []
        
        if parent is not None:
            adj_list[node.val].append(parent)
            adj_list[parent].append(node.val)
            
        build_graph(node.left, node.val)
        build_graph(node.right, node.val)

    build_graph(root, None)

    # Step 2: Perform Breadth-First Search (BFS) starting from the 'start' node
    # BFS naturally finds the shortest path to all nodes; the max shortest path 
    # represents the time taken to reach the furthest node.
    queue: deque[int] = deque([start])
    visited: set[int] = {start}
    time_elapsed = -1

    while queue:
        # Increment time for each level of the BFS traversal
        time_elapsed += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            current_node = queue.popleft()
            
            # Explore all neighbors (parent and children)
            for neighbor in adj_list.get(current_node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return time_elapsed