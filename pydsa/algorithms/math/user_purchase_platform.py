METADATA = {
    "id": 1127,
    "name": "User Purchase Platform",
    "slug": "user_purchase_platform",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "group_by"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Analyze user transactions across two platforms to determine daily platform usage and total revenue.",
}

from collections import defaultdict

def solve(transactions: list[dict]) -> dict:
    """
    Analyzes user transactions to calculate daily platform usage and total revenue.

    Args:
        transactions: A list of dictionaries, where each dictionary contains:
            - 'user_id': int
            - 'platform': str ('A' or 'B')
            - 'date': str (format 'YYYY-MM-DD')
            - 'amount': float

    Returns:
        A dictionary containing:
            - 'daily_platform_usage': dict mapping date to a list of platform usage 
              (e.g., ['A'], ['B'], or ['A', 'B']).
            - 'total_revenue': float representing the sum of all transaction amounts.

    Examples:
        >>> txs = [
        ...     {'user_id': 1, 'platform': 'A', 'date': '2023-01-01', 'amount': 10.0},
        ...     {'user_id': 1, 'platform': 'B', 'date': '2023-01-01', 'amount': 20.0},
        ...     {'user_id': 2, 'platform': 'A', 'date': '2023-01-02', 'amount': 5.0}
        ... ]
        >>> solve(txs)
        {'daily_platform_usage': {'2023-01-01': ['A', 'B'], '2023-01-02': ['A']}, 'total_revenue': 35.0}
    """
    # Map to track which platforms were used by which users on a specific date
    # Structure: { date: { user_id: set(platforms) } }
    date_user_platforms = defaultdict(lambda: defaultdict(set))
    total_revenue = 0.0

    for tx in transactions:
        date = tx['date']
        user_id = tx['user_id']
        platform = tx['platform']
        amount = tx['amount']

        # Accumulate total revenue
        total_revenue += amount
        
        # Track platform usage per user per day
        date_user_platforms[date][user_id].add(platform)

    daily_platform_usage = {}

    # Process the grouped data to determine daily platform status
    for date, users in date_user_platforms.items():
        platforms_seen_on_date = set()
        
        for user_id in users:
            # For each user, check if they used one or both platforms
            user_platforms = users[user_id]
            if len(user_platforms) > 1:
                # User used both platforms on this date
                platforms_seen_on_date.add('A')
                platforms_seen_on_date.add('B')
            else:
                # User used exactly one platform
                platforms_seen_on_date.add(list(user_platforms)[0])
        
        # Convert set to sorted list to ensure deterministic output ['A', 'B'] or ['A'] or ['B']
        daily_platform_usage[date] = sorted(list(platforms_seen_on_date))

    return {
        "daily_platform_usage": daily_platform_usage,
        "total_revenue": total_revenue
    }
