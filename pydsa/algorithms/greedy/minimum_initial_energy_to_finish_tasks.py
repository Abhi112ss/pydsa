METADATA = {
    "id": 1665,
    "name": "Minimum Initial Energy to Finish Tasks",
    "slug": "minimum-initial-energy-to-finish-tasks",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum initial energy required to complete all tasks given their cost and minimum energy requirement.",
}

def solve(costs: list[int], minimum_required: list[int]) -> int:
    """
    Calculates the minimum initial energy needed to complete all tasks.

    The strategy is to sort tasks based on the difference (minimum_required - cost).
    Tasks with a larger 'buffer' requirement relative to their cost should be 
    processed earlier to ensure the energy level stays high enough for subsequent tasks.

    Args:
        costs: A list of integers representing the energy cost of each task.
        minimum_required: A list of integers representing the minimum energy 
            required to start each task.

    Returns:
        The minimum initial energy required to complete all tasks.

    Examples:
        >>> solve([3, 5], [4, 5])
        6
        >>> solve([1, 2, 3], [2, 3, 4])
        6
    """
    # Combine costs and requirements into tuples for sorting
    tasks = list(zip(costs, minimum_required))

    # Sort tasks by the difference (requirement - cost) in descending order.
    # This greedy approach prioritizes tasks that leave the least 'slack' 
    # or require the most relative headroom.
    tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

    current_energy = 0
    total_needed = 0

    for cost, requirement in tasks:
        # If current energy is less than what is required to start the task,
        # we must increase our initial energy (total_needed) by the deficit.
        if current_energy < requirement:
            deficit = requirement - current_energy
            total_needed += deficit
            current_energy += deficit
        
        # After starting the task, subtract the cost from current energy
        current_energy -= cost

    return total_needed
