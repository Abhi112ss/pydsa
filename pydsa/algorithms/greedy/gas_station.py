METADATA = {
    "id": 134,
    "name": "Gas Station",
    "slug": "gas-station",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the starting gas station index to complete a circular circuit given gas amounts and costs.",
}

def solve(gas: list[int], cost: list[int]) -> int:
    """
    Finds the starting gas station index to complete a circular circuit.

    The algorithm uses a greedy approach. If the total gas available is less 
    than the total cost required, it is mathematically impossible to complete 
    the circuit. If total gas >= total cost, a solution is guaranteed to exist.
    We track the current tank balance; if it drops below zero, the current 
    starting station (and all stations between the start and current) cannot 
    be the valid starting point.

    Args:
        gas: A list of integers representing the amount of gas at each station.
        cost: A list of integers representing the cost to travel to the next station.

    Returns:
        The starting station index if a solution exists, otherwise -1.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
        3
        >>> solve([2, 3, 4], [3, 4, 3])
        -1
    """
    total_surplus = 0
    current_tank = 0
    start_index = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total_surplus += diff
        current_tank += diff

        # If current_tank is negative, the current start_index cannot be the solution.
        # We reset the tank and try starting from the next station.
        if current_tank < 0:
            start_index = i + 1
            current_tank = 0

    # If the total gas collected is less than the total cost, no solution exists.
    # Otherwise, the greedy start_index is guaranteed to be valid.
    return start_index if total_surplus >= 0 else -1
