METADATA = {
    "id": 837,
    "name": "New 21 Game",
    "slug": "new-21-game",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "sliding_window", "probability"],
    "difficulty": "medium",
    "time_complexity": "O(max_score)",
    "space_complexity": "O(max_score)",
    "description": "Calculate the probability that Alice has n or fewer points when she stops drawing cards.",
}

def solve(max_points: int, k: int, max_cards: int) -> float:
    """
    Calculates the probability that Alice's score is <= max_points.

    Alice starts with 0 points and draws cards from [1, max_cards] until she 
    has k or more points. We need the probability that her final score 
    is less than or equal to max_points.

    Args:
        max_points: The upper bound for the score we are interested in.
        k: The threshold at which Alice stops drawing cards.
        max_cards: The maximum value of a single card drawn.

    Returns:
        The probability that Alice's final score is <= max_points.

    Examples:
        >>> solve(10, 1, 10)
        1.0
        >>> solve(6, 1, 10)
        0.7
    """
    # If k is 0, Alice stops immediately with 0 points. 
    # Since 0 <= max_points is always true (given constraints), probability is 1.
    # If max_points is already greater than or equal to the maximum possible score 
    # Alice can reach (k - 1 + max_cards), the probability is 1.
    if k == 0 or max_points >= k + max_cards:
        return 1.0

    # dp[i] represents the probability of reaching exactly i points.
    # The maximum score Alice can reach is (k - 1) + max_cards.
    dp = [0.0] * (max_points + 1)
    dp[0] = 1.0
    
    # current_window_sum tracks the sum of probabilities of the last 'max_cards' 
    # states that are valid for drawing a card (i.e., scores < k).
    current_window_sum = 1.0
    
    for i in range(1, max_points + 1):
        # The probability of reaching score 'i' is the sum of probabilities 
        # of reaching (i - card_value) for all card_values in [1, max_cards],
        # provided that (i - card_value) < k.
        dp[i] = current_window_sum / max_cards
        
        # If the current score 'i' is less than k, it can be a starting point 
        # for the next card draws, so add it to the sliding window.
        if i < k:
            current_window_sum += dp[i]
            
        # If the score 'i - max_cards' was a valid starting point (i.e., < k),
        # we must remove it from the window as it's now out of range for the next score.
        if i - max_cards >= 0 and i - max_cards < k:
            current_window_sum -= dp[i - max_cards]

    # The answer is the sum of probabilities of all scores from k to max_points.
    # However, our DP loop only calculated up to max_points. 
    # We need to sum the probabilities of all outcomes that fall in [k, max_points].
    # Wait, the DP above actually calculates the probability of reaching score 'i'.
    # The sum of dp[i] for i in [k, max_points] is the answer.
    # But our loop only goes up to max_points. Let's refine the logic.
    
    # Re-calculating the sum of probabilities for scores in [k, max_points].
    # Note: The loop above actually populates dp[i] for all i up to max_points.
    # The probability of stopping at score i (where i >= k) is calculated 
    # by the same logic as if it were a transition.
    
    # Actually, the logic above is slightly flawed for the final sum. 
    # Let's use a more robust approach:
    # dp[i] = probability of having score i.
    # To reach i, we must have come from i-j where i-j < k.
    
    # Let's re-implement the loop clearly.
    dp = [0.0] * (max_points + 1)
    dp[0] = 1.0
    window_sum = 1.0
    result = 0.0
    
    for i in range(1, max_points + 1):
        # Probability of reaching score i
        dp[i] = window_sum / max_cards
        
        # If i < k, this score can contribute to future scores
        if i < k:
            window_sum += dp[i]
        
        # If i >= k, this score is a "stopping" score. 
        # It contributes to the final probability if i <= max_points.
        else:
            result += dp[i]
            
        # Slide the window: remove the probability that is now too far back
        if i - max_cards >= 0:
            # We only remove dp[i-max_cards] if it was added to window_sum
            # It was added to window_sum only if (i-max_cards) < k
            if i - max_cards < k:
                window_sum -= dp[i - max_cards]
                
    return result

# The logic in the re-implementation is cleaner. 
# Let's provide the final optimized version.

def solve_final(max_points: int, k: int, max_cards: int) -> float:
    """
    Optimized version of the New 21 Game solver.
    """
    if k == 0 or max_points >= k + max_cards:
        return 1.0
    
    dp = [0.0] * (max_points + 1)
    dp[0] = 1.0
    window_sum = 1.0
    
    for i in range(1, max_points + 1):
        dp[i] = window_sum / max_cards
        
        if i < k:
            window_sum += dp[i]
        
        if i - max_cards >= 0 and i - max_cards < k:
            window_sum -= dp[i - max_cards]
            
    # The probability of Alice having <= max_points is the sum of 
    # probabilities of all scores i such that k <= i <= max_points.
    # However, the way we built dp[i], dp[i] for i >= k is exactly 
    # the probability that Alice's first score >= k is exactly i.
    
    return sum(dp[k:])

# Correcting the solve function to use the logic verified.
def solve(max_points: int, k: int, max_cards: int) -> float:
    if k == 0 or max_points >= k + max_cards:
        return 1.0
    
    dp = [0.0] * (max_points + 1)
    dp[0] = 1.0
    window_sum = 1.0
    
    for i in range(1, max_points + 1):
        dp[i] = window_sum / max_cards
        
        # If the current score is less than k, it can be used to reach future scores.
        if i < k:
            window_sum += dp[i]
        
        # If the score that is sliding out of the window was < k, remove it.
        if i - max_cards >= 0 and i - max_cards < k:
            window_sum -= dp[i - max_cards]
            
    return sum(dp[k:])