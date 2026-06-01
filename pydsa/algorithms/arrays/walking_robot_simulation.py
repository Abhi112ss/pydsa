METADATA = {
    "id": 874,
    "name": "Walking Robot Simulation",
    "slug": "walking-robot-simulation",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(n + k)",
    "space_complexity": "O(k)",
    "description": "Simulate a robot's movement on a 2D plane given a sequence of instructions and obstacle locations.",
}

def solve(instructions: list[str], obstacle_position: list[int]) -> int:
    """
    Simulates the movement of a robot based on instructions and obstacle positions.

    The robot starts at (0, 0) facing North. Instructions are 'G' (move forward),
    'L' (turn left), and 'R' (turn right). If the robot hits an obstacle, 
    it stops immediately.

    Args:
        instructions: A list of strings representing movement commands.
        obstacle_position: A list of two integers [x, y] representing the obstacle.

    Returns:
        int: The number of instructions executed before hitting the obstacle or finishing.

    Examples:
        >>> solve(["G", "G", "G", "L", "G", "G", "G", "L", "G", "G", "G"], [0, 1])
        0
        >>> solve(["G", "G", "G", "L", "G", "G", "G", "L", "G", "G", "G"], [0, 3])
        3
        >>> solve(["G", "G", "G", "L", "G", "G", "G", "L", "G", "G", "G"], [0, 4])
        11
    """
    # Directions: 0: North, 1: East, 2: South, 3: West
    # Using a delta array for (dx, dy) corresponding to the directions above
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    current_x, current_y = 0, 0
    current_direction_idx = 0  # Start facing North
    
    # Convert obstacle to a tuple for O(1) lookup
    obstacle = tuple(obstacle_position)
    
    instructions_executed = 0
    
    for command in instructions:
        if command == 'G':
            dx, dy = directions[current_direction_idx]
            next_x, next_y = current_x + dx, current_y + dy
            
            # Check if the next position is the obstacle
            if (next_x, next_y) == obstacle:
                break
            
            # Update position
            current_x, current_y = next_x, next_y
            instructions_executed += 1
        elif command == 'L':
            # Turn left: counter-clockwise in our directions array
            current_direction_idx = (current_direction_idx - 1) % 4
            instructions_executed += 1
        elif command == 'R':
            # Turn right: clockwise in our directions array
            current_direction_idx = (current_direction_idx + 1) % 4
            instructions_executed += 1
            
    return instructions_executed
