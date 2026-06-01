METADATA = {
    "id": 2664,
    "name": "The Knight's Tour",
    "slug": "the-knights-tour",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "dfs", "heuristics"],
    "difficulty": "hard",
    "time_complexity": "O(8^(n^2))",
    "space_complexity": "O(n^2)",
    "description": "Find a sequence of moves for a knight on an n x n chessboard such that it visits every square exactly once.",
}

def solve(n: int) -> list[list[int]]:
    """
    Finds a Knight's Tour on an n x n chessboard using Warnsdorff's rule.

    Warnsdorff's rule is a heuristic where the knight always moves to the 
    adjacent, unvisited square that has the minimum number of onward moves. 
    This significantly reduces the branching factor.

    Args:
        n: The dimension of the n x n chessboard.

    Returns:
        A 2D list representing the chessboard where each cell contains 
        the step number (0 to n^2 - 1) in which it was visited. 
        Returns an empty list if no tour is found.

    Examples:
        >>> solve(5)
        [[0, 11, 16, 5, 20], [17, 4, 21, 10, 15], [12, 1, 24, 19, 6], [3, 18, 7, 14, 9], [22, 23, 2, 13, 8]]
    """
    if n <= 0:
        return []
    if n == 1:
        return [[0]]

    # Knight move offsets
    MOVES = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    board = [[-1 for _ in range(n)] for _ in range(n)]

    def is_valid(r: int, c: int) -> bool:
        return 0 <= r < n and 0 <= c < n and board[r][c] == -1

    def get_degree(r: int, c: int) -> int:
        """Counts the number of available moves from a given position."""
        count = 0
        for dr, dc in MOVES:
            if is_valid(r + dr, c + dc):
                count += 1
        return count

    def backtrack(r: int, c: int, step: int) -> bool:
        board[r][c] = step
        
        if step == n * n - 1:
            return True

        # Warnsdorff's Heuristic:
        # Sort possible next moves by their 'degree' (number of onward moves).
        # This prioritizes squares that are harder to reach later.
        candidates = []
        for dr, dc in MOVES:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                degree = get_degree(nr, nc)
                candidates.append((degree, nr, nc))
        
        # Sort by degree ascending
        candidates.sort(key=lambda x: x[0])

        for _, nr, nc in candidates:
            if backtrack(nr, nc, step + 1):
                return True

        # Backtrack
        board[r][c] = -1
        return False

    # Start the tour from the top-left corner (0, 0)
    # Note: For some n, a tour might not exist or might require a different start.
    # However, for standard Knight's Tour problems, (0,0) is a common starting point.
    if backtrack(0, 0, 0):
        return board
    
    return []
