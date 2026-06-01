METADATA = {
    "id": 2359,
    "name": "Find Closest Node to Given Two Nodes",
    "slug": "find-closest-node-to-given-two-nodes",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "graphs", "breadth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the node with the minimum distance to either of the two given nodes in a directed graph.",
}

from collections import deque

def solve(edges: list[int], node1: int, node2: int) -> int:
    """
    Finds the node that has the minimum distance to either node1 or node2.
    If there is a tie, the node with the smallest index is returned.

    Args:
        edges: A list where edges[i] is the target of the edge from node i.
               If edges[i] is -1, there is no outgoing edge from node i.
        node1: The first target node.
        node2: The second target node.

    Returns:
        The index of the node with the minimum distance to node1 or node2.

    Examples:
        >>> solve([2, 2, 3, -1, 4, -1], 1, 3)
        2
        >>> solve([2, 2, 3, -1, 4, -1], 1, 4)
        2
    """
    n = len(edges)
    
    # To find the distance from any node TO node1/node2, 
    # we must traverse the graph in reverse.
    # Build an adjacency list of the reversed graph.
    reverse_adj = [[] for _ in range(n)]
    for source, target in enumerate(edges):
        if target != -1:
            reverse_adj[target].append(source)

    def get_distances(start_node: int) -> list[int]:
        """Performs BFS on the reversed graph to find distances to start_node."""
        distances = [-1] * n
        distances[start_node] = 0
        queue = deque([start_node])
        
        while queue:
            current = queue.popleft()
            for neighbor in reverse_adj[current]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        return distances

    # Calculate distances from all nodes to node1 and node2 using reverse BFS
    dist_to_node1 = get_distances(node1)
    dist_to_node2 = get_distances(node2)

    min_dist = float('inf')
    best_node = -1

    # Iterate through all nodes to find the one with the minimum distance
    for i in range(n):
        # Calculate the minimum distance from node i to either target node
        d1 = dist_to_node1[i]
        d2 = dist_to_node2[i]
        
        # Filter out unreachable nodes (where distance is -1)
        current_min = -1
        if d1 != -1 and d2 != -1:
            current_min = min(d1, d2)
        elif d1 != -1:
            current_min = d1
        elif d2 != -1:
            current_min = d2
            
        # Update best_node if we found a smaller distance
        # Since we iterate i from 0 to n-1, the smallest index is handled automatically
        if current_min != -1 and current_min < min_dist:
            min_dist = current_min
            best_node = i

    return best_node
