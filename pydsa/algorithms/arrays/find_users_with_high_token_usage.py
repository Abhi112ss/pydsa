METADATA = {
    "id": 3793,
    "name": "Find Users with High Token Usage",
    "slug": "find_users_with_high_token_usage",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Identify users whose total token usage exceeds a specific threshold, returning them sorted by usage descending.",
}

def solve(usage_logs: list[dict[str, int]], threshold: int) -> list[dict[str, int]]:
    """
    Aggregates token usage per user and returns users exceeding the threshold.

    Args:
        usage_logs: A list of dictionaries where each dictionary contains 
            'user_id' (int) and 'tokens' (int).
        threshold: The minimum token usage required to be included in the result.

    Returns:
        A list of dictionaries containing 'user_id' and 'total_tokens', 
        sorted by 'total_tokens' in descending order. If tokens are equal, 
        sorted by 'user_id' in ascending order.

    Examples:
        >>> logs = [{"user_id": 1, "tokens": 10}, {"user_id": 2, "tokens": 20}, {"user_id": 1, "tokens": 15}]
        >>> solve(logs, 20)
        [{'user_id': 1, 'total_tokens': 25}, {'user_id': 2, 'total_tokens': 20}]
    """
    user_totals: dict[int, int] = {}

    # Aggregate token usage per user using a hash map
    for log in usage_logs:
        user_id = log["user_id"]
        tokens = log["tokens"]
        user_totals[user_id] = user_totals.get(user_id, 0) + tokens

    # Filter users who meet or exceed the threshold
    high_usage_users: list[dict[str, int]] = []
    for user_id, total_tokens in user_totals.items():
        if total_tokens >= threshold:
            high_usage_users.append({
                "user_id": user_id,
                "total_tokens": total_tokens
            })

    # Sort by total_tokens descending, then by user_id ascending for stability
    # We use a tuple in the key: (-total_tokens, user_id)
    high_usage_users.sort(key=lambda x: (-x["total_tokens"], x["user_id"]))

    return high_usage_users
