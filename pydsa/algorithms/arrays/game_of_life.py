METADATA = {
    "id": 289,
    "name": "Game of Life",
    "slug": "game-of-life",
    "category": "Simulation",
    "aliases": [],
    "tags": ["matrix", "simulation", "in_place"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(1)",
    "description": "Simulate a cellular automaton where cells live or die based on their neighbors' states using in-place updates.",
}

def solve(board: list[list[int]]) -> None:
    """
    Simulates the Game of Life in-place on a 2D grid.

    The rules are:
    1. Any live cell with < 2 live neighbors dies (underpopulation).
    2. Any live cell with 2 or 3 live neighbors lives on to the next generation.
    3. Any live cell with > 3 live neighbors dies (overpopulation).
    4. Any dead cell with exactly 3 live neighbors becomes a live cell (reproduction).

    Args:
        board: A list of lists of integers representing the current state (0 or 1).

    Returns:
        None. The board is modified in-place.

    Examples:
        >>> board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        >>> solve(board)
        >>> board
        [[0,0,0],[1,0,1],[0,1,1],[0,0,0]]
    """
    if not board or not board[0]:
        return

    rows = len(board)
    cols = len(board[0])

    # We use temporary states to represent transitions:
    # 0 -> 0: Remains dead
    # 1 -> 1: Remains alive
    # 0 -> 1: Was dead, now alive (represented by 2)
    # 1 -> 0: Was alive, now dead (represented by -1)
    
    # Directions for the 8 neighbors
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            
            # Count neighbors that were originally alive
            # We check for 1 or -1 because both represent a cell that was originally alive
            for dr, dc in neighbor_offsets:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in (1, -1):
                        live_neighbors += 1

            # Apply Game of Life rules
            if board[r][c] == 1:
                # Rule 1 & 3: Live cell dies
                if live_neighbors < 2 or live_neighbors > 3:
                    board[r][c] = -1
                # Rule 2: Live cell lives (stays 1)
            else:
                # Rule 4: Dead cell becomes alive
                if live_neighbors == 3:
                    board[r][c] = 2

    # Second pass: Convert temporary states to final 0 or 1
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 2:
                board[r][c] = 1
            elif board[r][c] == -1:
                board[r][c] = 0
