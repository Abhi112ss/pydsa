METADATA = {
    "id": 2282,
    "name": "Number of People That Can Be Seen in a Grid",
    "slug": "number-of-people-that-can-be-seen-in-a-grid",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "grid", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Count how many people can be seen from each cell in a grid, considering obstacles and line of sight in eight directions.",
}

def solve(grid: list[list[int]]) -> list[list[int]]:
    """
    Calculates the number of people visible from each cell in a grid.

    A person is visible if there is a direct line of sight in one of the 
    eight directions (horizontal, vertical, or diagonal) without any 
    obstacles (represented by 2) in between.

    Args:
        grid: A 2D list of integers where 0 is empty, 1 is a person, and 2 is an obstacle.

    Returns:
        A 2D list of integers of the same dimensions as the input grid, 
        where each cell contains the count of visible people.

    Examples:
        >>> grid = [[1, 2, 1], [0, 0, 0], [1, 0, 1]]
        >>> solve(grid)
        [[0, 0, 0], [2, 0, 2], [0, 0, 0]]
    """
    rows = len(grid)
    cols = len(grid[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    # The 8 possible directions: N, NE, E, SE, S, SW, W, NW
    directions = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]

    for r in range(rows):
        for c in range(cols):
            # If the current cell is an obstacle, no one can see from here
            if grid[r][c] == 2:
                continue
            
            visible_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Traverse in the current direction until we hit a boundary or obstacle
                while 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        # Found a person, increment count and stop looking in this direction
                        visible_count += 1
                        break
                    elif grid[nr][nc] == 2:
                        # Found an obstacle, stop looking in this direction
                        break
                    
                    # Move to the next cell in the same direction
                    nr += dr
                    nc += dc
            
            result[r][c] = visible_count

    return result
