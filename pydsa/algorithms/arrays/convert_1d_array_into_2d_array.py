METADATA = {
    "id": 2022,
    "name": "Convert 1D Array Into 2D Array",
    "slug": "convert-1d-array-into-2d-array",
    "category": "Array",
    "aliases": [],
    "tags": ["array_manipulation", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a 1D array into a 2D array with a specified number of columns, returning an empty array if the total elements are insufficient.",
}

def solve(original: list[int], numRows: int, numCols: int) -> list[list[int]]:
    """
    Converts a 1D array into a 2D array with a given number of rows and columns.

    Args:
        original: The input 1D list of integers.
        numRows: The desired number of rows in the 2D array.
        numCols: The desired number of columns in the 2D array.

    Returns:
        A 2D list representing the converted array. Returns an empty list if 
        the original array does not have enough elements to fill the 
        numRows * numCols grid.

    Examples:
        >>> solve([1, 2, 3, 4], 2, 2)
        [[1, 2], [3, 4]]
        >>> solve([1, 2, 3, 4], 1, 4)
        [[1, 2, 3, 4]]
        >>> solve([1, 2, 3], 2, 2)
        []
    """
    # Check if the total elements required (rows * cols) is available in the original array
    if len(original) < numRows * numCols:
        return []

    result: list[list[int]] = []
    
    # Iterate through the array in chunks of size numCols
    for row_index in range(numRows):
        # Calculate the start and end indices for the current row in the 1D array
        start_idx = row_index * numCols
        end_idx = start_idx + numCols
        
        # Slice the original array to extract the row and append to the result
        result.append(original[start_idx:end_idx])
        
    return result
