METADATA = {
    "id": 3924,
    "name": "Minimum Threshold Path With Limited Heavy Edges",
    "slug": "minimum_threshold_path_with_limited_heavy_edges",
    "category": "Graph",
    "aliases": [],
    "tags": ["binary_search", "dijkstra", "graphs", "shortest_path"],
    "difficulty": "hard",
    "time_complexity": "O(E * log(max_weight) * log(V))",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum threshold value such that there exists a path from source to target using at most K edges with weight greater than the threshold.",
}

import heapq

def solve(n: int, edges: list[list[int]], source: int, target: int, k: int) -> int:
    """
    Finds the minimum threshold value such that a path exists from source to target
    using at most k edges with weight strictly greater than the threshold.

    Args:
        n: Number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v, w] representing an edge 
               between u and v with weight w.
        source: The starting node.
        target: The destination node.
        k: The maximum number of 'heavy' edges (weight > threshold) allowed.

    Returns:
        The minimum threshold value, or -1 if no such path exists.

    Examples:
        >>> solve(3, [[0, 1, 10], [1, 2, 20], [0, 2, 30]], 0, 2, 1)
        19
    """
    # Build adjacency list
    adj = [[] for _ in range(n)]
    weights = set()
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        weights.add(w)
    
    # Sorted unique weights to binary search over possible threshold values
    # We also include 0 in case all edges can be considered 'light'
    sorted_weights = sorted(list(weights))
    
    def can_reach(threshold: int) -> bool:
        """
        Checks if target is reachable from source using at most k edges 
        with weight > threshold using Dijkstra's algorithm.
        """
        # min_heavy_edges[u] stores the minimum number of heavy edges used to reach u
        min_heavy_edges = [float('inf')] * n
        min_heavy_edges[source] = 0
        
        # Priority queue stores (heavy_edges_count, current_node)
        pq = [(0, source)]
        
        while pq:
            heavy_count, u = heapq.heappop(pq)
            
            if u == target:
                return True
            
            if heavy_count > min_heavy_edges[u]:
                continue
                
            for v, weight in adj[u]:
                # An edge is heavy if its weight is strictly greater than the threshold
                is_heavy = 1 if weight > threshold else 0
                new_heavy_count = heavy_count + is_heavy
                
                if new_heavy_count <= k and new_heavy_count < min_heavy_edges[v]:
                    min_heavy_edges[v] = new_heavy_count
                    heapq.heappush(pq, (new_heavy_count, v))
                    
        return False

    # Binary search on the indices of sorted_weights
    # The threshold can be any value. If we pick a threshold from the weights,
    # we are testing if we can satisfy the condition by making all edges > threshold 'heavy'.
    # Note: The problem asks for the minimum threshold. If threshold is X, 
    # edges with weight > X are heavy.
    
    # We need to consider that the threshold could be one less than a weight.
    # Let's refine: the possible threshold values that change the 'heaviness' 
    # are the weights themselves (specifically, threshold = weight - 1).
    # However, a simpler way is to binary search over the sorted weights.
    # If threshold = sorted_weights[i], then edges with weight > sorted_weights[i] are heavy.
    # If threshold = sorted_weights[i] - 1, then edges with weight >= sorted_weights[i] are heavy.
    
    # Let's use the weights themselves as potential thresholds.
    # If we can reach with threshold W, we might be able to do it with a smaller W.
    # But wait, if threshold is W, edges > W are heavy. 
    # If we decrease W, more edges become heavy. So the property is monotonic.
    
    # Possible thresholds to check: 
    # Any weight 'w' in the graph could be a threshold. 
    # If threshold is 'w', edges > w are heavy.
    # If threshold is 'w-1', edges > w-1 (i.e., >= w) are heavy.
    # The optimal threshold will always be one of the weights or 0 or max_weight.
    
    # Let's collect all possible "boundary" thresholds.
    # A threshold 't' makes an edge 'w' heavy if w > t.
    # This is equivalent to saying 't' is in the range [w-1, w-1] or similar.
    # Actually, the threshold can be any value. The "critical" values are weights.
    # If threshold is W, edges with weight > W are heavy.
    # If we want to minimize W, we want to find the smallest W such that 
    # count(weight > W) <= k.
    
    # Let's test thresholds from the set of weights and also 0.
    # If threshold is W, edges > W are heavy.
    # If threshold is W-1, edges > W-1 (i.e. >= W) are heavy.
    
    # Let's use a more robust approach: 
    # The threshold can be any value. The number of heavy edges only changes 
    # when the threshold crosses a weight value.
    # Let's test thresholds: {w for w in weights} UNION {w-1 for w in weights} UNION {0}
    
    possible_thresholds = {0}
    for w in weights:
        possible_thresholds.add(w)
        if w > 0:
            possible_thresholds.add(w - 1)
            
    sorted_candidates = sorted(list(possible_thresholds))
    
    low = 0
    high = len(sorted_candidates) - 1
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if can_reach(sorted_candidates[mid]):
            ans = sorted_candidates[mid]
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
