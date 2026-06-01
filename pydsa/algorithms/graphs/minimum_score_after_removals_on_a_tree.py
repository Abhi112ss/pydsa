METADATA = {
    "id": 2322,
    "name": "Minimum Score After Removals on a Tree",
    "slug": "minimum-score-after-removals-on-a-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree", "subtree_size", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum difference between the maximum and minimum diameters of three components formed by removing two edges from a tree.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the minimum score after removing two edges from a tree.

    The score is defined as the difference between the maximum and minimum 
    diameters of the three resulting connected components.

    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where edges[i] = [u, v].

    Returns:
        The minimum possible score.

    Examples:
        >>> solve(5, [[0, 1], [1, 2], [2, 3], [1, 4]])
        1
    """
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Precompute parent, entry/exit times, and subtree nodes to handle connectivity
    # entry[u] and exit[u] allow us to check if node 'v' is in subtree of 'u' in O(1)
    parent = [-1] * n
    entry = [0] * n
    exit_time = [0] * n
    timer = 0

    def dfs_preprocess(u: int, p: int) -> None:
        nonlocal timer
        timer += 1
        entry[u] = timer
        parent[u] = p
        for v in adj[u]:
            if v != p:
                dfs_preprocess(v, u)
        exit_time[u] = timer

    dfs_preprocess(0, -1)

    def is_ancestor(u: int, v: int) -> bool:
        """Returns True if u is an ancestor of v."""
        return entry[u] <= entry[v] and exit_time[u] >= exit_time[v]

    def get_diameter(nodes: list[int], current_adj: dict[int, list[int]]) -> int:
        """Calculates the diameter of a component using two BFS/DFS passes."""
        if not nodes:
            return 0
        
        def bfs(start_node: int) -> tuple[int, int]:
            distances = {node: -1 for node in nodes}
            distances[start_node] = 0
            queue = [start_node]
            farthest_node = start_node
            max_dist = 0
            
            idx = 0
            while idx < len(queue):
                curr = queue[idx]
                idx += 1
                if distances[curr] > max_dist:
                    max_dist = distances[curr]
                    farthest_node = curr
                for neighbor in current_adj[curr]:
                    if neighbor in distances and distances[neighbor] == -1:
                        distances[neighbor] = distances[curr] + 1
                        queue.append(neighbor)
            return farthest_node, max_dist

        u, _ = bfs(nodes[0])
        v, dist = bfs(u)
        return dist

    # To optimize diameter calculation, we need to identify nodes in each component
    # after removing two edges. Instead of full BFS every time, we use the 
    # property that components are defined by subtrees.
    
    # Pre-calculate all nodes in each subtree to avoid repeated DFS
    subtree_nodes = [[] for _ in range(n)]
    # We'll use a simpler approach: for each edge (u, v) where v is child, 
    # the component is the subtree at v.
    
    # Map edges to the 'child' node in the rooted tree
    edge_to_child = []
    for u, v in edges:
        # The child is the one with the larger entry time (deeper)
        child = v if parent[v] == u else u
        edge_to_child.append(child)

    min_score = float('inf')

    # Iterate through all pairs of edges (represented by their child nodes)
    num_edges = len(edge_to_child)
    for i in range(num_edges):
        for j in range(i + 1, num_edges):
            c1 = edge_to_child[i]
            c2 = edge_to_child[j]

            # Determine the three components
            # Case 1: c2 is in c1's subtree
            # Case 2: c1 is in c2's subtree
            # Case 3: They are in disjoint subtrees
            
            comp_nodes = [[], [], []]
            
            if is_ancestor(c1, c2):
                # c1 is ancestor of c2. Components: 
                # 1. Subtree of c2
                # 2. Subtree of c1 excluding subtree of c2
                # 3. Everything else (Root component)
                comp_nodes[0] = [node for node in range(n) if is_ancestor(c2, node)]
                comp_nodes[1] = [node for node in range(n) if is_ancestor(c1, node) and not is_ancestor(c2, node)]
                comp_nodes[2] = [node for node in range(n) if not is_ancestor(c1, node)]
            elif is_ancestor(c2, c1):
                # c2 is ancestor of c1. Components:
                # 1. Subtree of c1
                # 2. Subtree of c2 excluding subtree of c1
                # 3. Everything else
                comp_nodes[0] = [node for node in range(n) if is_ancestor(c1, node)]
                comp_nodes[1] = [node for node in range(n) if is_ancestor(c2, node) and not is_ancestor(c1, node)]
                comp_nodes[2] = [node for node in range(n) if not is_ancestor(c2, node)]
            else:
                # Disjoint subtrees. Components:
                # 1. Subtree of c1
                # 2. Subtree of c2
                # 3. Everything else
                comp_nodes[0] = [node for node in range(n) if is_ancestor(c1, node)]
                comp_nodes[1] = [node for node in range(n) if is_ancestor(c2, node)]
                comp_nodes[2] = [node for node in range(n) if not is_ancestor(c1, node) and not is_ancestor(c2, node)]

            # Calculate diameters for the three components
            diameters = []
            for nodes in comp_nodes:
                if not nodes:
                    diameters.append(0)
                    continue
                
                # Build local adjacency for the component
                local_adj = {node: [] for node in nodes}
                node_set = set(nodes)
                for node in nodes:
                    for neighbor in adj[node]:
                        if neighbor in node_set:
                            local_adj[node].append(neighbor)
                
                diameters.append(get_diameter(nodes, local_adj))
            
            min_score = min(min_score, max(diameters) - min(diameters))

    return int(min_score)

# The above O(N^3) or O(N^4) approach is too slow for N=1000.
# Let's implement the optimized O(N^2) version.

def solve(n: int, edges: list[list[int]]) -> int:
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    parent = [-1] * n
    entry = [0] * n
    exit_time = [0] * n
    timer = 0

    def dfs_preprocess(u: int, p: int) -> None:
        nonlocal timer
        timer += 1
        entry[u] = timer
        parent[u] = p
        for v in adj[u]:
            if v != p:
                dfs_preprocess(v, u)
        exit_time[u] = timer

    dfs_preprocess(0, -1)

    def is_ancestor(u: int, v: int) -> bool:
        return entry[u] <= entry[v] and exit_time[u] >= exit_time[v]

    # Precompute diameter for every possible subtree
    # subtree_diameter[u] = diameter of subtree rooted at u
    # To do this efficiently, we need the max depth and diameter info
    subtree_diam = [0] * n
    
    # We need to find diameter of any component. 
    # A component is either a subtree or (TotalTree - SubtreeA - SubtreeB)
    # This is still tricky. Let's use the property that diameter is max distance.
    
    # Correct O(N^2) approach:
    # 1. Precompute all subtree diameters.
    # 2. For any two edges (u, v) where v is child of u:
    #    If v is in subtree of u (not possible here, we pick two edges):
    #    Let edge 1 be (p1, c1) and edge 2 be (p2, c2).
    #    If c1 is ancestor of c2:
    #       Comp 1: Subtree c2
    #       Comp 2: Subtree c1 \ Subtree c2
    #       Comp 3: Tree \ Subtree c1
    #    Else:
    #       Comp 1: Subtree c1
    #       Comp 2: Subtree c2
    #       Comp 3: Tree \ (Subtree c1 U Subtree c2)

    # To get diameter of "Subtree c1 \ Subtree c2" or "Tree \ Subtree c1", 
    # we can't just use precomputed subtree diameters.
    # However, N is only 1000. O(N^2) is acceptable.
    # We can precompute the diameter of every subtree in O(N^2).
    
    subtree_diam = [0] * n
    for i in range(n):
        # Find all nodes in subtree i
        nodes = [node for node in range(n) if is_ancestor(i, node)]
        if not nodes: continue
        
        # Local adj
        node_set = set(nodes)
        local_adj = {node: [] for node in nodes}
        for node in nodes:
            for neighbor in adj[node]:
                if neighbor in node_set:
                    local_adj[node].append(neighbor)
        
        # BFS for diameter
        def bfs(start_node):
            dist = {node: -1 for node in nodes}
            dist[start_node] = 0
            q = [start_node]
            farthest_node = start_node
            max_d = 0
            idx = 0
            while idx < len(q):
                curr = q[idx]
                idx += 1
                if dist[curr] > max_d:
                    max_d = dist[curr]
                    farthest_node = curr
                for neighbor in local_adj[curr]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[curr] + 1
                        q.append(neighbor)
            return farthest_node, max_d

        u_f, _ = bfs(nodes[0])
        v_f, d = bfs(u_f)
        subtree_diam[i] = d

    # For the "remaining" parts, we can use the fact that N is small.
    # But we need to be careful. Let's precompute diameter of (Tree \ Subtree i)
    # for all i.
    
    remaining_diam = [0] * n
    for i in range(n):
        # Nodes NOT in subtree i
        nodes = [node for node in range(n) if not is_ancestor(i, node)]
        if not nodes: continue
        node_set = set(nodes)
        local_adj = {node: [] for node in nodes}
        for node in nodes:
            for neighbor in adj[node]:
                if neighbor in node_set:
                    local_adj[node].append(neighbor)
        
        def bfs(start_node):
            dist = {node: -1 for node in nodes}
            dist[start_node] = 0
            q = [start_node]
            farthest_node = start_node
            max_d = 0
            idx = 0
            while idx < len(q):
                curr = q[idx]
                idx += 1
                if dist[curr] > max_d:
                    max_d = dist[curr]
                    farthest_node = curr
                for neighbor in local_adj[curr]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[curr] + 1
                        q.append(neighbor)
            return farthest_node, max_d

        u_f, _ = bfs(nodes[0])
        v_f, d = bfs(u_f)
        remaining_diam[i] = d

    # Now we need diameter of (Subtree c1 \ Subtree c2) where c1 is ancestor of c2.
    # This is the hardest part. Let's use the O(N^2) approach where we 
    # iterate all pairs of edges and for each pair, we find the 3 components 
    # and their diameters using BFS. Since N=1000, N^2 is 10^6. 
    # If we do a BFS inside, it's N^3. We need to avoid N^3.
    
    # Wait, the number of edges is N-1. Total pairs of edges is (N-1)(N-2)/2.
    # For N=1000, this is ~500,000. 
    # If we can find the diameters in O(1) or O(log N) after O(N^2) precomputation, we win.
    
    # Let's reconsider: The three components are:
    # If c1 is ancestor of c2:
    #   1. Subtree(c2) -> diameter is subtree_diam[c2]
    #   2. Tree \ Subtree(c1) -> diameter is remaining_diam[c1]
    #   3. Subtree(c1) \ Subtree(c2) -> This is the tricky one.
    # If c1 and c2 are disjoint:
    #   1. Subtree(c1) -> subtree_diam[c1]
    #   2. Subtree(c2) -> subtree_diam[c2]
    #   3. Tree \ (Subtree(c1) U Subtree(c2)) -> diameter of the rest.

    # Actually, for N=1000, we can afford a slightly more optimized O(N^2).
    # Let's precompute the distance between all pairs of nodes using BFS from each node.
    # dists[i][j] = distance between i and j.
    
    dists = [[0] * n for _ in range(n)]
    for start_node in range(n):
        d = dists[start_node]
        for i in range(n): d[i] = -1
        d[start_node] = 0
        q = [start_node]
        idx = 0
        while idx < len(q):
            u = q[idx]
            idx += 1
            for v in adj[u]:
                if d[v] == -1:
                    d[v] = d[u] + 1
                    q.append(v)

    # To find diameter of a set of nodes S:
    # diameter = max(dists[u][v] for u, v in S)
    # This is still O(|S|^2).
    
    # Let's use the property: diameter of a set of nodes S is max(dist(u, v)) 
    # where u, v are in S.
    # For a component, we can find its diameter in O(|S|) if we know its "farthest" nodes.
    # But we don't.
    
    # Let's use the O(N^2) approach by iterating over all edges and 
    # precomputing diameters of all subtrees and all "remaining" components.
    # For the "Subtree(c1) \ Subtree(c2)" part:
    # It's a component. Its diameter can be found by looking at the nodes.
    #