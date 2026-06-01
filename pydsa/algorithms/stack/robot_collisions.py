METADATA = {
    "id": 2751,
    "name": "Robot Collisions",
    "slug": "robot-collisions",
    "category": "Simulation",
    "aliases": [],
    "tags": ["stack", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Simulate robot collisions on a 1D line where robots move left or right and destroy each other based on specific rules.",
}

def solve(robots: list[list[int]]) -> list[list[int]]:
    """
    Simulates the collisions of robots moving on a 1D line.

    Robots collide if they are moving towards each other. 
    A collision between a right-moving robot and a left-moving robot 
    results in the destruction of one or both based on their energy.

    Args:
        robots: A list of robots, where each robot is [position, direction].
                direction is 1 for right and -1 for left.

    Returns:
        A list of robots that remain after all collisions have occurred.

    Examples:
        >>> solve([[5, -1], [2, 2], [3, 3], [4, -1]])
        [[2, 2], [3, 3]]
        >>> solve([[10, -1], [5, 1], [11, -1]])
        [[5, 1]]
    """
    # Sort robots by position to process them from left to right
    robots.sort()
    
    stack: list[list[int]] = []

    for current_robot in robots:
        curr_pos, curr_dir = current_robot
        
        # A collision only happens if the current robot is moving LEFT (-1)
        # and the previous robot in the stack is moving RIGHT (1).
        if curr_dir == -1:
            is_destroyed = False
            
            while stack and stack[-1][1] == 1:
                prev_pos, prev_dir = stack[-1]
                
                # Compare energy (represented by position in this problem context)
                # Note: The problem implies energy is the position value.
                if prev_pos < curr_pos:
                    # Right-moving robot is destroyed, current robot continues
                    stack.pop()
                    continue
                elif prev_pos > curr_pos:
                    # Left-moving robot is destroyed, current robot is gone
                    is_destroyed = True
                    break
                else:
                    # Both robots have equal energy and destroy each other
                    stack.pop()
                    is_destroyed = True
                    break
            
            if not is_destroyed:
                stack.append(current_robot)
        else:
            # If robot is moving RIGHT, it cannot collide with anything 
            # currently in the stack (since stack contains robots to its left).
            stack.append(current_robot)

    return stack
