METADATA = {
    "id": 391,
    "name": "Perfect Rectangle",
    "slug": "perfect-rectangle",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "hash_map", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a set of rectangles forms a perfect rectangle without overlaps or gaps.",
}

def solve(rectangles: list[list[int]]) -> bool:
    """
    Determines if the given rectangles form a perfect rectangle.
    
    A perfect rectangle is formed if:
    1. The sum of the areas of all small rectangles equals the area of the bounding box.
    2. Every corner point within the set of rectangles appears an even number of times, 
       except for the four corners of the bounding box, which must appear exactly once.

    Args:
        rectangles: A list of lists, where each inner list contains [x1, y1, x2, y2]
                    representing the bottom-left and top-right coordinates.

    Returns:
        bool: True if the rectangles form a perfect rectangle, False otherwise.

    Examples:
        >>> solve([[1,1,3,3],[1,1,2,2],[2,2,3,3],[1,2,2,3],[2,1,3,2]])
        True
        >>> solve([[1,1,3,3],[1,1,2,2],[2,2,3,3],[1,2,2,3]])
        False
    """
    if not rectangles:
        return False

    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')
    total_area = 0
    corners = set()

    for x1, y1, x2, y2 in rectangles:
        # Update the bounding box dimensions
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
        
        # Accumulate the area of the current rectangle
        total_area += (x2 - x1) * (y2 - y1)
        
        # Track the frequency of each corner point.
        # If a point is seen twice, it's an internal junction; 
        # if seen once, it's a potential boundary corner.
        # We use a set and toggle: if it exists, remove it; if not, add it.
        for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
            if corner in corners:
                corners.remove(corner)
            else:
                corners.add(corner)

    # Condition 1: The sum of areas must match the area of the bounding box
    bounding_area = (max_x - min_x) * (max_y - min_y)
    if total_area != bounding_area:
        return False

    # Condition 2: There must be exactly 4 corners left in the set,
    # and they must be the four corners of the bounding box.
    expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
    
    return corners == expected_corners