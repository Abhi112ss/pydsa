METADATA = {
    "id": 3540,
    "name": "Minimum Time to Visit All Houses",
    "slug": "minimum-time-to-visit-all-houses",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bit_manipulation", "graphs", "tsp"],
    "difficulty": "hard",
    "time_complexity": "O(2^n * n^2)",
    "space_complexity": "O(2^n * n)",
    "description": "Find the minimum time to visit all houses starting from any house and returning to the starting house, effectively solving the Traveling Salesperson Problem.",
}

def solve(houses: list[list[int]]) -> int:
    """
    Calculates the minimum time to visit all houses using the Traveling Salesperson Problem (TSP) approach.

    The problem is equivalent to finding the shortest Hamiltonian cycle in a complete graph 
    where nodes are houses and edge weights are Manhattan distances.

    Args:
        houses: A list of coordinates [x, y] representing the location of each house.

    Returns:
        The minimum Manhattan distance required to visit all houses and return to the start.

    Examples:
        >>> solve([[0,0],[1,1],[2,2]])
        6
        >>> solve([[0,0],[0,1],[1,0],[1,1]])
        4
    """
    n = len(houses)
    if n <= 1:
        return 0

    # Precompute Manhattan distances between all pairs of houses
    # dists[i][j] is the distance from house i to house j
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])
            distances[i][j] = d
            distances[j][i] = d

    # dp[mask][i] represents the minimum distance to visit the set of houses 
    # represented by the bitmask 'mask', ending at house 'i'.
    # mask: an integer where the k-th bit is 1 if house k has been visited.
    num_states = 1 << n
    inf = float('inf')
    dp = [[inf] * n for _ in range(num_states)]

    # Base case: Starting at any house 'i' (we can fix the start to house 0 
    # because a Hamiltonian cycle visits all nodes regardless of starting point)
    # However, to be general for TSP, we initialize the first house.
    # Since it's a cycle, we can assume we start at house 0.
    dp[1 << 0][0] = 0

    # Iterate through all possible subsets of visited houses
    for mask in range(1, num_states):
        for u in range(n):
            # If house 'u' is in the current subset
            if (mask >> u) & 1:
                if dp[mask][u] == inf:
                    continue
                
                # Try moving to a house 'v' that has not been visited yet
                for v in range(n):
                    if not ((mask >> v) & 1):
                        new_mask = mask | (1 << v)
                        new_dist = dp[mask][u] + distances[u][v]
                        if new_dist < dp[new_mask][v]:
                            dp[new_mask][v] = new_dist

    # To complete the cycle, we must return from the last visited house to the starting house (0)
    min_cycle_dist = inf
    full_mask = num_states - 1
    for last_house in range(1, n):
        # Add distance from the last house in the path back to house 0
        total_dist = dp[full_mask][last_house] + distances[last_house][0]
        if total_dist < min_cycle_dist:
            min_cycle_dist = total_dist

    return int(min_cycle_dist)
