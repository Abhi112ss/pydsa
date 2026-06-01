METADATA = {
    "id": 2886,
    "name": "Change Data Type",
    "slug": "change-data-type",
    "category": "pandas",
    "aliases": [],
    "tags": ["pandas", "data_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a column in a pandas DataFrame from one data type to another.",
}

import pandas as pd

def solve(df: pd.DataFrame, column_name: str, target_type: str) -> pd.DataFrame:
    """
    Converts the specified column in a pandas DataFrame to the target data type.

    Args:
        df (pd.DataFrame): The input DataFrame containing the column to be converted.
        column_name (str): The name of the column to transform.
        target_type (str): The target data type as a string (e.g., 'int', 'float', 'str').

    Returns:
        pd.DataFrame: The DataFrame with the transformed column.

    Examples:
        >>> df = pd.DataFrame({'a': ['1', '2', '3']})
        >>> solve(df, 'a', 'int')
           a
        0  1
        1  2
        2  3
    """
    # Create a copy to avoid SettingWithCopyWarning if the input is a slice
    df = df.copy()

    # Map string type names to actual python/numpy types or use astype directly
    # pandas astype() is highly optimized for vectorized type conversion
    if target_type == 'int':
        df[column_name] = df[column_name].astype(int)
    elif target_type == 'float':
        df[column_name] = df[column_name].astype(float)
    elif target_type == 'str':
        df[column_name] = df[column_name].astype(str)
    else:
        # Fallback for other types like 'bool' or specific numpy types
        df[column_name] = df[column_name].astype(target_type)

    return df
