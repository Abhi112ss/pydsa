METADATA = {
    "id": 1934,
    "name": "Confirmation Rate",
    "slug": "confirmation-rate",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "join", "aggregation"],
    "difficulty": "medium",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Calculate the confirmation rate for each user by finding the ratio of 'confirmed' messages to total requests.",
}

import collections

def solve(signups: list[dict[str, int]], confirmation_requests: list[dict[str, str]]) -> list[dict[str, float]]:
    """
    Calculates the confirmation rate for each user.
    
    The confirmation rate is defined as the number of 'confirmed' messages 
    divided by the total number of confirmation requests for that user. 
    If a user has no requests, the rate is 0.00.

    Args:
        signups: A list of dictionaries where each dict contains 'user_id'.
        confirmation_requests: A list of dictionaries where each dict contains 
            'user_id' and 'action' ('confirmed' or 'timeout').

    Returns:
        A list of dictionaries containing 'user_id' and 'confirmation_rate' 
        rounded to two decimal places.

    Examples:
        >>> signups = [{"user_id": 1}, {"user_id": 2}, {"user_id": 3}]
        >>> requests = [{"user_id": 1, "action": "confirmed"}, {"user_id": 1, "action": "timeout"}, {"user_id": 2, "action": "confirmed"}]
        >>> solve(signups, requests)
        [{'user_id': 1, 'confirmation_rate': 0.5}, {'user_id': 2, 'confirmation_rate': 1.0}, {'user_id': 3, 'confirmation_rate': 0.0}]
    """
    # Map to store total requests and confirmed counts per user
    # user_id -> [total_count, confirmed_count]
    user_stats = collections.defaultdict(lambda: [0, 0])

    # Aggregate request data: O(M) where M is number of requests
    for request in confirmation_requests:
        user_id = request["user_id"]
        action = request["action"]
        
        user_stats[user_id][0] += 1  # Increment total requests
        if action == "confirmed":
            user_stats[user_id][1] += 1  # Increment confirmed count

    results = []

    # Perform a "LEFT JOIN" logic: Iterate through all signups to ensure every user is included
    # O(N) where N is number of signups
    for signup in signups:
        user_id = signup["user_id"]
        total_requests, confirmed_requests = user_stats.get(user_id, [0, 0])

        # Calculate ratio; handle division by zero for users with no requests
        if total_requests == 0:
            rate = 0.0
        else:
            rate = round(confirmed_requests / total_requests, 2)

        results.append({
            "user_id": user_id,
            "confirmation_rate": rate
        })

    return results
