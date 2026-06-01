METADATA = {
    "id": 957,
    "name": "Prison Cells After N Days",
    "slug": "prison-cells-after-n-days",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "hash_map", "cycle_detection"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Simulate the state of prison cells over N days, using cycle detection to handle large N.",
}

def solve(cells: list[int], n: int) -> list[int]:
    """
    Simulates the state of prison cells after N days using cycle detection.

    Args:
        cells: A list of 8 integers representing the initial state of the cells.
        n: The number of days to simulate.

    Returns:
        A list of 8 integers representing the state of the cells after N days.

    Examples:
        >>> solve([0,1,0,1,1,0,0,1], 7)
        [0, 0, 1, 1, 0, 0, 0, 0]
        >>> solve([1,0,0,1,0,0,1,0], 1)
        [0, 1, 1, 0, 0, 0, 1, 0]
    """
    def get_next_state(current_cells: list[int]) -> list[int]:
        """Computes the state of the cells for the next day."""
        next_state = [0] * 8
        # The first and last cells always become 0 because they don't have two neighbors
        for i in range(1, 7):
            # A cell becomes 1 if its neighbors are the same (both 0 or both 1)
            next_state[i] = 1 if current_cells[i - 1] == current_cells[i + 1] else 0
        return next_state

    seen_states: dict[tuple[int, ...], int] = {}
    current_state = cells
    day = 0

    while day < n:
        # Convert list to tuple to make it hashable for the dictionary
        state_tuple = tuple(current_state)
        
        # If we have seen this state before, a cycle is detected
        if state_tuple in seen_states:
            cycle_start_day = seen_states[state_tuple]
            cycle_length = day - cycle_start_day
            
            # Calculate how many days are left after skipping full cycles
            remaining_days = (n - day) % cycle_length
            
            # Simulate the remaining days after skipping cycles
            for _ in range(remaining_days):
                current_state = get_next_state(current_state)
            return current_state
        
        # Record the day we first encountered this state
        seen_states[state_tuple] = day
        current_state = get_next_state(current_state)
        day += 1

    return current_state
