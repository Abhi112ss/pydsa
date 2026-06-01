METADATA = {
    "id": 787,
    "name": "Cheapest Flights Within K Stops",
    "slug": "cheapest-flights-within-k-stops",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dijkstra", "dynamic_programming", "bellman-ford"],
    "difficulty": "medium",
    "time_complexity": "O(K * E)",
    "space_complexity": "O(V)",
    "description": "Find the cheapest price from a source to a destination with at most K stops using a modified Bellman-Ford approach.",
}

def solve(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    """
    Finds the cheapest price from src to dst with at most k stops.

    Args:
        n: The number of cities.
        flights: A list of flights where flights[i] = [from, to, price].
        src: The starting city.
        dst: The destination city.
        k: The maximum number of stops allowed.

    Returns:
        The cheapest price to reach dst from src within k stops, or -1 if impossible.

    Examples:
        >>> solve(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
        700
        >>> solve(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
        200
    """
    # Initialize distances with infinity, except for the source city
    # We use a Bellman-Ford variation where we iterate at most k+1 times
    # (k stops means at most k+1 edges)
    inf = float('inf')
    prices = [inf] * n
    prices[src] = 0

    for _ in range(k + 1):
        # We must use a copy of the current prices to ensure we are only 
        # using results from the previous iteration (preventing using 
        # more than one edge per iteration).
        temp_prices = list(prices)
        
        for u, v, price in flights:
            # If the starting city of the flight is reachable
            if prices[u] != inf:
                # If traveling to v via u is cheaper than the current known price for v
                if prices[u] + price < temp_prices[v]:
                    temp_prices[v] = prices[u] + price
        
        # Update the main prices array for the next iteration
        prices = temp_prices

    return int(prices[dst]) if prices[dst] != inf else -1
