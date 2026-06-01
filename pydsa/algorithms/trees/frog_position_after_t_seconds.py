METADATA = {
    "id": 1377,
    "name": "Frog Position After T Seconds",
    "slug": "frog-position-after-t-seconds",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(h)",
    "description": "Determine the frog's position in a binary tree after T seconds, considering jump constraints.",
}

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def solve(edges: list[list[int]], t: int) -> int:
    """
    Finds the frog's position in a binary tree after T seconds.

    The frog starts at the root (node 0). In each second, it can jump to a child.
    If a node has no children, the frog stays at the current node.
    If a node has children, the frog must jump to a child.
    If the frog reaches a leaf node before T seconds, it stays there.

    Args:
        edges: A list of edges where edges[i] = [u, v] represents a connection.
        t: The total time in seconds.

    Returns:
        The integer value of the node where the frog is located after T seconds.

    Examples:
        >>> solve([[0, 1], [0, 2], [1, 3], [1, 4]], 3)
        3
        >>> solve([[0, 1], [0, 2], [1, 3], [1, 4]], 2)
        3
        >>> solve([[0, 1], [0, 2], [1, 3], [1, 4]], 1)
        1
    """
    if t == 0:
        return 0

    # Build adjacency list to represent the tree
    # Since it's a tree, we treat it as a directed graph from parent to child
    # to avoid jumping back to the parent.
    adj: dict[int, list[int]] = {}
    for u, v in edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)

    # Convert undirected graph to a directed tree structure (parent -> children)
    # to simplify DFS traversal.
    children: dict[int, list[int]] = {}
    visited = {0}
    stack = [0]
    while stack:
        curr = stack.pop()
        children[curr] = []
        if curr in adj:
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    children[curr].append(neighbor)
                    stack.append(neighbor)

    # Result variable to store the best node found
    # We want the deepest node reached within time T.
    # If multiple nodes are at the same depth, the DFS order handles it.
    final_position = [0]

    def dfs(node: int, current_time: int) -> None:
        # Update the final position if this node is reached within time
        final_position[0] = node

        # If we have reached the time limit, we cannot jump further
        if current_time == t:
            return

        # If the current node is a leaf, the frog stays here
        if not children.get(node):
            return

        # Otherwise, the frog must jump to a child
        for child in children[node]:
            dfs(child, current_time + 1)
            # If a child already found a valid position at depth T or 
            # if the child is a leaf and we have time left, we stop searching.
            # However, the standard DFS will naturally find the deepest node.
            # To optimize, we check if the child's branch reached the time limit.
            # But for simplicity in a tree, we just need to find the deepest node.
            # We use a trick: if we found a node at depth T, we can stop.
            # But since we need to return the node, we'll check the depth.
            pass

    # Re-implementing DFS to track depth to ensure we find the deepest node
    # within the time constraint.
    best_node = 0
    max_depth = 0

    def find_deepest(node: int, depth: int) -> None:
        nonlocal best_node, max_depth
        
        # Update best node if this is deeper than what we've found
        # or if it's the same depth but we are traversing.
        # Actually, any node reached at depth <= t is a candidate.
        # The rule is: if it's a leaf, it stays. If not, it must jump.
        if depth > max_depth:
            max_depth = depth
            best_node = node

        if depth < t:
            # If not at time limit, try to jump to children
            node_children = children.get(node, [])
            if not node_children:
                # It's a leaf, frog stays here. max_depth is already updated.
                return
            
            for child in node_children:
                find_deepest(child, depth + 1)
                # If we found a node at depth T, we can't go deeper, 
                # but we might find another node at depth T. 
                # However, the problem implies we follow one path.
                # The DFS will explore all paths. We want the one that goes deepest.
                if max_depth == t:
                    return

    find_deepest(0, 0)
    return best_node
