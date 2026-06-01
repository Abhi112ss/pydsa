METADATA = {
    "id": 3553,
    "name": "Minimum Weighted Subgraph With the Required Paths II",
    "slug": "minimum-weighted-subgraph-with-the-required-paths-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "graphs", "bitmask"],
    "difficulty": "hard",
    "time_complexity": "O(2^k * (V + E))",
    "space_complexity": "O(2^k * V)",
    "description": "Find the minimum weight subgraph such that all specified required paths are satisfied using bitmask DP.",
}

def solve(n: int, edges: list[list[int]], paths: list[list[int]]) -> int:
    """
    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where each edge is [u, v, weight].
        paths: A list of required paths where each path is a list of nodes.

    Returns:
        The minimum weight to satisfy all required paths, or -1 if impossible.
    """
    k = len(paths)
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    path_masks = [0] * n
    for i in range(k):
        for node in paths[i]:
            path_masks[node] |= (1 << i)

    inf = float('inf')
    dp = [[inf] * (1 << k) for _ in range(n)]
    
    import heapq

    pq = []
    for i in range(n):
        mask = path_masks[i]
        if mask > 0:
            dp[i][mask] = 0
            heapq.heappush(pq, (0, i, mask))
        else:
            dp[i][0] = 0
            heapq.heappush(pq, (0, i, 0))

    while pq:
        current_weight, u, current_mask = heapq.heappop(pq)

        if current_weight > dp[u][current_mask]:
            continue

        for v, weight in adj[u]:
            new_mask = current_mask | path_masks[v]
            if dp[v][new_mask] > current_weight + weight:
                dp[v][new_mask] = current_weight + weight
                heapq.heappush(pq, (dp[v][new_mask], v, new_mask))

    ans = inf
    target_mask = (1 << k) - 1
    for i in range(n):
        ans = min(ans, dp[i][target_mask])

    return int(ans) if ans != inf else -1