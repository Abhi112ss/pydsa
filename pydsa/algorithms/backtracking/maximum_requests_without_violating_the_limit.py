METADATA = {
    "id": 3851,
    "name": "Maximum Requests Without Violating the Limit",
    "slug": "maximum-requests-without-violating-the-limit",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of requests that can be fulfilled without exceeding the capacity limit of any building.",
}

def solve(requests: list[list[int]], limits: list[int]) -> int:
    """
    Finds the maximum number of requests that can be fulfilled such that 
    the number of requests for each building does not exceed its limit.

    Args:
        requests: A list of lists where requests[i] = [building_a, building_b] 
                  representing a request from building_a to building_b.
        limits: A list where limits[i] is the maximum allowed requests for building i.

    Returns:
        The maximum number of requests that can be fulfilled.

    Examples:
        >>> solve([[0, 1], [1, 0], [0, 1]], [1, 1])
        2
        >>> solve([[0, 1], [1, 2], [2, 0]], [1, 1, 1])
        3
    """
    n_requests = len(requests)
    n_buildings = len(limits)
    
    # current_counts tracks how many requests are currently assigned to each building
    current_counts = [0] * n_buildings
    max_fulfilled = 0

    def backtrack(request_idx: int, current_count: int) -> None:
        nonlocal max_fulfilled
        
        # Base case: all requests have been considered
        if request_idx == n_requests:
            max_fulfilled = max(max_fulfilled, current_count)
            return

        # Pruning: if even if we take all remaining requests, we can't beat max_fulfilled
        if current_count + (n_requests - request_idx) <= max_fulfilled:
            return

        # Option 1: Try to include the current request
        src, dest = requests[request_idx]
        # Check if adding this request violates the limits for either the source or destination
        if current_counts[src] < limits[src] and current_counts[dest] < limits[dest]:
            current_counts[src] += 1
            current_counts[dest] += 1
            backtrack(request_idx + 1, current_count + 1)
            # Backtrack: undo the changes
            current_counts[src] -= 1
            current_counts[dest] -= 1

        # Option 2: Skip the current request
        backtrack(request_idx + 1, current_count)

    backtrack(0, 0)
    return max_fulfilled
