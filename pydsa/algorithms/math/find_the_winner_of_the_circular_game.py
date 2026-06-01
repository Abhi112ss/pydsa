METADATA = {
    "id": 1823,
    "name": "Find the Winner of the Circular Game",
    "slug": "find-the-winner-of-the-circular-game",
    "category": "Math",
    "aliases": ["Josephus Problem"],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the winner of a circular game where every k-th person is removed until only one remains.",
}

def solve(n: int, k: int) -> int:
    """
    Finds the winner of the circular game using the Josephus problem recurrence.

    The problem can be modeled by the recurrence relation:
    f(n, k) = (f(n - 1, k) + k) % n
    where f(n, k) is the position of the winner in a circle of size n.
    Since the problem uses 1-based indexing, we calculate using 0-based 
    indexing and add 1 at the end.

    Args:
        n: The number of people in the circle.
        k: The step size for removal.

    Returns:
        The 1-based index of the winner.

    Examples:
        >>> solve(5, 2)
        3
        >>> solve(6, 5)
        1
    """
    # winner_index tracks the position of the winner in a circle of size 'i'
    # We start with a circle of size 1, where the winner is at index 0.
    winner_index = 0

    # Iteratively build up the solution for circles of size 2 to n.
    # This avoids the overhead of recursion and uses O(1) space.
    for current_circle_size in range(2, n + 1):
        # The recurrence relation shifts the winner's position based on the step k.
        # We use modulo to wrap around the circular structure.
        winner_index = (winner_index + k) % current_circle_size

    # Convert the 0-based index back to 1-based indexing as required by the problem.
    return winner_index + 1
