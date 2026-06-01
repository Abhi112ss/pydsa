METADATA = {
    "id": 2880,
    "name": "Select Data",
    "slug": "select-data",
    "category": "Pandas",
    "aliases": [],
    "tags": ["pandas"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Select specific columns from a pandas DataFrame.",
}

import pandas as pd

def solve(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Selects the specified columns from the given pandas DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame containing the data.
        columns (list[str]): A list of column names to be selected.

    Returns:
        pd.DataFrame: A new DataFrame containing only the selected columns.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]})
        >>> columns = ['a', 'c']
        >>> solve(df, columns)
           a  c
        0  1  5
        1  2  6
    """
    # In pandas, passing a list of column names inside the indexing 
    # operator [] allows for selecting multiple columns simultaneously.
    # This returns a view or a copy of the DataFrame with only those columns.
    return df[columns]