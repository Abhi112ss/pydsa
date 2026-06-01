METADATA = {
    "id": 1659,
    "name": "Maximize Grid Happiness",
    "slug": "maximize-grid-happiness",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "dfs", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(3^n)",
    "space_complexity": "O(n)",
    "description": "Place n people in an n x n grid to maximize the sum of their happiness scores based on their neighbors.",
}

def solve(grid: list[list[int]], n: int) -> int:
    """
    Places n people in an n x n grid to maximize total happiness.
    
    Happiness is calculated by checking the 4-directional neighbors of each person.
    If a neighbor is also a person, their happiness score is added to the total.

    Args:
        grid: An n x n matrix where grid[i][j] is the happiness score of a person at (i, j).
        n: The number of people to place in the grid.

    Returns:
        The maximum possible total happiness.

    Examples:
        >>> grid = [[1, 2], [3, 4]]
        >>> n = 2
        >>> solve(grid, n)
        7
    """
    # current_grid stores the happiness score if a person is placed, 0 otherwise
    current_grid = [[0] * n for _ in range(n)]
    max_happiness = 0

    def get_happiness_gain(row: int, col: int) -> int:
        """Calculates the happiness added by placing a person at (row, col)."""
        gain = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n:
                # If neighbor has a person, add both scores to the total gain
                # because the new person gains neighbor's score AND neighbor gains new person's score
                if current_grid[nr][nc] > 0:
                    gain += current_grid[nr][nc] + grid[row][col]
        return gain

    def backtrack(people_left: int, start_idx: int, current_total: int) -> None:
        nonlocal max_happiness
        
        # Base case: all people placed
        if people_left == 0:
            max_happiness = max(max_happiness, current_total)
            return

        # Pruning: if remaining people cannot possibly beat max_happiness, stop
        # (Though in this specific problem, a simple backtrack is usually sufficient)

        # Iterate through the grid starting from start_idx to avoid duplicate combinations
        for idx in range(start_idx, n * n):
            r, c = divmod(idx, n)
            
            # Calculate happiness gain for placing a person at (r, c)
            gain = get_happiness_gain(r, c)
            
            # Place person
            current_grid[r][c] = grid[r][c]
            backtrack(people_left - 1, idx + 1, current_total + gain)
            
            # Backtrack: remove person
            current_grid[r][c] = 0

    backtrack(n, 0, 0)
    return max_happiness
