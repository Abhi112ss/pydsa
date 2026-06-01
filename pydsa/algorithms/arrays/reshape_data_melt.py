METADATA = {
    "id": 2890,
    "name": "Reshape Data: Melt",
    "slug": "reshape_data_melt",
    "category": "Data Manipulation",
    "aliases": [],
    "tags": ["pandas", "data_manipulation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N * M)",
    "description": "Unpivot a 2D structure by transforming multiple columns into two columns: one for variable names and one for values.",
}

def solve(df: list[dict[str, any]], id_vars: list[str], value_vars: list[str]) -> list[dict[str, any]]:
    """
    Reshapes the data from a wide format to a long format (unpivoting).

    Args:
        df: A list of dictionaries representing the input table rows.
        id_vars: A list of column names to be used as identifier variables.
        value_vars: A list of column names to be unpivoted into 'variable' and 'value'.

    Returns:
        A list of dictionaries representing the melted (long format) table.

    Examples:
        >>> df = [{"id": 1, "a": 10, "b": 20}, {"id": 2, "a": 30, "b": 40}]
        >>> id_vars = ["id"]
        >>> value_vars = ["a", "b"]
        >>> solve(df, id_vars, value_vars)
        [{'id': 1, 'variable': 'a', 'value': 10}, {'id': 1, 'variable': 'b', 'value': 20}, 
         {'id': 2, 'variable': 'a', 'value': 30}, {'id': 2, 'variable': 'b', 'value': 40}]
    """
    melted_data: list[dict[str, any]] = []

    for row in df:
        # Extract the identifier values that remain constant for this row's unpivoted versions
        base_row: dict[str, any] = {var: row[var] for var in id_vars}
        
        # For every column specified in value_vars, create a new row entry
        for var_name in value_vars:
            # Create a new dictionary combining the identifiers with the new variable/value pair
            new_entry = base_row.copy()
            new_entry["variable"] = var_name
            new_entry["value"] = row[var_name]
            melted_data.append(new_entry)

    return melted_data
