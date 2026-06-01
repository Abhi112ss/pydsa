METADATA = {
    "id": 3384,
    "name": "Team Dominance by Pass Success",
    "slug": "team-dominance-by-pass-success",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine if a single team's pass success rate is significantly higher than the average of all other teams.",
}

def solve(success_rates: list[float], threshold: float) -> bool:
    """
    Determines if there exists a team whose pass success rate is greater than 
    the average pass success rate of all other teams by at least the given threshold.

    Args:
        success_rates: A list of floats representing the pass success rate of each team.
        threshold: A float representing the minimum required difference between 
            the top team's rate and the average of the others.

    Returns:
        True if such a team exists, False otherwise.

    Examples:
        >>> solve([0.9, 0.5, 0.4, 0.6], 0.2)
        True
        >>> solve([0.5, 0.5, 0.5], 0.1)
        False
    """
    n = len(success_rates)
    if n <= 1:
        return False

    # To maximize the difference (Team_i - Average_of_others), 
    # we should pick the team with the highest success rate.
    # The average of others is minimized when the sum of others is minimized.
    # However, the problem asks if *any* team satisfies the condition.
    # The best candidate is always the team with the maximum success rate.
    
    total_sum = sum(success_rates)
    max_rate = max(success_rates)
    
    # Calculate the sum of all other teams
    sum_of_others = total_sum - max_rate
    
    # Calculate the average of the other n-1 teams
    average_of_others = sum_of_others / (n - 1)
    
    # Check if the difference meets the threshold
    return (max_rate - average_of_others) >= threshold
