METADATA = {
    "id": 2093,
    "name": "Minimum Cost to Reach City With Discounts",
    "slug": "minimum-cost-to-reach-city-with-discounts",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dijkstra", "shortest-path"],
    "difficulty": "hard",
    "time_complexity": "O(k * E * log(k * N))",
    "space_complexity": "O(k * N)",
    "description": "Find the minimum cost to reach the target city using at most k discounts on edges.",
}

import heapq

def solve(n: int, edges: list[list[int]], k: int) -> int:
    """
    Finds the minimum cost to reach city n-1 from city 0 using at most k discounts.

    Args:
        n: The number of cities.
        edges: A list of edges where each edge is [u, v, cost, discount].
        k: The maximum number of discounts that can be applied.

    Returns:
        The minimum cost to reach city n-1, or -1 if unreachable.

    Examples:
        >>> solve(3, [[0,1,10,1],[1,2,10,1]], 1)
        10
        >>> solve(3, [[0,1,10,1],[1,2,10,1]], 0)
        20
    """
    # Build adjacency list: adj[u] = [(v, cost, has_discount), ...]
    adj = [[] for _ in range(n)]
    for u, v, cost, discount in edges:
        adj[u].append((v, cost, discount))
        adj[v].append((u, cost, discount))

    # min_costs[city][discounts_used] stores the minimum cost to reach 'city'
    # having used exactly 'discounts_used' discounts.
    # We use k + 1 to account for 0 to k discounts.
    min_costs = [[float('inf')] * (k + 1) for _ in range(n)]
    
    # Priority Queue stores (current_cost, current_city, discounts_used)
    # Dijkstra's algorithm explores the cheapest paths first.
    pq = [(0, 0, 0)]
    min_costs[0][0] = 0

    while pq:
        current_cost, u, used_discounts = heapq.heappop(pq)

        # If we found a path to u with used_discounts that is more expensive 
        # than what we've already recorded, skip it.
        if current_cost > min_costs[u][used_discounts]:
            continue

        # If we reached the target city, since we use Dijkstra, 
        # the first time we pop it, it's the minimum cost for that specific discount count.
        # However, we continue to find if other discount counts yield even lower costs.
        if u == n - 1:
            continue

        for v, cost, has_discount in adj[u]:
            # Option 1: Don't use a discount on this edge
            new_cost_no_discount = current_cost + cost
            if new_cost_no_discount < min_costs[v][used_discounts]:
                min_costs[v][used_discounts] = new_cost_no_discount
                heapq.heappush(pq, (new_cost_no_discount, v, used_discounts))

            # Option 2: Use a discount on this edge (if available and we have budget)
            if has_discount and used_discounts < k:
                new_cost_with_discount = current_cost
                if new_cost_with_discount < min_costs[v][used_discounts + 1]:
                    min_costs[v][used_discounts + 1] = new_cost_with_discount
                    heapq.heappush(pq, (new_cost_with_discount, v, used_discounts + 1))

    # The answer is the minimum cost to reach city n-1 across all possible discount counts [0...k]
    result = min(min_costs[n - 1])
    return int(result) if result != float('inf') else -1
