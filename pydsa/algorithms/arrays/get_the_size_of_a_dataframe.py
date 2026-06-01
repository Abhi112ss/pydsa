METADATA = {
    "id": 2878,
    "name": "Get the Size of a DataFrame",
    "slug": "get-the-size-of-a-dataframe",
    "category": "pandas",
    "aliases": [],
    "tags": ["pandas"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the total number of elements in a pandas DataFrame.",
}

import pandas as pd

def solve(df: pd.DataFrame) -> int:
    """
    Returns the total number of elements in the given pandas DataFrame.

    The size of a DataFrame is the product of the number of rows and the 
    number of columns.

    Args:
        df (pd.DataFrame): The input pandas DataFrame.

    Returns:
        int: The total number of elements in the DataFrame.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        >>> solve(df)
        4
        >>> df2 = pd.DataFrame({'a': [1], 'b': [2], 'c': [3]})
        >>> solve(df2)
        3
    """
    # The .size attribute in pandas returns the total number of elements 
    # (rows * columns) in the DataFrame.
    return df.size