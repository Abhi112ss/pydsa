METADATA = {
    "id": 2888,
    "name": "Reshape Data: Concatenate",
    "slug": "reshape-data-concatenate",
    "category": "Data Manipulation",
    "aliases": [],
    "tags": ["pandas", "data_manipulation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Concatenate two datasets vertically or horizontally based on the specified axis.",
}

def solve(df1: list[list[any]], df2: list[list[any]], axis: int) -> list[list[any]]:
    """
    Concatenates two datasets (represented as lists of lists) along a specified axis.

    Args:
        df1: The first dataset.
        df2: The second dataset.
        axis: The axis along which to concatenate. 0 for vertical, 1 for horizontal.

    Returns:
        A new dataset containing the concatenated elements.

    Examples:
        >>> solve([[1, 2], [3, 4]], [[5, 6], [7, 8]], 0)
        [[1, 2], [3, 4], [5, 6], [7, 8]]
        >>> solve([[1, 2], [3, 4]], [[5, 6], [7, 8]], 1)
        [[1, 2, 5, 6], [3, 4, 7, 8]]
    """
    if axis == 0:
        # Vertical concatenation: simply append the rows of the second list to the first
        return df1 + df2
    
    elif axis == 1:
        # Horizontal concatenation: zip the rows of both datasets together
        # We assume df1 and df2 have the same number of rows for a valid horizontal concat
        result = []
        # Iterate through pairs of rows from both datasets
        for row1, row2 in zip(df1, df2):
            # Combine the elements of the two rows into a single list
            result.append(row1 + row2)
        return result
    
    else:
        raise ValueError("Axis must be 0 (vertical) or 1 (horizontal).")
