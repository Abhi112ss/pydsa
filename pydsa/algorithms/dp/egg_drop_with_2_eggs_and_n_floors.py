METADATA = {
    "id": 1884,
    "name": "Egg Drop With 2 Eggs and N Floors",
    "slug": "egg-drop-with-2-eggs-and-n-floors",
    "category": "Math",
    "aliases": [],
    "tags": ["dp", "math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of moves required to determine the critical floor using exactly two eggs and n floors.",
}

def solve(k: int, n: int) -> int:
    """
    Calculates the minimum number of drops needed to find the critical floor 
    given exactly 2 eggs and n floors.

    The strategy uses the concept of triangular numbers. If we have 'x' moves, 
    the maximum number of floors we can cover is x + (x-1) + (x-2) + ... + 1.
    This is because if the first egg breaks at the first drop (floor x), 
    we use the second egg to check the remaining x-1 floors linearly. 
    If it doesn't break, we jump x-1 floors higher.

    Args:
        k (int): The number of eggs (always 2 in this specific problem version).
        n (int): The number of floors.

    Returns:
        int: The minimum number of drops required in the worst case.

    Examples:
        >>> solve(2, 6)
        3
        >>> solve(2, 2)
        2
        >>> solve(2, 10)
        4
    """
    # Since the problem specifically asks for 2 eggs, we solve for k=2.
    # We need to find the smallest integer 'moves' such that:
    # moves + (moves - 1) + (moves - 2) + ... + 1 >= n
    # This sum is the triangular number formula: (moves * (moves + 1)) / 2
    
    moves = 0
    floors_covered = 0
    
    # Increment moves until the total floors covered by the triangular 
    # series meets or exceeds the target n.
    while floors_covered < n:
        moves += 1
        floors_covered += moves
        
    return moves
