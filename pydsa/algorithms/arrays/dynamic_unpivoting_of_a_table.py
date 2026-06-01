METADATA = {
    "id": 2253,
    "name": "Dynamic Unpivoting of a Table",
    "slug": "dynamic-unpivoting-of-a-table",
    "category": "Simulation",
    "aliases": [],
    "tags": ["hash_map", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N * M)",
    "description": "Transform a table by unpivoting columns into rows based on a specified index column.",
}

def solve(table: list[list[str]], index_column: str) -> list[list[str]]:
    """
    Transforms a table by unpivoting columns into rows.

    The function identifies the index column, then for every other column, 
    it creates a new row containing the index column value, the column name, 
    and the cell value.

    Args:
        table: A 2D list of strings representing the table. 
               The first row is the header.
        index_column: The name of the column to be used as the identifier.

    Returns:
        A 2D list of strings representing the unpivoted table. 
        The first row is ['index_column', 'variable', 'value'].

    Examples:
        >>> table = [["id", "name", "age"], ["1", "Alice", "25"], ["2", "Bob", "30"]]
        >>> index_column = "id"
        >>> solve(table, index_column)
        [['id', 'variable', 'value'], ['1', 'name', 'Alice'], ['1', 'age', '25'], ['2', 'name', 'Bob'], ['2', 'age', '30']]
    """
    if not table:
        return []

    headers = table[0]
    
    # Find the index of the column that will serve as our identifier
    try:
        index_col_idx = headers.index(index_column)
    except ValueError:
        return []

    # Initialize the result with the new header structure
    result: list[list[str]] = [[index_column, "variable", "value"]]

    # Iterate through each data row (skipping the header row)
    for row_idx in range(1, len(table)):
        current_row = table[row_idx]
        index_value = current_row[index_col_idx]

        # Iterate through all columns to unpivot them
        for col_idx in range(len(headers)):
            # Skip the column that is acting as our index
            if col_idx == index_col_idx:
                continue
            
            # Append the new row: [index_val, column_name, cell_value]
            result.append([
                index_value,
                headers[col_idx],
                current_row[col_idx]
            ])

    return result
