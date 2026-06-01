METADATA = {
    "id": 469,
    "name": "Convex Polygon",
    "slug": "convex-polygon",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given list of points forms a convex polygon.",
}

def solve(points: list[list[int]]) -> bool:
    """
    Determines if the given sequence of points forms a convex polygon.
    
    A polygon is convex if all interior angles are less than 180 degrees.
    In terms of cross products, this means that as we traverse the edges,
    the direction of the turn (left or right) must remain consistent.

    Args:
        points: A list of [x, y] coordinates representing the vertices of the polygon.

    Returns:
        True if the polygon is convex, False otherwise.

    Examples:
        >>> solve([[0,0],[0,1],[1,1],[1,0]])
        True
        >>> solve([[0,0],[0,1],[1,1],[0,0]])
        False
    """
    n = len(points)
    if n < 3:
        return False

    def get_cross_product(o: list[int], a: list[int], b: list[int]) -> int:
        """
        Calculates the 2D cross product of vectors (a-o) and (b-o).
        The sign tells us if the turn is clockwise or counter-clockwise.
        """
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    prev_sign = 0
    
    for i in range(n):
        # Get three consecutive points: p1, p2, p3
        # We use modulo to wrap around the list for the last edges
        p1 = points[i]
        p2 = points[(i + 1) % n]
        p3 = points[(i + 2) % n]
        
        cp = get_cross_product(p1, p2, p3)
        
        # If cp is 0, the points are collinear, which is allowed in some 
        # definitions of convexity, but usually, we just skip it.
        if cp != 0:
            current_sign = 1 if cp > 0 else -1
            
            # If we have seen a turn in the opposite direction, it's concave
            if prev_sign != 0 and current_sign != prev_sign:
                return False
            
            prev_sign = current_sign

    return True
