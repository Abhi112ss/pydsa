METADATA = {
    "id": 1131,
    "name": "Maximum of Absolute Value Expression",
    "slug": "maximum-of-absolute-value-expression",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum value of |xi ± xj| + |yi ± yj| for all pairs of points.",
}

def solve(points: list[list[int]]) -> int:
    """
    Calculates the maximum value of the expression |xi - xj| + |yi - yj| 
    for all pairs of points (xi, yi) and (xj, yj).

    The expression |xi - xj| + |yi - yj| can be expanded into four cases:
    1. (xi + yi) - (xj + yj)
    2. (xi - yi) - (xj - yj)
    3. (-xi + yi) - (-xj + yj)
    4. (-xi - yi) - (-xj - yj)
    
    Essentially, we need to find the maximum difference between (xi + yi) and (xi - yi) 
    across all points, or more generally, the max and min of (xi + yi) and (xi - yi).

    Args:
        points: A list of lists where each inner list contains two integers [xi, yi].

    Returns:
        The maximum absolute value expression result.

    Examples:
        >>> solve([[1, 2], [3, 4], [5, 6]])
        8
        >>> solve([[1, 1], [2, 2], [3, 3]])
        4
    """
    # We need to track the min and max for the two fundamental linear combinations:
    # Case A: x + y
    # Case B: x - y
    # The maximum of |xi - xj| + |yi - yj| is equivalent to:
    # max( max(x+y) - min(x+y), max(x-y) - min(x-y) )
    
    max_plus = float('-inf')
    min_plus = float('inf')
    max_minus = float('-inf')
    min_minus = float('inf')

    for x, y in points:
        # Calculate the two possible linear combinations for the current point
        val_plus = x + y
        val_minus = x - y
        
        # Update the running min/max for both combinations
        if val_plus > max_plus:
            max_plus = val_plus
        if val_plus < min_plus:
            min_plus = val_plus
            
        if val_minus > max_minus:
            max_minus = val_minus
        if val_minus < min_minus:
            min_minus = val_minus

    # The result is the maximum spread found in either combination
    return int(max(max_plus - min_plus, max_minus - min_minus))
