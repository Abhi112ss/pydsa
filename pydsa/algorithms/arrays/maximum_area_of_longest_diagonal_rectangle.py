METADATA = {
    "id": 3000,
    "name": "Maximum Area of Longest Diagonal Rectangle",
    "slug": "maximum-area-of-longest-diagonal-rectangle",
    "category": "Math",
    "aliases": [],
    "tags": ["geometry", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the area of the rectangle with the longest diagonal, and if there's a tie, the one with the largest area.",
}

def solve(dimensions: list[list[int]]) -> int:
    """
    Finds the maximum area among rectangles that have the longest diagonal.

    Args:
        dimensions: A list of lists where each inner list contains two integers [length, width].

    Returns:
        The area of the rectangle with the longest diagonal. If multiple rectangles 
        have the same longest diagonal, returns the maximum area among them.

    Examples:
        >>> solve([[9, 3], [8, 6]])
        48
        >>> solve([[3, 4], [4, 3]])
        12
        >>> solve([[1, 1], [2, 2], [3, 3]])
        9
    """
    max_diagonal_sq: int = 0
    max_area: int = 0

    for length, width in dimensions:
        # Calculate diagonal squared to avoid floating point precision issues
        # diagonal^2 = length^2 + width^2
        current_diagonal_sq = length**2 + width**2
        current_area = length * width

        # If we find a strictly longer diagonal, update both diagonal and area
        if current_diagonal_sq > max_diagonal_sq:
            max_diagonal_sq = current_diagonal_sq
            max_area = current_area
        
        # If the diagonal is equal to the current maximum, pick the larger area
        elif current_diagonal_sq == max_diagonal_sq:
            if current_area > max_area:
                max_area = current_area

    return max_area
