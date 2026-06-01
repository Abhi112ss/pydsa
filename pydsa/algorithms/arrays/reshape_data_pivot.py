METADATA = {
    "id": 2889,
    "name": "Reshape Data: Pivot",
    "slug": "reshape_data_pivot",
    "category": "Data Manipulation",
    "aliases": [],
    "tags": ["pandas", "data_manipulation", "pivot"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Reshape a dataset by pivoting values from one column into multiple new columns based on unique values in another column.",
}

def solve(data: list[dict[str, any]], index_col: str, columns_col: str, values_col: str) -> list[dict[str, any]]:
    """
    Reshapes the input data by pivoting the values of 'values_col' into new columns 
    defined by the unique values found in 'columns_col', grouped by 'index_col'.

    Args:
        data: A list of dictionaries representing the input rows.
        index_col: The column name to be used as the unique identifier for rows.
        columns_col: The column name whose unique values will become new column headers.
        values_col: The column name containing the values to populate the new columns.

    Returns:
        A list of dictionaries representing the pivoted dataset.

    Examples:
        >>> data = [
        ...     {"id": 1, "attr": "A", "val": 10},
        ...     {"id": 1, "attr": "B", "val": 20},
        ...     {"id": 2, "attr": "A", "val": 30}
        ... ]
        >>> solve(data, "id", "attr", "val")
        [{'id': 1, 'A': 10, 'B': 20}, {'id': 2, 'A': 30, 'B': None}]
    """
    # Dictionary to store the pivoted rows: {index_value: {column_name: value}}
    pivoted_map: dict[any, dict[str, any]] = {}
    
    # Set to keep track of all unique column headers encountered
    unique_columns: set[str] = set()

    # First pass: Group values by the index column and identify all unique column headers
    for row in data:
        idx_val = row[index_col]
        col_header = row[columns_col]
        val = row[values_col]

        unique_columns.add(col_header)

        if idx_val not in pivoted_map:
            pivoted_map[idx_val] = {index_col: idx_val}
        
        # Assign the value to the specific column header for this index
        pivoted_map[idx_val][col_header] = val

    # Second pass: Ensure every row contains all unique column headers (fill missing with None)
    # and maintain a consistent structure for the output.
    result: list[dict[str, any]] = []
    
    # Sort keys to ensure deterministic output order (optional but good for testing)
    sorted_indices = sorted(pivoted_map.keys())
    sorted_headers = sorted(list(unique_columns))

    for idx in sorted_indices:
        row_data = pivoted_map[idx]
        # Fill in missing columns with None to simulate a complete DataFrame structure
        for header in sorted_headers:
            if header not in row_data:
                row_data[header] = None
        result.append(row_data)

    return result
