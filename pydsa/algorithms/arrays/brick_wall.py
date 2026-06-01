METADATA = {
    "id": 554,
    "name": "Brick Wall",
    "slug": "brick-wall",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash table", "array", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(w)",
    "description": "Find the minimum number of bricks to cross a wall by finding the maximum number of edges at a single vertical position.",
}

def solve(wall: list[int], target_width: int) -> int:
    """
    Finds the minimum number of bricks required to cross the wall.

    The strategy is to find the vertical line that passes through the maximum 
    number of brick edges. The number of bricks crossed at that line will be 
    the total height minus the maximum number of edges found at any position.

    Args:
        wall: A list of integers representing the widths of bricks in each row.
        target_width: The total width of the wall.

    Returns:
        The minimum number of bricks that must be crossed.

    Examples:
        >>> solve([1, 2, 2, 1], 5)
        1
        >>> solve([1, 1, 1, 1, 1], 5)
        5
    """
    # edge_counts maps the x-coordinate of a vertical edge to the number of edges at that position
    edge_counts: dict[int, int] = {}
    current_x_position = 0

    # Iterate through each row to find the positions of all vertical edges
    for brick_width in wall:
        current_x_position += brick_width
        
        # We ignore the very last edge because it is the boundary of the wall, 
        # not a line passing through the wall.
        if current_x_position < target_width:
            edge_counts[current_x_position] = edge_counts.get(current_x_position, 0) + 1

    # If no edges were found (e.g., wall is one big brick), max_edges is 0
    max_edges = 0
    if edge_counts:
        max_edges = max(edge_counts.values())

    # The minimum bricks crossed is the total height (number of rows) minus 
    # the maximum number of edges we can align vertically.
    return len(wall) - max_edges
