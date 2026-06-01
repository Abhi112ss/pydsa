METADATA = {
    "id": 883,
    "name": "Projection Area of 3D Shapes",
    "slug": "projection-area-of-3d-shapes",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Calculate the total projection area of a 3D shape on the XY, YZ, and ZX planes.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Args:
        grid: A 2D list of integers representing the heights of the 3D shape.

    Returns:
        The sum of the projection areas on the XY, YZ, and ZX planes.
    """
    n = len(grid)
    xy_area = 0
    yz_area = 0
    zx_area = 0

    for i in range(n):
        row_max = 0
        col_max = 0
        for j in range(n):
            if grid[i][j] > 0:
                xy_area += 1
            
            if grid[i][j] > row_max:
                row_max = grid[i][j]
            
            if grid[j][i] > col_max:
                col_max = grid[j][i]
        
        yz_area += row_max
        zx_area += col_max

    return xy_area + yz_area + zx_area