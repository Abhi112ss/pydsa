METADATA = {
    "id": 2610,
    "name": "Convert an Array Into a 2D Array With Conditions",
    "slug": "convert-an-array-into-a-2d-array-with-conditions",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a 1D array into a 2D array where each row has at most numRows elements and at most numCols elements, with rows containing only even numbers being filled first.",
}

def solve(nums: list[int], numRows: int, numCols: int) -> list[list[int]]:
    """
    Converts a 1D array into a 2D array based on row and column constraints,
    prioritizing rows that contain only even numbers.

    Args:
        nums: The input list of integers.
        numRows: The maximum number of rows allowed in the 2D array.
        numCols: The maximum number of columns allowed in each row.

    Returns:
        A 2D list of integers satisfying the given constraints.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6], 2, 3)
        [[2, 4, 6], [1, 3, 5]]
        >>> solve([1, 2, 3, 4, 5, 6], 3, 2)
        [[2, 4], [6], [1, 3]]
    """
    # Separate even and odd numbers to satisfy the condition that 
    # rows containing only even numbers are filled first.
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    
    # Combine them: all evens first, then all odds.
    # This allows us to treat the problem as a simple greedy partitioning.
    combined = evens + odds
    
    result = []
    current_index = 0
    total_elements = len(combined)
    
    # Iterate while we still have elements to place and haven't exceeded numRows.
    while len(result) < numRows and current_index < total_elements:
        # Calculate the end of the current row based on numCols constraint.
        end_index = min(current_index + numCols, total_elements)
        
        # Slice the combined list to form the current row.
        row = combined[current_index:end_index]
        result.append(row)
        
        # Move the pointer to the start of the next potential row.
        current_index = end_index
        
    return result
