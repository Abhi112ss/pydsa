METADATA = {
    "id": 2159,
    "name": "Order Two Columns Independently",
    "slug": "order-two-columns-independently",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Sort two columns of a 2D array independently based on specific rules for each column.",
}

def solve(grid: list[list[int]]) -> list[list[int]]:
    """
    Sorts the two columns of a 2D grid independently.
    
    Column 0 is sorted in descending order.
    Column 1 is sorted in ascending order.
    The rows are reconstructed such that the sorted values are placed back into their respective columns.

    Args:
        grid: A 2D list of integers where each row has exactly two elements.

    Returns:
        A 2D list of integers with the columns sorted independently.

    Examples:
        >>> solve([[1, 1], [3, 2], [2, 3]])
        [[3, 1], [2, 2], [1, 3]]
        >>> solve([[1, 3], [2, 2], [3, 1]])
        [[3, 1], [2, 2], [1, 3]]
    """
    if not grid:
        return []

    # Extract the columns into separate lists
    # col0 will contain all elements from the first column
    # col1 will contain all elements from the second column
    col0 = [row[0] for row in grid]
    col1 = [row[1] for row in grid]

    # Sort column 0 in descending order
    col0.sort(reverse=True)
    
    # Sort column 1 in ascending order
    col1.sort()

    # Reconstruct the grid by pairing the sorted elements back together
    # We iterate through the length of the columns and create new rows
    result = []
    for i in range(len(grid)):
        result.append([col0[i], col1[i]])

    return result
