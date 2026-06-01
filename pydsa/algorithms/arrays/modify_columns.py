METADATA = {
    "id": 2884,
    "name": "Modify Columns",
    "slug": "modify_columns",
    "category": "Pandas",
    "aliases": [],
    "tags": ["pandas", "data_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Modify specific columns in a DataFrame based on provided functions.",
}

import pandas as pd

def solve(columns: list[str], functions: list[callable], df: pd.DataFrame) -> pd.DataFrame:
    """
    Modifies the specified columns in the DataFrame using the provided functions.

    Args:
        columns: A list of column names to be modified.
        functions: A list of functions to apply to each corresponding column.
        df: The input pandas DataFrame.

    Returns:
        pd.DataFrame: The modified DataFrame.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        >>> solve(['a'], [lambda x: x + 1], df)
           a  b
        0  2  3
        1  3  4
    """
    # Iterate through the pairs of column names and their corresponding functions
    for column_name, func in zip(columns, functions):
        # Apply the function element-wise to the specified column
        # Using .loc to ensure we are modifying the original DataFrame structure correctly
        df[column_name] = df[column_name].apply(func)
        
    return df
