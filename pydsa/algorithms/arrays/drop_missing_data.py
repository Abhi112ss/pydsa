METADATA = {
    "id": 2883,
    "name": "Drop Missing Data",
    "slug": "drop-missing-data",
    "category": "Data Manipulation",
    "aliases": [],
    "tags": ["pandas", "data_cleaning"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Remove rows from a dataset where any of the specified columns contain null values.",
}

import pandas as pd

def solve(dataset: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Removes rows from the dataset where any of the specified columns have missing values.

    Args:
        dataset (pd.DataFrame): The input DataFrame containing data.
        columns (list[str]): A list of column names to check for null values.

    Returns:
        pd.DataFrame: A new DataFrame with rows containing nulls in the specified 
            columns removed.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'a': [1, None, 3], 'b': [4, 5, None], 'c': [7, 8, 9]})
        >>> solve(df, ['a', 'b'])
           a    b  c
        0  1.0  4.0  7
        2  3.0  NaN  9  # Wait, the logic is to drop if ANY of the specified columns are null.
        # Correct example behavior:
        >>> df = pd.DataFrame({'a': [1, None, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        >>> solve(df, ['a'])
           a  b  c
        0  1  4  7
        2  3  6  9
    """
    # Use the subset parameter of dropna to target only the specified columns.
    # This is more efficient than manual boolean indexing for large datasets.
    cleaned_dataset = dataset.dropna(subset=columns)
    
    return cleaned_dataset
