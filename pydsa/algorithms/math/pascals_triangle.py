METADATA = {
    "id": 118,
    "name": "Pascal's Triangle",
    "slug": "pascals-triangle",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "dynamic_programming"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Given an integer numRows, return the first numRows of Pascal's triangle.",
}

def solve(num_rows: int) -> list[list[int]]:
    """
    Generates the first num_rows of Pascal's triangle.

    Args:
        num_rows: The number of rows to generate.

    Returns:
        A list of lists representing Pascal's triangle.

    Examples:
        >>> solve(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if num_rows <= 0:
        return []

    triangle: list[list[int]] = []

    for row_index in range(num_rows):
        # Initialize the row with 1s. 
        # A row at index 'i' has 'i + 1' elements.
        row = [1] * (row_index + 1)

        # Each interior element (not the first or last) is the sum 
        # of the two elements directly above it in the previous row.
        for col_index in range(1, row_index):
            prev_row = triangle[row_index - 1]
            row[col_index] = prev_row[col_index - 1] + prev_row[col_index]

        triangle.append(row)

    return triangle
