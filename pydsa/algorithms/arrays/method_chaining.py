METADATA = {
    "id": 2891,
    "name": "Method Chaining",
    "slug": "method_chaining",
    "category": "Pandas",
    "aliases": [],
    "tags": ["pandas", "data_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Perform a sequence of data manipulation operations on a DataFrame using method chaining.",
}

import pandas as pd

def solve(df: pd.DataFrame, operations: list[dict]) -> pd.DataFrame:
    """
    Applies a series of pandas operations to a DataFrame using method chaining.

    Args:
        df (pd.DataFrame): The initial input DataFrame.
        operations (list[dict]): A list of dictionaries where each dictionary 
            represents an operation. Supported operations:
            - {'type': 'filter', 'condition': lambda x: ...}
            - {'type': 'sort', 'by': str, 'ascending': bool}
            - {'type': 'select', 'columns': list[str]}
            - {'type': 'assign', 'column': str, 'value': lambda x: ...}
            - {'type': 'groupby_agg', 'by': str, 'agg_dict': dict}

    Returns:
        pd.DataFrame: The transformed DataFrame after all operations are applied.

    Examples:
        >>> df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        >>> ops = [{'type': 'filter', 'condition': lambda x: x['a'] > 1}]
        >>> solve(df, ops)
           a  b
        1  2  5
        2  3  6
    """
    # We use a functional approach to chain operations.
    # Since pandas methods often return new objects, we can iterate through 
    # the operations list and update the reference to the current DataFrame.
    
    current_df = df.copy()

    for op in operations:
        op_type = op["type"]

        if op_type == "filter":
            # Apply boolean indexing based on the provided condition function
            current_df = current_df[op["condition"](current_df)]

        elif op_type == "sort":
            # Sort the DataFrame by specified columns
            current_df = current_df.sort_values(
                by=op["by"], 
                ascending=op.get("ascending", True)
            )

        elif op_type == "select":
            # Subset the DataFrame to include only specific columns
            current_df = current_df[op["columns"]]

        elif op_type == "assign":
            # Create new columns or overwrite existing ones using a lambda/value
            current_df = current_df.assign(**{op["column"]: op["value"](current_df)})

        elif op_type == "groupby_agg":
            # Group by a column and apply aggregation functions
            current_df = current_df.groupby(op["by"]).agg(op["agg_dict"]).reset_index()

    return current_df
