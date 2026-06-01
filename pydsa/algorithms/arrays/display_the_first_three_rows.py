METADATA = {
    "id": 2879,
    "name": "Display the First Three Rows",
    "slug": "display-the-first-three-rows",
    "category": "Pandas",
    "aliases": [],
    "tags": ["pandas"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Return the first three rows of a given DataFrame.",
}

import pandas as pd

def solve(players: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the first three rows of the provided DataFrame.

    Args:
        players (pd.DataFrame): The input DataFrame containing player data.

    Returns:
        pd.DataFrame: A DataFrame containing only the first three rows of the input.

    Examples:
        >>> import pandas as pd
        >>> df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David'], 'score': [10, 20, 30, 40]})
        >>> solve(df)
           name  score
        0  Alice     10
        1    Bob     20
        2  Charlie   30
    """
    # The head(n) method in pandas returns the first n rows of the DataFrame.
    # This is an O(1) operation in terms of complexity relative to the total size 
    # because it returns a view/slice of the existing data structure.
    return players.head(3)