METADATA = {
    "id": 963,
    "name": "Minimum Area Rectangle II",
    "slug": "minimum-area-rectangle-ii",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "hash_map"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum area of a rectangle formed by four points from a given set of points in a 2D plane.",
}

def solve(points: list[list[int]]) -> int:
    """
    Args:
        points: A list of lists where each sub-list contains two integers representing coordinates.

    Returns:
        The minimum area of a rectangle formed by four points, or 0 if no such rectangle exists.
    """
    midpoint_map = {}
    min_area = float('inf')

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            mid_x_2 = x1 + x2
            mid_y_2 = y1 + y2
            dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2

            key = (mid_x_2, mid_y_2, dist_sq)

            if key in midpoint_map:
                for other_point_idx in midpoint_map[key]:
                    x3, y3 = points[other_point_idx]
                    x4, y4 = points[i if j == other_point_idx else j] 
                    
                    # Since we know the diagonals share the same midpoint and length,
                    # the four points form a rectangle. We need to find the area.
                    # The area of a rectangle with diagonals (x1,y1)-(x2,y2) and (x3,y3)-(x4,y4)
                    # can be calculated using the side lengths.
                    # Side 1: distance between (x1, y1) and (x3, y3)
                    # Side 2: distance between (x1, y1) and (x4, y4)
                    # However, we need to identify which point is which. 
                    # Let's use the property that the area is |(x1-x3)(y1-y4) - (x1-x4)(y1-y3)| 
                    # for a rectangle where (x1,y1) and (x2,y2) are opposite vertices.
                    # But a simpler way: Area = |(x1-x3)*(y1-y4) - (x1-x4)*(y1-y3)| is for any quadrilateral.
                    # For a rectangle, we can just use the distance between adjacent vertices.
                    
                    # Let's pick one point from the first diagonal (points[i]) 
                    # and one from the second (points[other_point_idx]).
                    # The distance between them is one side.
                    # The distance between points[i] and the remaining point (points[j]) is the other side.
                    # Wait, points[j] is the other end of the first diagonal.
                    # The four points are points[i], points[j], points[other_point_idx], and the 4th point.
                    # The 4th point is implicitly defined by the midpoint.
                    # Let's find the 4th point: x4 = mid_x_2 - x3, y4 = mid_y_2 - y3.
                    
                    x3, y3 = points[other_point_idx]
                    x4 = mid_x_2 - x3
                    y4 = mid_y_2 - y3
                    
                    # Area of rectangle with vertices (x1,y1), (x3,y3), (x2,y2), (x4,y4)
                    # is the absolute value of the cross product of vectors (x3-x1, y3-y1) and (x4-x1, y4-y1)
                    # No, that's for a triangle. Area = 2 * Area of triangle.
                    # Area = |(x1-x3)*(y1-y4) - (x1-x4)*(y1-y3)| is not quite right for all orientations.
                    # Let's use: Area = sqrt(dist(p1, p3)^2 * dist(p1, p4)^2) is wrong.
                    # Correct: Area = |(x1-x3)*(y1-y4) - (x1-x4)*(y1-y3)| is actually the area of the parallelogram.
                    # Since it's a rectangle, this works.
                    
                    area = abs((x1 - x3) * (y1 - y4) - (x1 - x4) * (y1 - y3))
                    if area > 0:
                        min_area = min(min_area, area)
                
                midpoint_map[key].append(i)
                midpoint_map[key].append(j)
            else:
                midpoint_map[key] = [i, j]

    return int(min_area) if min_area != float('inf') else 0