METADATA = {
    "id": 2877,
    "name": "Create a DataFrame from List",
    "slug": "create-a-dataframe-from-list",
    "category": "Pandas",
    "aliases": [],
    "tags": ["pandas"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Create a pandas DataFrame from a list of lists where each inner list represents a row.",
}

import pandas as pd

def solve(data: list[list[int]]) -> pd.DataFrame:
    """
    Creates a pandas DataFrame from a list of lists.

    Args:
        data: A list of lists where each inner list contains integers 
              representing a row in the DataFrame.

    Returns:
        A pandas DataFrame constructed from the input data.

    Examples:
        >>> solve([[1, 2], [3, 4]])
           0  1
        0  1  2
        1  3  4
    """
    # The pandas DataFrame constructor accepts a list of lists directly.
    # Each inner list is treated as a row, and columns are indexed 0 to N-1.
    df = pd.DataFrame(data)
    
    return df
