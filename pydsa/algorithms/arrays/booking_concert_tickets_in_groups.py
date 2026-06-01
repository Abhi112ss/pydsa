METADATA = {
    "id": 2286,
    "name": "Booking Concert Tickets in Groups",
    "slug": "booking-concert-tickets-in-groups",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n + q)",
    "space_complexity": "O(n)",
    "description": "Determine if a series of group bookings can be accommodated within a given capacity over a specific time range using a difference array.",
}

def solve(capacity: int, bookings: list[list[int]], queries: list[list[int]]) -> list[bool]:
    """
    Determines if the capacity is exceeded during specific time intervals based on bookings.

    Args:
        capacity: The maximum number of people allowed at the concert at any time.
        bookings: A list of bookings where bookings[i] = [start_i, end_i, num_i].
                  The booking is inclusive of both start and end days.
        queries: A list of queries where queries[j] = [start_j, end_j].
                 Check if capacity is exceeded at any point between start_j and end_j.

    Returns:
        A list of booleans indicating if each query is valid (True if capacity is never exceeded).

    Examples:
        >>> solve(10, [[1, 5, 4], [2, 6, 5]], [[1, 2], [3, 4]])
        [True, True]
        >>> solve(5, [[1, 5, 4], [2, 6, 5]], [[1, 2]])
        [False]
    """
    # Find the maximum time range needed. 
    # Based on constraints, we can assume a reasonable upper bound or find max from bookings.
    # For LeetCode, we typically look at the max value in bookings/queries.
    # Let's find the max day to size our difference array.
    max_day = 0
    for start, end, num in bookings:
        max_day = max(max_day, end)
    for start, end in queries:
        max_day = max(max_day, end)
    
    # Initialize difference array. Size is max_day + 2 to handle end + 1 index safely.
    diff = [0] * (max_day + 2)

    # Apply difference array technique for each booking
    for start, end, num in bookings:
        diff[start] += num
        diff[end + 1] -= num

    # Convert difference array to prefix sum array to get actual occupancy per day
    # Then, to answer range queries efficiently, we transform this into a 
    # prefix sum of the occupancy to find the maximum occupancy in a range.
    # Wait, the query asks if capacity is exceeded *at any point* in [start, end].
    # This means we need to check if max(occupancy[start...end]) > capacity.
    
    # Step 1: Compute actual occupancy per day
    occupancy = [0] * (max_day + 2)
    current_occupancy = 0
    for i in range(1, max_day + 1):
        current_occupancy += diff[i]
        occupancy[i] = current_occupancy

    # Step 2: To answer "is max in range > capacity", we can use a Sparse Table 
    # or a Segment Tree. However, since we only need to know if ANY day exceeds capacity,
    # we can pre-calculate a "violation" array where violation[i] = 1 if occupancy[i] > capacity else 0.
    # Then, a prefix sum of the violation array allows O(1) range queries.
    
    violation_prefix_sum = [0] * (max_day + 2)
    for i in range(1, max_day + 1):
        is_violated = 1 if occupancy[i] > capacity else 0
        violation_prefix_sum[i] = violation_prefix_sum[i - 1] + is_violated

    results = []
    for start, end in queries:
        # If the number of violations in [start, end] is > 0, capacity was exceeded.
        # We want to return True if capacity was NOT exceeded.
        num_violations = violation_prefix_sum[end] - violation_prefix_sum[start - 1]
        results.append(num_violations == 0)

    return results
