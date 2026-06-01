METADATA = {
    "id": 892,
    "name": "Surface Area of 3D Shapes",
    "slug": "surface_area_of_3d_shapes",
    "category": "Geometry",
    "aliases": [],
    "tags": ["matrix", "geometry"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Calculate the total surface area of a 3D shape formed by stacking unit cubes on a grid.",
}


def solve(grid: list[list[int]]) -> int:
    """Calculate the total surface area of the 3D shape formed by stacking unit cubes.

    Args:
        grid: A square matrix where grid[i][j] represents the height of stacked cubes
              at position (i, j). Each height is a non‑negative integer.

    Returns:
        The total surface area of the resulting 3D shape.

    Examples:
        >>> solve([[1,2],[3,4]])
        34
        >>> solve([[2]])
        10
        >>> solve([[1,0],[0,2]])
        16
    """
    row_count: int = len(grid)
    if row_count == 0:
        return 0
    column_count: int = len(grid[0])

    total_surface: int = 0

    for i in range(row_count):
        for j in range(column_count):
            height: int = grid[i][j]
            if height == 0:
                continue
            # surface contributed by this stack alone (4 sides + top + bottom)
            total_surface += 4 * height + 2

            # subtract shared faces with the stack above (if any)
            if i > 0:
                neighbor_height: int = grid[i - 1][j]
                total_surface -= 2 * min(height, neighbor_height)

            # subtract shared faces with the stack to the left (if any)
            if j > 0:
                neighbor_height = grid[i][j - 1]
                total_surface -= 2 * min(height, neighbor_height)

    return total_surface