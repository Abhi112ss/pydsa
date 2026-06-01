METADATA = {
    "id": 2881,
    "name": "Create a New Column",
    "slug": "create-a-new-column",
    "category": "Pandas",
    "aliases": [],
    "tags": ["pandas", "data-manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Create a new column based on conditional logic applied to an existing column in a DataFrame.",
}

import pandas as pd

def solve(statistics: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a new column 'is_high_income' based on the 'income' column.
    The new column is 1 if income is greater than or equal to 20,000, and 0 otherwise.

    Args:
        statistics (pd.DataFrame): A DataFrame containing at least an 'income' column.

    Returns:
        pd.DataFrame: The original DataFrame with the added 'is_high_income' column.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'income': [10000, 25000, 20000, 5000]})
        >>> solve(df)
           income  is_high_income
        0   10000               0
        1   25000               1
        2   20000               1
        3    5000               0
    """
    # We use the astype(int) method on a boolean series to convert 
    # True/False values into 1/0 efficiently.
    # This is a vectorized operation which is O(n) and highly optimized in pandas.
    statistics['is_high_income'] = (statistics['income'] >= 20000).astype(int)
    
    return statistics
