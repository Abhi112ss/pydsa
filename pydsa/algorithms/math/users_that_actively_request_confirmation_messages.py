METADATA = {
    "id": 1939,
    "name": "Users That Actively Request Confirmation Messages",
    "slug": "users-that-actively-request-confirmation-messages",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "aggregation", "grouping"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find users with a confirmation rate of at least 0.5 based on their request history.",
}

from typing import List, Dict, Any


def solve(requests: List[Dict[str, Any]], users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Calculates the confirmation rate for each user and filters those with rate >= 0.5.

    Args:
        requests: A list of dictionaries representing the 'Signups' table.
                  Each dict contains 'user_id' and 'time_stamp'.
        users: A list of dictionaries representing the 'Confirmations' table.
               Each dict contains 'user_id' and 'action' ('confirmed' or 'timeout').

    Returns:
        A list of dictionaries containing 'user_id' and 'confirmation_rate' 
        for users with a rate >= 0.5.

    Examples:
        >>> requests = [{'user_id': 1, 'time_stamp': 1}, {'user_id': 1, 'time_stamp': 2}]
        >>> users = [{'user_id': 1, 'action': 'confirmed'}, {'user_id': 1, 'action': 'timeout'}]
        >>> solve(requests, users)
        [{'user_id': 1, 'confirmation_rate': 0.5}]
    """
    # Map to store total requests and confirmed counts per user
    # user_id -> [total_count, confirmed_count]
    stats: Dict[int, List[int]] = {}

    # Initialize stats for all users to handle users with no requests (rate 0.0)
    # Note: In the actual LeetCode problem, 'users' is the primary table 
    # and 'requests' is the secondary table.
    for user in users:
        uid = user['user_id']
        stats[uid] = [0, 0]

    # Aggregate confirmation data from the requests table
    for req in requests:
        uid = req['user_id']
        # If user exists in the users table, update their stats
        if uid in stats:
            stats[uid][0] += 1
            if req.get('action') == 'confirmed':
                stats[uid][1] += 1
        else:
            # This case handles if a request exists for a user not in the users table
            # though per schema, users should be the source of truth.
            stats[uid] = [1, 1 if req.get('action') == 'confirmed' else 0]

    result: List[Dict[str, Any]] = []

    # Calculate rates and filter based on the 0.5 threshold
    for uid, counts in stats.items():
        total_requests = counts[0]
        confirmed_requests = counts[1]

        if total_requests == 0:
            rate = 0.0
        else:
            rate = round(confirmed_requests / total_requests, 2)

        if rate >= 0.5:
            result.append({
                "user_id": uid,
                "confirmation_rate": rate
            })

    # Sort by user_id as per standard SQL output expectations if necessary
    return sorted(result, key=lambda x: x['user_id'])
