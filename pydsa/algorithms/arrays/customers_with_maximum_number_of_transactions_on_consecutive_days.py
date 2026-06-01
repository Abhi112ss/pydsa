METADATA = {
    "id": 2752,
    "name": "Customers with Maximum Number of Transactions on Consecutive Days",
    "slug": "customers-with-maximum-number-of-transactions-on-consecutive-days",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "sliding_window"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find customers who have the maximum number of transactions on consecutive days.",
}

def solve(transactions: list[list[int]]) -> list[list[int]]:
    """
    Finds customers with the maximum number of transactions on consecutive days.

    Args:
        transactions: A list of lists where each inner list contains [customer_id, day].

    Returns:
        A list of lists where each inner list contains [customer_id, max_consecutive_transactions].
        The result is sorted by customer_id in ascending order.

    Examples:
        >>> solve([[1,1],[1,2],[1,3],[2,1],[2,2]])
        [[1, 3], [2, 2]]
        >>> solve([[1,1],[2,2],[1,3]])
        []
    """
    # Map to store: customer_id -> {day: transaction_count}
    customer_daily_counts: dict[int, dict[int, int]] = {}
    
    for customer_id, day in transactions:
        if customer_id not in customer_daily_counts:
            customer_daily_counts[customer_id] = {}
        
        customer_daily_counts[customer_id][day] = customer_daily_counts[customer_id].get(day, 0) + 1

    max_consecutive = 0
    results: list[list[int]] = []

    # Sort customer IDs to ensure the final output is ordered
    sorted_customers = sorted(customer_daily_counts.keys())

    for customer_id in sorted_customers:
        # Get days and counts for this customer, sorted by day
        day_counts = customer_daily_counts[customer_id]
        sorted_days = sorted(day_counts.keys())
        
        current_max_for_customer = 0
        
        # We need to check consecutive days. 
        # Since days might not be perfectly sequential (e.g., day 1, day 3),
        # we iterate through the sorted days and check if day[i] == day[i-1] + 1.
        # However, the problem implies we look at consecutive days where transactions occurred.
        # Actually, the problem asks for transactions on consecutive days. 
        # If a customer has transactions on day 1 and day 2, they are consecutive.
        
        # We use a sliding window or a simple loop to find the max sum of counts 
        # for a sequence of days where each day is exactly 1 greater than the previous.
        
        # To handle the "consecutive" requirement efficiently:
        # We can use a dictionary to track the current running sum of consecutive days.
        # dp[day] = count[day] + dp[day-1] if day-1 exists else count[day]
        dp: dict[int, int] = {}
        for day in sorted_days:
            count = day_counts[day]
            if day - 1 in dp:
                dp[day] = count + dp[day - 1]
            else:
                dp[day] = count
            
            if dp[day] > current_max_for_customer:
                current_max_for_customer = dp[day]

        # Update global maximum and collect results
        if current_max_for_customer > max_consecutive:
            max_consecutive = current_max_for_customer
            results = [[customer_id, current_max_for_customer]]
        elif current_max_for_customer == max_consecutive and max_consecutive > 0:
            results.append([customer_id, current_max_for_customer])

    return results
