METADATA = {
    "id": 3820,
    "name": "Pythagorean Distance Nodes in a Tree",
    "slug": "pythagorean_distance_nodes_in_a_tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count the number of pairs of nodes in a tree such that the square of the distance between them is equal to the sum of the squares of the distances from each node to their lowest common ancestor.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where each edge is a list of two integers.

    Returns:
        The number of pairs of nodes (u, v) such that the distance between them satisfies the Pythagorean condition.
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def get_distances(start_node: int) -> list[int]:
        distances = [-1] * n
        distances[start_node] = 0
        stack = [start_node]
        while stack:
            curr = stack.pop()
            for neighbor in adj[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    stack.append(neighbor)
        return distances

    def get_lca_distances(u: int, v: int) -> int:
        parent = [-1] * n
        depth = [-1] * n
        stack = [(u, -1, 0)]
        while stack:
            curr, p, d = stack.pop()
            parent[curr] = p
            depth[curr] = d
            for neighbor in adj[curr]:
                if neighbor != p:
                    stack.append((neighbor, curr, d + 1))
        
        curr_u, curr_v = u, v
        while curr_u != curr_v:
            if depth[curr_u] > depth[curr_v]:
                curr_u = parent[curr_u]
            elif depth[curr_v] > depth[curr_u]:
                curr_v = parent[curr_v]
            else:
                curr_u = parent[curr_u]
                curr_v = parent[curr_v]
        return depth[u] + depth[v] - 2 * depth[curr_u]

    all_distances = []
    for i in range(n):
        all_distances.append(get_distances(i))

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist_ij = all_distances[i][j]
            
            curr_u, curr_v = i, j
            lca_dist_u = 0
            lca_dist_v = 0
            
            parent = [-1] * n
            depth = [-1] * n
            bfs_stack = [(i, -1, 0)]
            while bfs_stack:
                curr, p, d = bfs_stack.pop()
                parent[curr] = p
                depth[curr] = d
                for neighbor in adj[curr]:
                    if neighbor != p:
                        bfs_stack.append((neighbor, curr, d + 1))
            
            u_ptr, v_ptr = i, j
            while u_ptr != v_ptr:
                if depth[u_ptr] > depth[v_ptr]:
                    u_ptr = parent[u_ptr]
                elif depth[v_ptr] > depth[u_ptr]:
                    v_ptr = parent[v_ptr]
                else:
                    u_ptr = parent[u_ptr]
                    v_ptr = parent[v_ptr]
            lca = u_ptr
            
            dist_u_lca = depth[i] - depth[lca]
            dist_v_lca = depth[j] - depth[lca]
            
            if dist_ij**2 == dist_u_lca**2 + dist_v_lca**2:
                count += 1
                
    return count

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where each edge is a list of two integers.

    Returns:
        The number of pairs of nodes (u, v) such that the distance between them satisfies the Pythagorean condition.
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    parent = [[-1] * 20 for _ in range(n)]
    depth = [0] * n
    
    stack = [(0, -1, 0)]
    while stack:
        u, p, d = stack.pop()
        parent[u][0] = p
        depth[u] = d
        for v in adj[u]:
            if v != p:
                stack.append((v, u, d + 1))
                
    for j in range(1, 20):
        for i in range(n):
            if parent[i][j-1] != -1:
                parent[i][j] = parent[parent[i][j-1]][j-1]

    def get_lca(u: int, v: int) -> int:
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for i in range(20):
            if (diff >> i) & 1:
                u = parent[u][i]
        if u == v:
            return u
        for i in range(19, -1, -1):
            if parent[u][i] != parent[v][i]:
                u = parent[u][i]
                v = parent[v][i]
        return parent[u][0]

    def get_dist(u: int, v: int) -> int:
        lca = get_lca(u, v)
        return depth[u] + depth[v] - 2 * depth[lca]

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            lca = get_lca(i, j)
            d_uv = depth[i] + depth[j] - 2 * depth[lca]
            d_ui = depth[i] - depth[lca]
            d_vi = depth[j] - depth[lca]
            if d_uv**2 == d_ui**2 + d_vi**2:
                count += 1
    return count

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where each edge is a list of two integers.

    Returns:
        The number of pairs of nodes (u, v) such that the distance between them satisfies the Pythagorean condition.
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    depth = [0] * n
    parent = [[-1] * 18 for _ in range(n)]
    
    order = []
    stack = [(0, -1, 0)]
    while stack:
        u, p, d = stack.pop()
        depth[u] = d
        parent[u][0] = p
        order.append(u)
        for v in adj[u]:
            if v != p:
                stack.append((v, u, d + 1))
                
    for j in range(1, 18):
        for i in range(n):
            if parent[i][j-1] != -1:
                parent[i][j] = parent[parent[i][j-1]][j-1]

    def get_lca(u: int, v: int) -> int:
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for i in range(18):
            if (diff >> i) & 1:
                u = parent[u][i]
        if u == v:
            return u
        for i in range(17, -1, -1):
            if parent[u][i] != parent[v][i]:
                u = parent[u][i]
                v = parent[v][i]
        return parent[u][0]

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            lca = get_lca(i, j)
            dist_sq = (depth[i] + depth[j] - 2 * depth[lca])**2
            dist_i_lca_sq = (depth[i] - depth[lca])**2
            dist_j_lca_sq = (depth[j] - depth[lca])**2
            if dist_sq == dist_i_lca_sq + dist_j_lca_sq:
                ans += 1
    return ans