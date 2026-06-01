METADATA = {
    "id": 2596,
    "name": "Check Knight Tour Configuration",
    "slug": "check-knight-tour-configuration",
    "category": "Simulation",
    "aliases": [],
    "tags": ["graphs", "simulation", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Verify if a given sequence of knight moves forms a valid tour covering all cells in an n x n grid exactly once.",
}

def solve(n: int, knight_tour: list[list[int]]) -> bool:
    """
    Verifies if the given knight_tour is a valid knight's tour on an n x n board.

    A valid tour must:
    1. Contain all numbers from 0 to n^2 - 1 exactly once.
    2. Each consecutive number in the sequence must be a valid knight move away.

    Args:
        n: The dimension of the n x n board.
        knight_tour: An n x n matrix representing the sequence of moves.

    Returns:
        True if the tour is valid, False otherwise.

    Examples:
        >>> solve(3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        False
        >>> solve(3, [[0, 4, 8], [5, 1, 6], [2, 7, 3]])
        True
    """
    # Map each value to its (row, col) coordinates for O(1) lookup
    # This allows us to check the distance between consecutive numbers easily
    position_map: dict[int, tuple[int, int]] = {}
    
    for row_index in range(n):
        for col_index in range(n):
            value = knight_tour[row_index][col_index]
            # If a value is out of the expected range [0, n^2 - 1], it's invalid
            if value < 0 or value >= n * n:
                return False
            # If we encounter a duplicate value, it's invalid
            if value in position_map:
                return False
            position_map[value] = (row_index, col_index)

    # Ensure all numbers from 0 to n^2 - 1 are present
    if len(position_map) != n * n:
        return False

    # Check if every consecutive step in the sequence is a valid knight move
    # A knight move is defined by a change of (±1, ±2) or (±2, ±1)
    for current_step in range(n * n - 1):
        r1, c1 = position_map[current_step]
        r2, c2 = position_map[current_step + 1]
        
        row_diff = abs(r1 - r2)
        col_diff = abs(c1 - c2)
        
        # A valid knight move must satisfy (dr=1 and dc=2) or (dr=2 and dc=1)
        is_valid_move = (row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1)
        
        if not is_valid_move:
            return False

    return True
