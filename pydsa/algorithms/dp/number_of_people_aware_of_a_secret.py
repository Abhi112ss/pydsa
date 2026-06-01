METADATA = {
    "id": 2327,
    "name": "Number of People Aware of a Secret",
    "slug": "number-of-people-aware-of-a-secret",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of people who know a secret after n days given a delay before sharing and a delay before forgetting.",
}

def solve(n: int, delay: int, forget: int) -> int:
    """
    Calculates the number of people aware of a secret after n days.

    Args:
        n: The total number of days.
        delay: The number of days a person must wait before they can share the secret.
        forget: The number of days after which a person forgets the secret.

    Returns:
        The number of people who know the secret on day n, modulo 10^9 + 7.

    Examples:
        >>> solve(6, 2, 4)
        5
        >>> solve(10, 2, 4)
        11
    """
    MOD = 1_000_000_007
    
    # dp[i] stores the number of people who discovered the secret on day i.
    # We use n + 1 to accommodate 1-based indexing for days.
    dp = [0] * (n + 1)
    
    # On day 1, one person discovers the secret.
    dp[1] = 1
    
    # current_sharers tracks the number of people who are currently in the 
    # window [day - forget + 1, day - delay] and can share the secret.
    current_sharers = 0
    
    for day in range(2, n + 1):
        # People who learned the secret 'delay' days ago are now eligible to share.
        # They enter the 'sharer' pool on day: (day - delay)
        new_sharers_idx = day - delay
        if new_sharers_idx >= 1:
            current_sharers = (current_sharers + dp[new_sharers_idx]) % MOD
            
        # People who learned the secret 'forget' days ago are no longer eligible to share.
        # They leave the 'sharer' pool on day: (day - forget)
        forgetting_sharers_idx = day - forget
        if forgetting_sharers_idx >= 1:
            current_sharers = (current_sharers - dp[forgetting_sharers_idx] + MOD) % MOD
            
        # The number of new people who learn the secret today is equal to the current sharers.
        dp[day] = current_sharers
        
    # The answer is the sum of people who learned the secret from day (n - forget + 1) to day n.
    # These are the people who haven't forgotten the secret by the end of day n.
    total_aware = 0
    for day in range(max(1, n - forget + 1), n + 1):
        total_aware = (total_aware + dp[day]) % MOD
        
    return total_aware
