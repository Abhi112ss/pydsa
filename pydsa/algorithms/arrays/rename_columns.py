METADATA = {
    "id": 2885,
    "name": "Rename Columns",
    "slug": "rename-columns",
    "category": "Pandas",
    "aliases": [],
    "tags": ["pandas", "data_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Rename the columns of a given DataFrame using a provided mapping dictionary.",
}

import pandas as pd

def solve(columns: list[str], rename_map: dict[str, str]) -> list[str]:
    """
    Renames the columns of a list based on a provided mapping dictionary.

    Args:
        columns: A list of strings representing the original column names.
        rename_map: A dictionary where keys are old column names and 
            values are the new column names.

    Returns:
        A list of strings representing the renamed column names.

    Examples:
        >>> solve(["foo", "bar"], {"foo": "baz"})
        ['baz', 'bar']
        >>> solve(["a", "b", "c"], {"a": "x", "c": "z"})
        ['x', 'b', 'z']
    """
    # We iterate through the original columns and use the dictionary's 
    # .get() method to retrieve the new name. 
    # If the key doesn't exist in the map, we keep the original name.
    return [rename_map.get(col, col) for col in columns]

def solve_pandas(df: pd.DataFrame, rename_map: dict[str, str]) -> pd.DataFrame:
    """
    Renames the columns of a pandas DataFrame using a mapping dictionary.

    Args:
        df: The input pandas DataFrame.
        rename_map: A dictionary mapping old column names to new ones.

    Returns:
        A new DataFrame with renamed columns.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'foo': [1], 'bar': [2]})
        >>> solve_pandas(df, {'foo': 'baz'})
           baz  bar
        0    1    2
    """
    # The rename method in pandas is the most efficient way to perform 
    # element-wise mapping on the index (columns).
    return df.rename(columns=rename_map)