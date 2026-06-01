METADATA = {
    "id": 735,
    "name": "Asteroid Collision",
    "slug": "asteroid-collision",
    "category": "Simulation",
    "aliases": [],
    "tags": ["stack", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine the state of asteroids after all possible collisions occur.",
}

def solve(asteroids: list[int]) -> list[int]:
    """
    Simulates asteroid collisions using a stack to track surviving asteroids.

    Args:
        asteroids: A list of integers representing the size and direction 
            of asteroids. Positive values move right, negative move left.

    Returns:
        A list of integers representing the asteroids remaining after all 
        collisions have settled.

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
        # A collision only happens if the current asteroid is moving left (< 0)
        # and the previous asteroid in the stack is moving right (> 0).
        while stack and current_asteroid < 0 < stack[-1]:
            # Compare absolute values to determine the winner
            if abs(current_asteroid) > abs(stack[-1]):
                # The right-moving asteroid in the stack is destroyed
                stack.pop()
                # Continue checking against the next asteroid in the stack
                continue
            elif abs(current_asteroid) == abs(stack[-1]):
                # Both asteroids are destroyed
                stack.pop()
                # Break the while loop as the current asteroid is gone
                break
            else:
                # The current left-moving asteroid is destroyed
                break
        else:
            # This block executes if the while loop finished without a 'break'
            # (i.e., the current asteroid survived all collisions or no collision occurred)
            stack.append(current_asteroid)

    return stack
