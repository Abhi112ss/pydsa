METADATA = {
    "id": 2228,
    "name": "Users With Two Purchases Within Seven Days",
    "slug": "users-with-two-purchases-within-seven-days",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sliding_window", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find users who made at least two purchases within a seven-day window.",
}

def solve(transactions: list[list[int]]) -> list[int]:
    """
    Identifies users who made at least two purchases within any seven-day window.

    Args:
        transactions: A list of transactions where each transaction is [user_id, purchase_date].

    Returns:
        A list of user IDs who meet the criteria, sorted in ascending order.

    Examples:
        >>> solve([[1, 10], [2, 11], [1, 15], [2, 20]])
        [1]
        >>> solve([[1, 10], [2, 11], [1, 15], [2, 16]])
        [1, 2]
    """
    # Map user_id to a list of their purchase dates
    user_purchase_history: dict[int, list[int]] = {}
    
    for user_id, purchase_date in transactions:
        if user_id not in user_purchase_history:
            user_purchase_history[user_id] = []
        user_purchase_history[user_id].append(purchase_date)
    
    result_users: list[int] = []
    
    for user_id, dates in user_purchase_history.items():
        # Sort dates to allow checking consecutive purchases
        dates.sort()
        
        # Check if any two consecutive purchases are within 7 days
        # A window of 7 days means: date[i+1] - date[i] < 7
        is_eligible = False
        for i in range(len(dates) - 1):
            if dates[i + 1] - dates[i] < 7:
                is_eligible = True
                break
        
        if is_eligible:
            result_users.append(user_id)
            
    # Return sorted list of user IDs as per problem requirements
    return sorted(result_users)
