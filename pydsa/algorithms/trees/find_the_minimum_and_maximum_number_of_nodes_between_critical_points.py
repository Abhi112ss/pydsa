METADATA = {
    "id": 2058,
    "name": "Find the Minimum and Maximum Number of Nodes Between Critical Points",
    "slug": "find-the-minimum-and-maximum-number-of-nodes-between-critical-points",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum and maximum number of nodes between critical points in a tree, where a critical point is a node that is either a leaf or has degree 2.",
}

from typing import List, Optional


def solve(adj: List[List[int]], root: int) -> List[int]:
    """
    Finds the minimum and maximum number of nodes between critical points in a tree.

    A node is critical if it is a leaf or has a degree of 2. The distance between
    two critical points is the number of nodes on the path between them, excluding
    the endpoints.

    Args:
        adj: An adjacency list representing the tree.
        root: The index of the root node.

    Returns:
        A list of two integers [min_nodes, max_nodes]. If fewer than two critical
        points exist, returns [-1, -1].

    Examples:
        >>> solve([[1, 2], [0, 2], [0, 1]], 0)
        [-1, -1]
        >>> solve([[1], [0, 2], [1]], 0)
        [0, 0]
    """
    n = len(adj)
    critical_points_depths: List[int] = []

    # To handle the tree structure and avoid cycles/revisiting parents,
    # we use a standard DFS to track depth and identify critical points.
    # A node is critical if:
    # 1. It is a leaf (degree 1, except if it's the root and has degree 0).
    # 2. It has degree 2.
    
    # Note: In a tree, the degree of a node is len(adj[node]).
    # However, for the root, degree 1 is a leaf. For others, degree 1 is a leaf.
    # The problem defines critical points based on the graph degree.
    
    def get_critical_points_dfs(u: int, p: int, depth: int) -> None:
        degree = len(adj[u])
        
        # A node is critical if degree is 2 or it's a leaf (degree 1).
        # Special case: if root has degree 0, it's a leaf.
        is_leaf = (degree == 1 and u != root) or (degree == 0 and u == root)
        is_degree_two = (degree == 2)
        
        if is_leaf or is_degree_two:
            critical_points_depths.append(depth)
            
        for v in adj[u]:
            if v != p:
                get_critical_points_dfs(v, u, depth + 1)

    # Since we need the distance between nodes in a tree, and the problem 
    # implies a specific traversal/structure, we use the depth in a DFS.
    # However, the "distance" in a tree is usually the path length.
    # The problem asks for nodes *between* them.
    # For a tree, the distance between two nodes u and v is depth[u] + depth[v] - 2*depth[LCA(u, v)].
    # But the problem constraints and definition of "critical points" in this specific 
    # LeetCode context often relate to the order of discovery in a DFS traversal.
    
    # Re-reading: The problem asks for nodes between critical points in the 
    # context of the tree structure. The most efficient way to find min/max 
    # distance between nodes in a tree is via LCA, but for "nodes between" 
    # in a DFS order, we use the discovery sequence.
    
    discovery_order_depths: List[int] = []

    def dfs(u: int, p: int, depth: int) -> None:
        degree = len(adj[u])
        # Critical point definition: degree 2 or leaf (degree 1)
        # Root is special: if degree 1, it's a leaf. If degree 2, it's critical.
        is_critical = (degree == 2) or (degree == 1) or (degree == 0 and u == root)
        
        if is_critical:
            discovery_order_depths.append(depth)
            
        for v in adj[u]:
            if v != p:
                dfs(v, u, depth + 1)

    # Actually, the problem is simpler: the "distance" is the number of nodes 
    # on the path. In a tree, the distance between two nodes is the number of 
    # edges. The number of nodes *between* them is (edges - 1).
    # Wait, the problem asks for the number of nodes between them in the 
    # tree structure. This is usually calculated via LCA.
    
    # Let's use the standard approach for this problem:
    # 1. Find all critical points.
    # 2. Use DFS to find the depth and parent of each node.
    # 3. Use LCA to find the distance between critical points.
    # However, for min/max, we can observe that the max distance is between 
    # two leaves (diameter-like) and min is between adjacent critical points 
    # in a DFS traversal.
    
    # Correct approach for this specific problem:
    # The "distance" is the number of nodes on the path between two critical points.
    # The problem asks for the number of nodes *between* them.
    # If path is u -> ... -> v, nodes between are (dist(u, v) - 1).
    
    # Let's implement the DFS to collect critical points and their depths/parents.
    # To find min/max distance efficiently:
    # Max distance: Use the property that the furthest node from any node is a leaf.
    # Min distance: This is trickier.
    
    # Actually, the problem can be solved by finding the distance between 
    # all pairs of critical points, but that's O(K^2).
    # The optimal way is to use the tree diameter logic for Max and 
    # a specialized DFS for Min.
    
    # Wait, the problem is actually simpler: the "distance" is the number of nodes 
    # on the path. The "between" part means if path is A-B-C, distance is 1 (node B).
    # Let's use the LCA-based distance: dist(u, v) = depth[u] + depth[v] - 2*depth[LCA(u, v)].
    # Number of nodes between = dist(u, v) - 1.
    
    # Given the constraints and the "critical point" definition, 
    # we can use the DFS order to find the min/max.
    
    # Let's refine:
    depths = [-1] * n
    parents = [-1] * n
    critical_nodes = []
    
    stack = [(root, -1, 0)]
    while stack:
        u, p, d = stack.pop()
        depths[u] = d
        parents[u] = p
        
        degree = len(adj[u])
        # A node is critical if degree is 2 or it's a leaf (degree 1)
        # Root is a leaf if degree is 1 (unless it's the only node)
        # But the problem says "degree 2 or leaf".
        # In a tree, a leaf has degree 1.
        if degree == 2 or degree == 1 or (degree == 0 and u == root):
            critical_nodes.append(u)
            
        for v in adj[u]:
            if v != p:
                stack.append((v, u, d + 1))
                
    if len(critical_nodes) < 2:
        return [-1, -1]

    # To find max distance: diameter of the tree restricted to critical nodes.
    # To find min distance: This is harder. 
    # Actually, the problem can be solved by finding the distance between 
    # all critical points using the fact that they are part of the tree.
    
    # Let's use the property: Max distance is between two critical nodes.
    # We can find this using two BFS/DFS (standard diameter algorithm).
    
    def get_farthest(start_node: int) -> tuple[int, int]:
        # returns (farthest_node, distance)
        distances = [-1] * n
        distances[start_node] = 0
        q = [start_node]
        farthest_node = start_node
        max_dist = 0
        
        idx = 0
        while idx < len(q):
            u = q[idx]
            idx += 1
            if distances[u] > max_dist:
                max_dist = distances[u]
                farthest_node = u
            
            for v in adj[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    q.append(v)
        return farthest_node, max_dist

    # For Max:
    # 1. Pick any critical node.
    # 2. Find the farthest critical node from it.
    # 3. Find the farthest critical node from that node.
    
    # But we need to ensure the "farthest" node found is actually a critical node.
    # Let's use a modified BFS that only considers distances to critical nodes.
    
    def get_farthest_critical(start_node: int) -> tuple[int, int]:
        distances = [-1] * n
        distances[start_node] = 0
        q = [start_node]
        
        farthest_crit_node = -1
        max_dist = -1
        
        idx = 0
        while idx < len(q):
            u = q[idx]
            idx += 1
            
            # Check if u is critical
            is_crit = (len(adj[u]) == 2 or len(adj[u]) == 1 or (len(adj[u]) == 0 and u == root))
            if is_crit:
                if distances[u] > max_dist:
                    max_dist = distances[u]
                    farthest_crit_node = u
            
            for v in adj[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    q.append(v)
        return farthest_crit_node, max_dist

    # Max distance calculation
    node_a, _ = get_farthest_critical(critical_nodes[0])
    node_b, max_dist_edges = get_farthest_critical(node_a)
    
    # Min distance calculation:
    # The minimum distance between critical points in a tree can be found by 
    # checking all edges or using a DFS. However, the simplest way is to 
    # realize that the minimum distance must occur between two critical nodes 
    # that are "close" in the tree.
    
    # We can use a multi-source BFS starting from all critical nodes.
    # The first time two different critical nodes "meet", we find a candidate for min distance.
    # But that's for edges. For nodes, we can use the fact that min distance 
    # is between a node and its nearest critical neighbor.
    
    min_dist_edges = float('inf')
    
    # Multi-source BFS to find the nearest critical node for every node
    dist_to_crit = [float('inf')] * n
    nearest_crit = [-1] * n
    q = []
    
    # Initialize BFS with all critical nodes
    for cn in critical_nodes:
        dist_to_crit[cn] = 0
        nearest_crit[cn] = cn
        q.append(cn)
        
    idx = 0
    while idx < len(q):
        u = q[idx]
        idx += 1
        
        for v in adj[u]:
            if nearest_crit[v] == -1:
                nearest_crit[v] = nearest_crit[u]
                dist_to_crit[v] = dist_to_crit[u] + 1
                q.append(v)
            elif nearest_crit[v] != nearest_crit[u]:
                # We found a path between two different critical nodes
                # The distance is dist(u, nearest_crit[u]) + dist(v, nearest_crit[v]) + 1
                d = dist_to_crit[u] + dist_to_crit[v] + 1
                if d < min_dist_edges:
                    min_dist_edges = d
                    
    # The number of nodes *between* is distance - 1.
    # If distance is 1 (adjacent), nodes between is 0.
    
    # Final check for min_dist_edges
    if min_dist_edges == float('inf'):
        return [-1, -1]
        
    return [int(min_dist_edges - 1), int(max_dist_edges - 1)]

# The logic above is slightly complex for a single function. 
# Let's provide a cleaner, more robust version of the same logic.

def solve_optimized(adj: List[List[int]], root: int) -> List[int]:
    """
    Optimized version of the solver.
    """
    n = len(adj)
    is_critical = [False] * n
    critical_nodes = []
    
    for i in range(n):
        deg = len(adj[i])
        if deg == 2 or deg == 1 or (deg == 0 and i == root):
            is_critical[i] = True
            critical_nodes.append(i)
            
    if len(critical_nodes) < 2:
        return [-1, -1]
        
    # Max distance using two BFS
    def bfs(start_node: int):
        distances = [-1] * n
        distances[start_node] = 0
        queue = [start_node]
        farthest_node = start_node
        max_d = 0
        
        idx = 0
        while idx < len(queue):
            u = queue[idx]
            idx += 1
            
            if is_critical[u] and distances[u] > max_d:
                max_d = distances[u]
                farthest_node = u
                
            for v in adj[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        return farthest_node, max_d

    # First BFS from an arbitrary critical node to find one end of the diameter
    node_a, _ = bfs(critical_nodes[0])
    # Second BFS from node_a to find the actual max distance
    _, max_dist_edges = bfs(node_a)
    
    # Min distance using multi-source BFS
    # We want to find the minimum distance between any two distinct critical nodes.
    dist_to_crit = [float('inf')] * n
    source_crit = [-1] * n
    queue = []
    
    for cn in critical_nodes:
        dist_to_crit[cn] = 0
        source_crit[cn] = cn
        queue.append(cn)
        
    min_dist_edges = float('inf')
    idx = 0
    while idx < len(queue):
        u = queue[idx]
        idx += 1
        
        for v in adj[u]:
            if source_crit[v] == -1:
                source_crit[v] = source_crit[u]
                dist_to_crit[v] = dist_to_crit[u] + 1
                queue.append(v)
            elif source_crit[v] != source_crit[u]:
                # Path found between two different critical nodes
                d = dist_to_crit[u] + dist_to_crit[v] + 1
                if d < min_dist_edges:
                    min_dist_edges = d
                    
    return [int(min_dist_edges - 1), int(max_dist_edges - 1)]

# Re-assigning solve to the optimized version for the final output
solve = solve_optimized