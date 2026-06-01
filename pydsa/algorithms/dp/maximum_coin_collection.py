METADATA = {
    "id": 3466,
    "name": "Maximum Coin Collection",
    "slug": "maximum-coin-collection",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of coins that can be collected by traversing a path with specific movement constraints.",
}

def solve(coins: list[int], moves: list[list[int]]) -> int:
    """
    Calculates the maximum number of coins that can be collected given a set of 
    available moves between indices.

    Args:
        coins: A list of integers where coins[i] is the number of coins at index i.
        moves: A list of pairs [u, v] representing a directed move from index u to index v.

    Returns:
        The maximum number of coins collected starting from any index.

    Examples:
        >>> solve([1, 2, 3], [[0, 1], [1, 2]])
        6
        >>> solve([10, 1, 1], [[0, 1], [0, 2]])
        10
    """
    n = len(coins)
    if n == 0:
        return 0

    # Build adjacency list for the directed graph
    # Since we want to find the max path, and the problem implies a DAG structure 
    # for standard DP collection problems, we process nodes.
    # If cycles exist, the problem would typically specify a limit or be a different type.
    # Assuming standard DAG-based DP for "collection" problems.
    adj = [[] for _ in range(n)]
    in_degree = [0] * n
    for u, v in moves:
        adj[u].append(v)
        in_degree[v] += 1

    # dp[i] stores the maximum coins collected ending at index i
    # However, to find the max path in a DAG, it's easier to compute 
    # max coins starting from i or ending at i.
    # Let's use dp[i] as the max coins collected starting from index i.
    dp = [-1] * n
    
    # To handle the DAG efficiently, we use memoization (Top-Down DP)
    def get_max_from(u: int) -> int:
        if dp[u] != -1:
            return dp[u]
        
        max_future_coins = 0
        for v in adj[u]:
            max_future_coins = max(max_future_coins, get_max_from(v))
        
        # The max coins from here is current coins + best path from neighbors
        dp[u] = coins[u] + max_future_coins
        return dp[u]

    # We must check every node as a potential starting point
    overall_max = 0
    for i in range(n):
        overall_max = max(overall_max, get_max_from(i))

    return overall_max
