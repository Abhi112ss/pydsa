METADATA = {
    "id": 1041,
    "name": "Robot Bounded In Circle",
    "slug": "robot-bounded-in-circle",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a robot's movement sequence results in a bounded path.",
}

def solve(instructions: list[str]) -> bool:
    """
    Determines if the robot stays within a bounded circle after infinite movements.

    The robot is bounded if and only if:
    1. It returns to the origin (0, 0) after one cycle of instructions.
    2. It is NOT facing North after one cycle of instructions. If it faces 
       any other direction, it will eventually form a closed loop after 2 or 4 cycles.

    Args:
        instructions: A list of characters representing movement ('G' for go, 
            'L' for left turn, 'R' for right turn).

    Returns:
        True if the robot's path is bounded, False otherwise.

    Examples:
        >>> solve(["G", "G", "L", "L", "G", "G"])
        True
        >>> solve(["G", "G", "G", "G", "L"])
        False
    """
    # Position coordinates
    x, y = 0, 0
    
    # Direction vectors: North, East, South, West
    # We use a list of tuples to represent (dx, dy) for each direction
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction_idx = 0  # Start facing North (index 0)

    for command in instructions:
        if command == 'G':
            # Move one step in the current direction
            dx, dy = directions[current_direction_idx]
            x += dx
            y += dy
        elif command == 'L':
            # Turn left: index moves counter-clockwise
            # In our directions list, left is (idx - 1) % 4
            current_direction_idx = (current_direction_idx - 1) % 4
        elif command == 'R':
            # Turn right: index moves clockwise
            # In our directions list, right is (idx + 1) % 4
            current_direction_idx = (current_direction_idx + 1) % 4

    # The robot is bounded if it is back at the origin
    # OR if it is not facing North (index 0)
    is_at_origin = (x == 0 and y == 0)
    is_not_facing_north = (current_direction_idx != 0)

    return is_at_origin or is_not_facing_north
