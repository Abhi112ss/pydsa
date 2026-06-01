METADATA = {
    "id": 2247,
    "name": "Maximum Cost of Trip With K Highways",
    "slug": "maximum-cost-of-trip-with-k-highways",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "sliding_window", "monotonic_queue"],
    "difficulty": "hard",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Find the maximum cost of a trip from city 0 to city n-1 using at most k highways.",
}

def solve(n: int, k: int, highways: list[list[int]]) -> int:
    """
    Calculates the maximum cost of a trip from city 0 to city n-1 using at most k highways.

    Args:
        n: The number of cities.
        k: The maximum number of highways allowed.
        highways: A list of highways where highways[i] = [from, to, cost].

    Returns:
        The maximum cost of the trip, or -1 if it is impossible to reach city n-1.

    Examples:
        >>> solve(4, 2, [[0, 1, 10], [1, 2, 20], [2, 3, 30], [0, 2, 50]])
        60
        >>> solve(4, 1, [[0, 1, 10], [1, 2, 20], [2, 3, 30], [0, 2, 50]])
        50
    """
    # adj[u] stores list of (v, cost) representing a highway from u to v
    adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
    for u, v, cost in highways:
        adj[u].append((v, cost))

    # dp[i][j] is the maximum cost to reach city i using exactly j highways
    # We use -1 to represent unreachable states
    dp: list[list[int]] = [[-1] * (k + 1) for _ in range(n)]
    
    # Base case: starting at city 0 with 0 highways used has 0 cost
    dp[0][0] = 0

    # Iterate through the number of highways used (j)
    # We iterate j first because the state for j highways depends on j-1 highways
    for j in range(1, k + 1):
        # To optimize, we can iterate through all possible starting cities 'u'
        # and all highways originating from 'u'
        for u in range(n):
            # If city 'u' was reachable with j-1 highways
            if dp[u][j - 1] != -1:
                current_cost = dp[u][j - 1]
                for v, cost in adj[u]:
                    # Update the maximum cost to reach city 'v' using 'j' highways
                    new_cost = current_cost + cost
                    if new_cost > dp[v][j]:
                        dp[v][j] = new_cost

    # The answer is the maximum cost to reach city n-1 using any number of highways from 1 to k
    max_total_cost = -1
    for j in range(1, k + 1):
        if dp[n - 1][j] > max_total_cost:
            max_total_cost = dp[n - 1][j]

    return max_total_cost
