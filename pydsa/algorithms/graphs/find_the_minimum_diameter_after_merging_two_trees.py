METADATA = {
    "id": 3203,
    "name": "Find the Minimum Diameter After Merging Two Trees",
    "slug": "find-the-minimum-diameter-after-merging-two-trees",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "bfs", "tree", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum diameter possible after connecting two trees by adding one edge.",
}

from collections import deque

def solve(n1: int, edges1: list[list[int]], n2: int, edges2: list[list[int]]) -> int:
    """
    Calculates the minimum diameter possible after merging two trees.
    
    The strategy is to find the radius of each tree. The radius is the minimum 
    possible distance from a 'center' node to the farthest node in that tree.
    When connecting two trees, the best way to minimize the new diameter is 
    to connect their centers. The new diameter will be the maximum of:
    1. The diameter of the first tree.
    2. The diameter of the second tree.
    3. The sum of the radii of both trees + 1 (the new edge).

    Args:
        n1: Number of nodes in the first tree.
        edges1: Adjacency list representation of the first tree.
        n2: Number of nodes in the second tree.
        edges2: Adjacency list representation of the second tree.

    Returns:
        The minimum diameter after merging.

    Examples:
        >>> solve(3, [[0,1],[1,2]], 3, [[0,1],[1,2]])
        3
        >>> solve(2, [[0,1]], 2, [[0,1]])
        3
    """

    def get_tree_metrics(n: int, edges: list[list[int]]) -> tuple[int, int]:
        """
        Computes the diameter and the radius of a tree.
        
        Args:
            n: Number of nodes.
            edges: List of edges.
            
        Returns:
            A tuple containing (diameter, radius).
        """
        if n == 1:
            return 0, 0
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(start_node: int) -> tuple[int, int]:
            """Returns (farthest_node, distance)."""
            distances = [-1] * n
            distances[start_node] = 0
            queue = deque([start_node])
            farthest_node = start_node
            max_dist = 0
            
            while queue:
                curr = queue.popleft()
                if distances[curr] > max_dist:
                    max_dist = distances[curr]
                    farthest_node = curr
                
                for neighbor in adj[curr]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = distances[curr] + 1
                        queue.append(neighbor)
            return farthest_node, max_dist

        # 1. Find diameter using two BFS approach
        # First BFS to find one end of the diameter
        node_a, _ = bfs(0)
        # Second BFS from node_a to find the other end and the diameter length
        node_b, diameter = bfs(node_a)

        # 2. Find radius using the property that radius = ceil(diameter / 2)
        # In a tree, the center(s) lie on the diameter path.
        # The minimum distance from a center to any leaf is ceil(diameter / 2).
        radius = (diameter + 1) // 2
        
        return diameter, radius

    diam1, rad1 = get_tree_metrics(n1, edges1)
    diam2, rad2 = get_tree_metrics(n2, edges2)

    # The new diameter is the max of the two original diameters 
    # or the path created by connecting the two centers.
    return max(diam1, diam2, rad1 + rad2 + 1)
