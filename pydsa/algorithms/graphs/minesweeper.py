METADATA = {
    "id": 529,
    "name": "Minesweeper",
    "slug": "minesweeper",
    "category": "Simulation",
    "aliases": [],
    "tags": ["dfs", "bfs", "matrix", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Simulate a single click in a minesweeper game, revealing cells or showing mine counts.",
}

def solve(board: list[list[str]], click: list[int]) -> list[list[str]]:
    """
    Simulates a single click on a Minesweeper board.

    Args:
        board: A 2D list of strings representing the current state of the board.
               'M' is a hidden mine, 'E' is an empty cell, '*' is a mine,
               'B' is an empty cell with no adjacent mines, and digits '1'-'8'
               represent the number of adjacent mines.
        click: A list of two integers [row, col] representing the click coordinates.

    Returns:
        The updated board after the click.

    Examples:
        >>> board = [["M","E","E","E","E"],["M","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
        >>> click = [3,0]
        >>> solve(board, click)
        [['M', 'E', 'E', 'E', 'E'], ['M', 'E', 'M', 'E', 'E'], ['B', 'B', 'B', 'E', 'E'], ['B', 'B', 'E', 'E', 'E']]
    """
    rows = len(board)
    cols = len(board[0])
    click_row, click_col = click[0], click[1]

    # If a mine is clicked, change it to '*' and return immediately
    if board[click_row][click_col] == 'M':
        board[click_row][click_col] = '*'
        return board

    def get_adjacent_mines(r: int, c: int) -> int:
        """Counts the number of mines in the 8 surrounding cells."""
        mine_count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == 'M':
                        mine_count += 1
        return mine_count

    # Use a stack for iterative DFS to avoid recursion depth issues
    stack = [(click_row, click_col)]
    
    while stack:
        curr_r, curr_c = stack.pop()
        
        # If the cell is already revealed, skip it
        if board[curr_r][curr_c] != 'E':
            continue
            
        # Count mines around the current cell
        mines_nearby = get_adjacent_mines(curr_r, curr_c)
        
        if mines_nearby > 0:
            # If there are mines nearby, reveal the digit and stop expanding this path
            board[curr_r][curr_c] = str(mines_nearby)
        else:
            # If no mines nearby, reveal 'B' and add all neighbors to the stack
            board[curr_r][curr_c] = 'B'
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = curr_r + dr, curr_c + dc
                    # Only add unrevealed empty cells to the stack
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'E':
                        stack.append((nr, nc))
                        
    return board
