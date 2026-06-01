METADATA = {
    "id": 2747,
    "name": "Count Zero Request Servers",
    "slug": "count-zero-request-servers",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "prefix_sum", "difference_array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of time units where no requests are being processed using a difference array approach.",
}

def solve(requests: list[list[int]]) -> int:
    """
    Counts the number of time units where no servers are processing requests.

    Args:
        requests: A list of lists where each sub-list contains [start, end] 
                  representing the time interval of a request.

    Returns:
        The total number of time units where zero requests are active.

    Examples:
        >>> solve([[1, 3], [2, 4]])
        1
        >>> solve([[1, 2], [5, 6]])
        3
    """
    if not requests:
        return 0

    # Find the maximum time boundary to size our difference array.
    # Since we need to track intervals, we find the max end time.
    max_time = 0
    for start, end in requests:
        if end > max_time:
            max_time = end

    # Initialize a difference array. 
    # We use max_time + 2 to handle 1-based indexing and the end+1 boundary safely.
    diff = [0] * (max_time + 2)

    # Apply the difference array logic:
    # Increment at start, decrement at end + 1 to mark the interval [start, end].
    for start, end in requests:
        diff[start] += 1
        diff[end + 1] -= 1

    zero_request_count = 0
    current_active_requests = 0

    # Iterate through the timeline to compute prefix sums.
    # Each prefix sum represents the number of active requests at that specific time unit.
    for time in range(1, max_time + 1):
        current_active_requests += diff[time]
        
        # If no requests are active at this time unit, increment our counter.
        if current_active_requests == 0:
            zero_request_count += 1

    return zero_request_count
