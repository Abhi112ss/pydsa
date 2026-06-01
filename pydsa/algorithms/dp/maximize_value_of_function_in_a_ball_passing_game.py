METADATA = {
    "id": 2836,
    "name": "Maximize Value of Function in a Ball Passing Game",
    "slug": "maximize-value-of-function-in-a-ball-passing-game",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum value of a function defined by a sequence of ball passes using dynamic programming.",
}

def solve(n: int, values: list[int], rules: list[list[int]]) -> int:
    """
    Calculates the maximum value of a function in a ball passing game.
    
    The game involves passing a ball between players according to specific rules.
    Each player has a value, and the total value is the sum of values of players
    who receive the ball, subject to constraints.

    Args:
        n: The number of players.
        values: A list of integers where values[i] is the value of player i.
        rules: A list of rules where rules[i] = [u, v] means a pass can go from u to v.

    Returns:
        The maximum possible value of the function.

    Examples:
        >>> solve(3, [1, 2, 3], [[0, 1], [1, 2], [2, 0]])
        6
    """
    # Adjacency list to represent the directed graph of possible passes
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in rules:
        adj[u].append(v)

    # dp[i] stores the maximum value achievable starting from player i
    # We use memoization to avoid redundant calculations
    memo: list[int] = [-1] * n
    # visited tracks nodes in the current recursion stack to detect cycles
    visited: list[bool] = [False] * n

    def get_max_value(current_player: int) -> int:
        # If we hit a node currently in the recursion stack, we found a cycle.
        # In this specific problem context, cycles are handled by the game rules.
        # If the problem implies a DAG or specific termination, we return 0.
        if visited[current_player]:
            return 0
        
        if memo[current_player] != -1:
            return memo[current_player]

        visited[current_player] = True
        max_from_next = 0
        
        # Explore all possible next players according to the rules
        for neighbor in adj[current_player]:
            max_from_next = max(max_from_next, get_max_value(neighbor))
        
        visited[current_player] = False
        
        # The value at this state is the current player's value plus the best from neighbors
        memo[current_player] = values[current_player] + max_from_next
        return memo[current_player]

    # Since the game can start at any player, we check all starting positions
    # Note: If the graph contains cycles and we can traverse them infinitely, 
    # the problem usually defines a constraint or asks for a simple path.
    # Assuming standard DP on DAG or limited traversal.
    
    # For general graphs with cycles, we'd need to handle the cycle value.
    # However, based on the problem type, we assume a DAG or a specific structure.
    # If cycles are allowed and add value, the answer could be infinite.
    # We implement the standard DP approach.
    
    overall_max = 0
    for i in range(n):
        # Resetting visited for each start if we want to find the longest path in a DAG
        # but memoization handles the subproblems.
        overall_max = max(overall_max, get_max_value(i))

    return overall_max
