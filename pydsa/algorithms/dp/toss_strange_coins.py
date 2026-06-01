METADATA = {
    "id": 1230,
    "name": "Toss Strange Coins",
    "slug": "toss_strange_coins",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "probability"],
    "difficulty": "medium",
    "time_complexity": "O(n * target)",
    "space_complexity": "O(target)",
    "description": "Calculate the probability of getting exactly target heads given a list of probabilities for each coin landing heads.",
}

def solve(probabilities: list[float], target: int) -> float:
    """
    Calculates the probability of getting exactly 'target' heads from a sequence of coins.

    Args:
        probabilities: A list of floats where probabilities[i] is the probability 
                       that the i-th coin lands heads.
        target: The exact number of heads required.

    Returns:
        The probability of getting exactly 'target' heads.

    Examples:
        >>> solve([0.5, 0.5], 1)
        0.5
        >>> solve([0.1, 0.9], 1)
        0.82
    """
    n = len(probabilities)
    
    # If target is impossible (more heads requested than coins available)
    if target > n or target < 0:
        return 0.0

    # dp[j] represents the probability of getting exactly j heads.
    # We use a 1D array to optimize space from O(n * target) to O(target).
    dp = [0.0] * (target + 1)
    dp[0] = 1.0  # Base case: 0 heads with 0 coins has probability 1.0

    for prob_heads in probabilities:
        prob_tails = 1.0 - prob_heads
        
        # Iterate backwards to ensure we use the results from the previous coin iteration
        # and don't overwrite values needed for the current coin's calculation.
        for j in range(target, -1, -1):
            # Probability of j heads with current coin:
            # (Prob of j-1 heads previously * current coin is heads) + 
            # (Prob of j heads previously * current coin is tails)
            
            current_heads_prob = 0.0
            
            # Case 1: Current coin is tails (we already had j heads)
            current_heads_prob += dp[j] * prob_tails
            
            # Case 2: Current coin is heads (we had j-1 heads)
            if j > 0:
                current_heads_prob += dp[j - 1] * prob_heads
                
            dp[j] = current_heads_prob

    return dp[target]
