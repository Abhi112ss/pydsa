METADATA = {
    "id": 688,
    "name": "Knight Probability in Chessboard",
    "slug": "knight-probability-in-chessboard",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "probability", "math"],
    "difficulty": "medium",
    "time_complexity": "O(k * n * n)",
    "space_complexity": "O(n * n)",
    "description": "Calculate the probability that a knight remains on an n x n chessboard after k moves.",
}

def solve(n: int, k: int, knight_pos: list[int]) -> float:
    """
    Calculates the probability that a knight stays within an n x n chessboard after k moves.

    Args:
        n: The dimension of the n x n chessboard.
        k: The number of moves the knight makes.
        knight_pos: A list of two integers [row, col] representing the starting position.

    Returns:
        The probability that the knight remains on the board after k moves.

    Examples:
        >>> solve(3, 2, [0, 0])
        0.0625
        >>> solve(3, 1, [0, 0])
        0.0
    """
    # Possible moves for a knight in (delta_row, delta_col) format
    possible_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    # dp[r][c] stores the probability of being at square (r, c)
    # We use two grids to represent the current step and the next step to optimize space
    dp = [[0.0] * n for _ in range(n)]
    dp[knight_pos[0]][knight_pos[1]] = 1.0

    for _ in range(k):
        new_dp = [[0.0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                # If there is a non-zero probability of being at (r, c)
                if dp[r][c] > 0:
                    # Distribute the current probability equally among all 8 possible moves
                    prob_per_move = dp[r][c] / 8.0
                    for dr, dc in possible_moves:
                        nr, nc = r + dr, c + dc
                        # Only update if the move stays within the board boundaries
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += prob_per_move
        dp = new_dp

    # The total probability is the sum of probabilities of being at any square on the board
    total_probability = sum(sum(row) for row in dp)
    return total_probability
