METADATA = {
    "id": 3716,
    "name": "Find Churn Risk Customers",
    "slug": "find_churn_risk_customers",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Identify customers whose time intervals between consecutive activities exceed a given threshold.",
}

from collections import defaultdict

def solve(customer_activities: list[list[int]], threshold: int) -> list[int]:
    """
    Identifies customers who are at risk of churning based on the gap between activities.
    
    A customer is considered at risk if the time interval between any two 
    consecutive activities is strictly greater than the provided threshold.

    Args:
        customer_activities: A list of lists, where each sublist contains 
            [customer_id, timestamp].
        threshold: The maximum allowed gap between consecutive activities.

    Returns:
        A sorted list of unique customer IDs who meet the churn risk criteria.

    Examples:
        >>> solve([[1, 10], [1, 20], [2, 5], [2, 30], [1, 25]], 15)
        [2]
        >>> solve([[1, 1], [1, 5], [2, 10], [2, 12]], 2)
        [1]
    """
    # Group timestamps by customer ID
    activity_map = defaultdict(list)
    for customer_id, timestamp in customer_activities:
        activity_map[customer_id].append(timestamp)

    churn_risk_customers = []

    for customer_id, timestamps in activity_map.items():
        # Sort timestamps to calculate consecutive intervals
        timestamps.sort()
        
        is_risk = False
        # Check the gap between every consecutive pair of activities
        for i in range(len(timestamps) - 1):
            if timestamps[i + 1] - timestamps[i] > threshold:
                is_risk = True
                break
        
        if is_risk:
            churn_risk_customers.append(customer_id)

    # Return sorted list of IDs as per standard competitive programming requirements
    return sorted(churn_risk_customers)
