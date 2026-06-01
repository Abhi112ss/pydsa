METADATA = {
    "id": 3178,
    "name": "Find the Child Who Has the Ball After K Seconds",
    "slug": "find-the-child-who-has-the-ball-after-k-seconds",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(k)",
    "space_complexity": "O(1)",
    "description": "Simulate the movement of a ball being passed between children in a circle for k seconds.",
}

def solve(children: list[int], k: int) -> int:
    """
    Simulates the movement of a ball among children for k seconds.

    The ball starts at the first child (index 0). In each second, the ball 
    moves to the child at the index equal to the current child's value. 
    The index is calculated using modulo arithmetic to wrap around the circle.

    Args:
        children: A list of integers where children[i] represents the 
            jump distance from child i.
        k: The number of seconds to simulate.

    Returns:
        The index of the child who has the ball after k seconds.

    Examples:
        >>> solve([2, 3, 1, 1, 2, 1], 3)
        3
        >>> solve([1, 1, 1, 1], 2)
        2
    """
    current_index = 0
    num_children = len(children)

    # Simulate the movement for k seconds
    for _ in range(k):
        # The next position is determined by the value at the current index
        # We use modulo to ensure the index stays within the bounds of the list
        jump_distance = children[current_index]
        current_index = (current_index + jump_distance) % num_children

    return current_index
