METADATA = {
    "id": 3402,
    "name": "Minimum Operations to Make Columns Strictly Increasing",
    "slug": "minimum-operations-to-make-columns-strictly-increasing",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make each column in a grid strictly increasing by incrementing elements.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the minimum number of operations to make each column in a grid strictly increasing.
    An operation consists of incrementing an element by 1. To make a column strictly increasing,
    each element grid[i][j] must be greater than grid[i-1][j].

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        The total minimum number of operations required.

    Examples:
        >>> solve([[1, 2], [1, 1]])
        2
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        6
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    total_operations = 0

    # Iterate through each column independently
    for col in range(cols):
        # Start from the second row (index 1) to compare with the previous row
        for row in range(1, rows):
            previous_value = grid[row - 1][col]
            current_value = grid[row][col]

            # If the current element is not strictly greater than the one above it
            if current_value <= previous_value:
                # The minimum value required to make it strictly increasing is previous_value + 1
                target_value = previous_value + 1
                diff = target_value - current_value
                
                # Accumulate the operations needed
                total_operations += diff
                
                # Update the grid value in-place to reflect the change for the next row comparison
                grid[row][col] = target_value

    return total_operations
