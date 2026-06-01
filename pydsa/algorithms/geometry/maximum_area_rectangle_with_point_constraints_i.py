METADATA = {
    "id": 3380,
    "name": "Maximum Area Rectangle With Point Constraints I",
    "slug": "maximum-area-rectangle-with-point-constraints-i",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "two_pointer", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum area of a rectangle formed by four points from a given set such that no other points lie inside or on the boundary of the rectangle.",
}

def solve(points: list[list[int]]) -> int:
    """
    Finds the maximum area of a rectangle formed by four points from the given set
    such that no other points lie inside or on the boundary of the rectangle.

    Args:
        points: A list of [x, y] coordinates representing points in a 2D plane.

    Returns:
        The maximum area of a valid rectangle. Returns 0 if no such rectangle exists.

    Examples:
        >>> solve([[0,0], [0,1], [1,0], [1,1], [0.5, 0.5]])
        0
        >>> solve([[0,0], [0,2], [2,0], [2,2], [1,1]])
        0
        >>> solve([[0,0], [0,1], [1,0], [1,1]])
        1
    """
    n = len(points)
    if n < 4:
        return 0

    # Convert points to a set for O(1) lookup
    point_set = set((p[0], p[1]) for p in points)
    max_area = 0

    # Sort points to allow for structured iteration (optional but helps in some geometric approaches)
    # For O(n^2), we iterate through pairs of points that could be diagonal corners
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            # A rectangle with sides parallel to axes is defined by two diagonal points
            # (x1, y1) and (x2, y2). They must not share the same x or y coordinate.
            if x1 == x2 or y1 == y2:
                continue

            # Check if the other two corners of the axis-aligned rectangle exist
            # Corner 3: (x1, y2), Corner 4: (x2, y1)
            if (x1, y2) in point_set and (x2, y1) in point_set:
                current_area = abs(x1 - x2) * abs(y1 - y2)
                
                # To ensure no other points are inside or on the boundary,
                # we must check all points. However, the problem constraints 
                # for "Constraints I" often imply a specific search space.
                # For a general O(n^2) approach, we check if any point k is inside.
                is_valid = True
                
                # Define bounds for the rectangle
                min_x, max_x = min(x1, x2), max(x1, x2)
                min_y, max_y = min(y1, y2), max(y1, y2)

                # Check all points to see if any lie within the rectangle's bounds
                # Note: The problem asks for no points inside OR on the boundary.
                # Since we already know the 4 corners exist, we check if any OTHER point is inside.
                for k in range(n):
                    px, py = points[k]
                    # If the point is one of the 4 corners, skip it
                    if (px == x1 and py == y1) or (px == x2 and py == y2) or \
                       (px == x1 and py == y2) or (px == x2 and py == y1):
                        continue
                    
                    # Check if point k is within the closed rectangle [min_x, max_x] x [min_y, max_y]
                    if min_x <= px <= max_x and min_y <= py <= max_y:
                        is_valid = False
                        break
                
                if is_valid:
                    max_area = max(max_area, current_area)

    return max_area
