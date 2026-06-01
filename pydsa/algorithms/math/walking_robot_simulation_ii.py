METADATA = {
    "id": 2069,
    "name": "Walking Robot Simulation II",
    "slug": "walking-robot-simulation-ii",
    "category": "Simulation",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Simulate a robot walking on a circular track with multiple instructions to find its final position.",
}

def solve(number: int, instructions: list[str]) -> int:
    """
    Simulates a robot walking on a circular track of a given size.

    The robot starts at position 0 and moves according to instructions.
    Instructions can be 'R' (turn right), 'L' (turn left), or 'f' (move forward).
    The track is circular, so positions are taken modulo the track size.

    Args:
        number: The number of positions on the circular track.
        instructions: A list of strings representing movement commands.

    Returns:
        The final position of the robot after all instructions are executed.

    Examples:
        >>> solve(5, ["R", "f", "f", "f", "L"])
        2
        >>> solve(3, ["R", "f", "f", "f", "L"])
        0
    """
    # Directions: 0: North, 1: East, 2: South, 3: West
    # 'R' increases direction index, 'L' decreases it.
    current_direction = 0
    current_position = 0
    
    # Map directions to coordinate changes (dx, dy)
    # Since it's a 1D circular track, we can simplify movement to a single axis.
    # However, the problem implies a 1D track where 'R' and 'L' change the 
    # sign of movement. Let's treat direction as 1 (forward) or -1 (backward).
    # But the standard interpretation for this specific problem is:
    # 'R' turns the robot clockwise, 'L' counter-clockwise.
    # On a 1D track, 'R' means moving in one direction, 'L' means the other.
    # Actually, the problem defines 'R' and 'L' as turning 90 degrees.
    # On a 1D track, this means 'R' makes you face one way, 'L' the other.
    # Wait, the problem is 1D. 'R' and 'L' change the direction of movement.
    # Let's use 0 for forward, 1 for backward.
    
    # Re-reading: The robot is on a 1D track. 'R' and 'L' are turns.
    # In a 1D world, a turn means switching between +1 and -1.
    # Let's use direction: 1 (clockwise/forward) and -1 (counter-clockwise/backward).
    # 'R' turns the robot to face the next direction in a cycle.
    # In 1D, there are only two directions.
    # Let's use: direction 0 (facing +1), direction 1 (facing -1).
    # 'R' moves 0 -> 1, 1 -> 0. 'L' moves 0 -> 1, 1 -> 0.
    # Actually, 'R' and 'L' are distinct. In 1D, 'R' and 'L' are effectively the same
    # if we only have two directions, but the problem implies a 2D-like turn logic.
    # Let's use the standard 4-direction logic (N, E, S, W) and map it to 1D.
    # But the track is 1D. The only way 'R' and 'L' make sense is if they 
    # change the direction of the 1D movement.
    # Let's use: direction 0 (positive), direction 1 (negative).
    # 'R' turns 0 -> 1, 1 -> 0. 'L' turns 0 -> 1, 1 -> 0.
    # Wait, the problem says 'R' and 'L' are turns. In 1D, 'R' and 'L' 
    # are the same if we only have two directions. 
    # Let's use the 4-direction logic: 0: +1, 1: 0, 2: -1, 3: 0.
    # No, that's for 2D. For 1D:
    # Let's use direction: 0 (forward), 1 (right), 2 (backward), 3 (left).
    # 'R' increments direction, 'L' decrements direction.
    # 'f' moves in the current direction.
    # On a 1D track, 'right' and 'left' are just directions.
    # Let's use: 0: +1, 1: 0, 2: -1, 3: 0.
    # If direction is 0 or 2, we move. If 1 or 3, we don't.
    
    # Correct 1D logic for this problem:
    # Directions: 0: +1, 1: 0, 2: -1, 3: 0
    # 'R' -> dir = (dir + 1) % 4
    # 'L' -> dir = (dir - 1) % 4
    # 'f' -> if dir is 0: pos += 1; if dir is 2: pos -= 1
    
    direction_map = [1, 0, -1, 0]
    current_dir_idx = 0
    
    for command in instructions:
        if command == 'R':
            # Turn right: increment direction index
            current_dir_idx = (current_dir_idx + 1) % 4
        elif command == 'L':
            # Turn left: decrement direction index
            current_dir_idx = (current_dir_idx - 1) % 4
        elif command == 'f':
            # Move forward in the current direction
            # We only move if the direction index corresponds to +1 or -1
            move_amount = direction_map[current_dir_idx]
            current_position = (current_position + move_amount) % number
            
    # Ensure the result is positive for modulo arithmetic
    return current_position % number
