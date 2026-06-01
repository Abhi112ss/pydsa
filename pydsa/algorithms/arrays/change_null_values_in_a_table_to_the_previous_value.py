METADATA = {
    "id": 2388,
    "name": "Change Null Values in a Table to the Previous Value",
    "slug": "change-null-values-in-a-table-to-the-previous-value",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "window_functions", "data_processing"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Replace null values in a column with the most recent non-null value from a previous row based on an ordering column.",
}

def solve(table: list[dict]) -> list[dict]:
    """
    Simulates the SQL 'LAST_VALUE(... IGNORE NULLS)' behavior to fill nulls.

    Args:
        table: A list of dictionaries representing rows in a table. 
               Each dict contains 'id', 'call_date', and 'user_id'.
               The 'user_id' column contains the values to be filled.

    Returns:
        A list of dictionaries with null 'user_id' values replaced by the 
        most recent non-null 'user_id' for that specific user (if applicable) 
        or globally depending on the problem context. 
        Note: In the LeetCode context, the 'user_id' is the column being filled 
        based on the chronological order of 'call_date'.

    Examples:
        >>> table = [
        ...     {"id": 1, "call_date": "2023-01-01", "user_id": 1},
        ...     {"id": 2, "call_date": "2023-01-02", "user_id": None},
        ...     {"id": 3, "call_date": "2023-01-03", "user_id": 2},
        ...     {"id": 4, "call_date": "2023-01-04", "user_id": None}
        ... ]
        >>> solve(table)
        [{'id': 1, 'call_date': '2023-01-01', 'user_id': 1}, 
         {'id': 2, 'call_date': '2023-01-02', 'user_id': 1}, 
         {'id': 3, 'call_date': '2023-01-03', 'user_id': 2}, 
         {'id': 4, 'call_date': '2023-01-04', 'user_id': 2}]
    """
    if not table:
        return []

    # Sort the table by call_date to simulate the window function's ORDER BY clause
    # We create a copy to avoid mutating the input list directly
    sorted_rows = sorted(table, key=lambda x: x["call_date"])
    
    result = []
    last_seen_user_id = None

    for row in sorted_rows:
        # Create a shallow copy of the row to prevent modifying the original input
        new_row = row.copy()
        
        current_user_id = new_row.get("user_id")
        
        if current_user_id is not None:
            # If current value is not null, update the tracker
            last_seen_user_id = current_user_id
        else:
            # If current value is null, use the last non-null value found
            new_row["user_id"] = last_seen_user_id
            
        result.append(new_row)

    # The problem usually expects the output to be ordered by the original 'id' 
    # or simply returned as the processed set. LeetCode expects the rows 
    # to be returned, often sorted by 'id' for consistency.
    return sorted(result, key=lambda x: x["id"])
