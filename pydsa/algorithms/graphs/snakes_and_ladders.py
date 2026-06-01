METADATA = {
    "id": 909,
    "name": "Snakes and Ladders",
    "slug": "snakes-and-ladders",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "shortest_path", "breadth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of moves to reach the last square on a board with snakes and ladders using BFS.",
}

from collections import deque

def solve(board: list[list[int]]) -> int:
    """
    Finds the minimum number of dice rolls to reach the last square on a Snakes and Ladders board.

    Args:
        board: A 2D list representing the board. The board is labeled 1 to n^2 
               in a Boustrophedon (zigzag) pattern starting from the bottom-left.

    Returns:
        The minimum number of moves to reach the last square, or -1 if unreachable.

    Examples:
        >>> solve([[ -1, -1], [-1, -1]])
        -1
        >>> solve([[ -1, -1, -1], [-1, -1, -1], [ 1, -1, -1]])
        -1
        >>> solve([[ -1, -1, -1], [-1, -1, -1], [-1, -1, 1]])
        1
    """
    n = len(board)
    target = n * n

    def get_coordinates(square: int) -> tuple[int, int]:
        """Converts square number to (row, col) coordinates based on Boustrophedon pattern."""
        # Calculate row from bottom (0-indexed)
        row_from_bottom = (square - 1) // n
        # Calculate column
        col = (square - 1) % n
        
        # Actual row index in 2D array (top-down)
        row = (n - 1) - row_from_bottom
        
        # If row_from_bottom is odd, the direction is reversed (zigzag)
        if row_from_bottom % 2 == 1:
            col = (n - 1) - col
            
        return row, col

    # BFS setup
    queue = deque([(1, 0)])  # (current_square, moves_count)
    visited = {1}

    while queue:
        current_square, moves = queue.popleft()

        if current_square == target:
            return moves

        # Try all possible dice rolls (1 to 6)
        for dice_roll in range(1, 7):
            next_square = current_square + dice_roll
            
            if next_square <= target:
                r, c = get_coordinates(next_square)
                
                # If there is a snake or ladder, move to the destination
                destination = next_square
                if board[r][c] != -1:
                    destination = board[r][c]
                
                # Standard BFS: only visit if we haven't reached this destination before
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, moves + 1))

    return -1
