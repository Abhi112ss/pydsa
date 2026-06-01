METADATA = {
    "id": 1632,
    "name": "Rank Transform of a Matrix",
    "slug": "rank-transform-of-a-matrix",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(m * n log(m * n))",
    "space_complexity": "O(m * n)",
    "description": "Replace each element in a matrix with its rank among all unique elements in the matrix.",
}

def solve(matrix: list[list[int]]) -> list[list[int]]:
    """
    Transforms a matrix by replacing each element with its rank.
    The rank is determined by the sorted order of all unique elements in the matrix.

    Args:
        matrix: A 2D list of integers representing the input matrix.

    Returns:
        A 2D list of integers where each element is replaced by its rank.

    Examples:
        >>> solve([[4, 1, 2], [3, 5, 6]])
        [[3, 1, 2], [4, 5, 6]]
        >>> solve([[1, 1, 1], [1, 1, 1]])
        [[1, 1, 1], [1, 1, 1]]
    """
    if not matrix or not matrix[0]:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Flatten the matrix into a 1D list to collect all values
    flattened_elements = []
    for row in matrix:
        flattened_elements.extend(row)
    
    # Get unique elements and sort them to determine rank order
    unique_sorted_elements = sorted(list(set(flattened_elements)))
    
    # Create a mapping from the original value to its rank (1-indexed)
    # Using a dictionary for O(1) average lookup time
    rank_map: dict[int, int] = {
        val: rank + 1 
        for rank, val in enumerate(unique_sorted_elements)
    }
    
    # Construct the result matrix by looking up the rank for each element
    result: list[list[int]] = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(rank_map[matrix[r][c]])
        result.append(new_row)
        
    return result
