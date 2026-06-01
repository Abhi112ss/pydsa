METADATA = {
    "id": 2675,
    "name": "Array of Objects to Matrix",
    "slug": "array_of_objects_to_matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(rows * cols)",
    "space_complexity": "O(rows * cols)",
    "description": "Convert an array of coordinate-value objects into a 2D matrix of specified dimensions.",
}

from typing import Any, Dict, List


def solve(rows: int, cols: int, objects: List[Dict[str, Any]]) -> List[List[int]]:
    """
    Converts an array of objects containing row, col, and val into a 2D matrix.

    Args:
        rows: The number of rows in the resulting matrix.
        cols: The number of columns in the resulting matrix.
        objects: A list of dictionaries, where each dictionary contains 
                 'row', 'col', and 'val' keys.

    Returns:
        A 2D list (matrix) of integers with dimensions rows x cols.

    Examples:
        >>> solve(2, 3, [{"row": 0, "col": 1, "val": 5}, {"row": 1, "col": 2, "val": 10}])
        [[0, 5, 0], [0, 0, 10]]
        >>> solve(1, 1, [{"row": 0, "col": 0, "val": 1}])
        [[1]]
    """
    # Initialize the matrix with zeros using a list comprehension
    # to ensure each row is a unique object in memory.
    matrix: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

    # Iterate through each object to place the value at the specified coordinates.
    for obj in objects:
        row_idx = obj["row"]
        col_idx = obj["col"]
        value = obj["val"]
        
        # Update the matrix at the given position.
        # Note: In a production environment, we might add bounds checking here.
        matrix[row_idx][col_idx] = value

    return matrix
