METADATA = {
    "id": 2686,
    "name": "Immediate Food Delivery III",
    "slug": "immediate-food-delivery-iii",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O((n + q) log n)",
    "space_complexity": "O(n)",
    "description": "Find the closest delivery point for each customer query using binary search on sorted coordinates.",
}

import bisect

def solve(customer_locations: list[int], delivery_locations: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the minimum distance to the nearest delivery point for each customer query.

    Args:
        customer_locations: A list of integers representing customer positions.
        delivery_locations: A list of integers representing delivery point positions.
        queries: A list of queries where each query is [customer_index, delivery_index].
                 Note: Based on the problem description, queries are usually 
                 [customer_id, delivery_id] or similar, but the logic focuses 
                 on finding the closest delivery point for a specific customer.

    Returns:
        A list of integers representing the minimum distance for each query.

    Examples:
        >>> solve([1, 5], [2, 10], [[0, 0]])
        [1]
    """
    # Sort delivery locations to enable binary search
    sorted_deliveries = sorted(delivery_locations)
    n = len(sorted_deliveries)
    results = []

    for customer_idx, _ in queries:
        # The problem context implies we look for the closest delivery point 
        # to the customer at customer_locations[customer_idx]
        target = customer_locations[customer_idx]
        
        # Find the insertion point to maintain order
        idx = bisect.bisect_left(sorted_deliveries, target)
        
        min_dist = float('inf')
        
        # Check the delivery point at the insertion index (the smallest value >= target)
        if idx < n:
            min_dist = min(min_dist, abs(sorted_deliveries[idx] - target))
            
        # Check the delivery point before the insertion index (the largest value < target)
        if idx > 0:
            min_dist = min(min_dist, abs(sorted_deliveries[idx - 1] - target))
            
        results.append(int(min_dist))
        
    return results

# Note: The problem description provided in the prompt for #2686 
# (Immediate Food Delivery III) is a variation of finding nearest neighbors.
# Standard LeetCode 2686 is actually "Find the Missing Number", 
# but I am following the specific algorithmic instructions provided in the prompt.
