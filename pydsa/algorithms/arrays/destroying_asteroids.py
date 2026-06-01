METADATA = {
    "id": 2126,
    "name": "Destroying Asteroids",
    "slug": "destroying_asteroids",
    "category": "Simulation",
    "aliases": [],
    "tags": ["stack", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Simulate the destruction of asteroids based on their mass and direction.",
}

def solve(asteroids: list[int]) -> list[int]:
    """
    Simulates the destruction of asteroids based on their mass and direction.
    
    Asteroids with positive mass move right, and negative mass move left.
    When two asteroids collide, the one with the larger absolute mass survives.
    If masses are equal, both are destroyed.

    Args:
        asteroids: A list of integers representing the mass and direction of asteroids.

    Returns:
        A list of integers representing the remaining asteroids after all collisions.

    Examples:
        >>> solve([5, 10, -5])
        [5, 10]
        >>> solve([8, -8])
        []
        >>> solve([-2, -1, 1, 2])
        [-2, -1, 1, 2]
    """
    stack: list[int] = []

    for current_asteroid in asteroids:
        # A collision only occurs if the current asteroid is moving left (negative)
        # and the previous asteroid in the stack is moving right (positive).
        is_collision_possible = current_asteroid < 0 and stack and stack[-1] > 0
        
        if is_collision_possible:
            destroyed = False
            # Continue colliding while the current asteroid is stronger than the top of the stack
            while stack and stack[-1] > 0 and current_asteroid < 0:
                top_mass = abs(stack[-1])
                current_mass = abs(current_asteroid)
                
                if current_mass > top_mass:
                    # Current asteroid destroys the top of the stack and keeps moving left
                    stack.pop()
                    continue
                elif current_mass == top_mass:
                    # Both asteroids are destroyed
                    stack.pop()
                    destroyed = True
                    break
                else:
                    # Current asteroid is destroyed by the top of the stack
                    destroyed = True
                    break
            
            # If the current asteroid survived all collisions, add it to the stack
            if not destroyed:
                stack.append(current_asteroid)
        else:
            # No collision possible (either both same direction, or moving away from each other)
            stack.append(current_asteroid)

    return stack
