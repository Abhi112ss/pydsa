METADATA = {
    "id": 2280,
    "name": "Minimum Lines to Represent a Line Chart",
    "slug": "minimum-lines-to-represent-a-line-chart",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of lines needed to represent a line chart by counting how many times the slope between consecutive points changes.",
}

def solve(slopeChanges: list[list[int]]) -> int:
    """
    Calculates the minimum number of lines required to represent a line chart.
    
    A new line is required whenever the slope between two consecutive points 
    is different from the slope between the previous two points.

    Args:
        slopeChanges: A list of lists where slopeChanges[i] = [x_i, y_i].

    Returns:
        The minimum number of lines needed to represent the chart.

    Examples:
        >>> solve([[1, 1], [2, 2], [3, 3], [4, 1]])
        2
        >>> solve([[1, 1], [2, 2], [3, 3]])
        1
        >>> solve([[1, 1], [2, 2], [3, 1], [4, 2], [5, 3]])
        3
    """
    # If there are fewer than 2 points, we can't even form one line.
    # However, the problem constraints usually imply n >= 2.
    if len(slopeChanges) < 2:
        return 0

    # We always need at least one line if there are at least two points.
    line_count = 1
    
    # To avoid floating point precision issues with division (y2-y1)/(x2-x1),
    # we compare slopes using cross-multiplication:
    # (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2)
    # is equivalent to:
    # (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
    
    for i in range(2, len(slopeChanges)):
        # Coordinates for the three points involved in the slope comparison
        x1, y1 = slopeChanges[i - 2]
        x2, y2 = slopeChanges[i - 1]
        x3, y3 = slopeChanges[i]
        
        # Calculate differences (deltas)
        dx1 = x2 - x1
        dy1 = y2 - y1
        dx2 = x3 - x2
        dy2 = y3 - y2
        
        # Check if the slope (dy1/dx1) is different from (dy2/dx2)
        # Using cross-multiplication to maintain integer precision
        if dy1 * dx2 != dy2 * dx1:
            line_count += 1
            
    return line_count
