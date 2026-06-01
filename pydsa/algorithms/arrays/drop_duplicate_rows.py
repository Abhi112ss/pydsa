METADATA = {
    "id": 2882,
    "name": "Drop Duplicate Rows",
    "slug": "drop-duplicate-rows",
    "category": "Data Manipulation",
    "aliases": [],
    "tags": ["pandas", "data_cleaning", "hashing"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove duplicate rows from a dataset while preserving the original order of the first occurrences.",
}

def solve(rows: list[list[any]]) -> list[list[any]]:
    """
    Removes duplicate rows from a list of lists, keeping only the first occurrence.

    Args:
        rows: A list of lists, where each inner list represents a row of data.

    Returns:
        A list of lists containing only the unique rows in their original order.

    Examples:
        >>> solve([[1, 2], [3, 4], [1, 2], [5, 6]])
        [[1, 2], [3, 4], [5, 6]]
        >>> solve([[1, 1], [1, 1], [1, 1]])
        [[1, 1]]
    """
    seen_rows = set()
    unique_rows = []

    for row in rows:
        # Convert the list to a tuple because lists are unhashable 
        # and cannot be stored in a set.
        row_tuple = tuple(row)
        
        # If the tuple has not been encountered before, it is a unique row.
        if row_tuple not in seen_rows:
            unique_rows.append(row)
            seen_rows.add(row_tuple)

    return unique_rows
