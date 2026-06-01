METADATA = {
    "id": 3497,
    "name": "Analyze Subscription Conversion",
    "slug": "analyze_subscription_conversion",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sliding_window", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the conversion rate by counting transitions from 'unsubscribed' to 'subscribed' states in a sequence of user logs.",
}

def solve(logs: list[str]) -> float:
    """
    Analyzes user logs to determine the conversion rate from unsubscribed to subscribed.

    The conversion rate is defined as the number of times a user transitions 
    from 'unsubscribed' to 'subscribed' divided by the total number of 
    possible transitions (total logs - 1).

    Args:
        logs: A list of strings where each string is either 'subscribed' or 'unsubscribed'.

    Returns:
        float: The conversion rate as a decimal. Returns 0.0 if there are fewer than 2 logs.

    Examples:
        >>> solve(["unsubscribed", "subscribed", "unsubscribed", "subscribed"])
        0.6666666666666666
        >>> solve(["subscribed", "subscribed", "unsubscribed"])
        0.0
        >>> solve(["unsubscribed", "subscribed"])
        1.0
    """
    n = len(logs)
    
    # If there are no transitions possible, conversion rate is 0
    if n < 2:
        return 0.0

    conversions = 0
    
    # Iterate through the logs and check the transition between consecutive states
    for i in range(n - 1):
        current_state = logs[i]
        next_state = logs[i + 1]
        
        # A conversion is defined as moving from 'unsubscribed' to 'subscribed'
        if current_state == "unsubscribed" and next_state == "subscribed":
            conversions += 1
            
    # The total number of transitions is the number of elements minus one
    total_transitions = n - 1
    
    return conversions / total_transitions
