METADATA = {
    "id": 2742,
    "name": "Painting the Walls",
    "slug": "painting-the-walls",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to paint all walls given free painter time and costs for each wall.",
}

def solve(paintings: list[int], free_time: int) -> int:
    """
    Args:
        paintings: A list of integers representing the cost to paint each wall.
        free_time: An integer representing the number of walls that can be painted for free.

    Returns:
        The minimum cost to paint all walls.
    """
    n = len(paintings)
    total_walls_to_paint = n + free_time
    
    dp = [float('inf')] * (total_walls_to_paint + 1)
    dp[0] = 0
    
    for cost in paintings:
        for j in range(total_walls_to_paint, 0, -1):
            dp[j] = min(dp[j], dp[j - 1] + cost)
            
    return int(min(dp[n:]))