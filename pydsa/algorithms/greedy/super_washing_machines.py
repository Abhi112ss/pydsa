METADATA = {
    "id": 517,
    "name": "Super Washing Machines",
    "slug": "super-washing-machines",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "prefix_sum", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of minutes to distribute laundry equally among all washing machines.",
}

def solve(machines: list[int]) -> int:
    """
    Calculates the minimum number of minutes required to distribute laundry equally.

    The problem can be modeled by looking at two constraints at each machine:
    1. The net flow of laundry that must pass through a specific point (prefix sum).
       If a prefix of machines has a total surplus or deficit, that amount must 
       eventually cross the boundary.
    2. The bottleneck of a single machine. A machine can only give away one 
       laundry per minute. If a machine has a large surplus, it must export 
       them one by one.

    Args:
        machines: A list of integers representing the number of clothes in each machine.

    Returns:
        The minimum number of minutes required.

    Examples:
        >>> solve([1, 0, 5])
        5
        >>> solve([0, 3, 0])
        2
    """
    total_laundry = sum(machines)
    n = len(machines)
    target = total_laundry // n
    
    max_minutes = 0
    current_imbalance = 0
    
    for laundry_count in machines:
        # Calculate how much this machine deviates from the target
        # A positive diff means it needs to give away clothes
        # A negative diff means it needs to receive clothes
        diff = laundry_count - target
        
        # current_imbalance tracks the cumulative net flow required 
        # to balance the machines seen so far.
        current_imbalance += diff
        
        # The answer is the maximum of:
        # 1. The absolute value of the cumulative imbalance (net flow through a point).
        # 2. The specific surplus of a single machine (it can only export 1 per minute).
        # Note: We use diff for the second case because a machine needing clothes 
        # (negative diff) doesn't create a bottleneck in the same way a surplus does.
        max_minutes = max(max_minutes, abs(current_imbalance), diff)
        
    return max_minutes
