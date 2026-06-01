METADATA = {
    "id": 2250,
    "name": "Count Number of Rectangles Containing Each Point",
    "slug": "count-number-of-rectangles-containing-each-point",
    "category": "Math",
    "aliases": [],
    "tags": ["binary_search", "sorting", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Count how many rectangles formed by points (0,0) and (x_i, y_i) contain each given point (x_j, y_j).",
}

def solve(points: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Calculates the number of rectangles containing each query point.
    
    A rectangle is defined by the origin (0,0) and a point (x, y) from the points list.
    A query point (qx, qy) is contained in a rectangle (0,0) to (x, y) if 
    qx <= x and qy <= y.

    Args:
        points: A list of [x, y] coordinates defining the top-right corners of rectangles.
        queries: A list of [qx, qy] coordinates to check.

    Returns:
        A list of integers where the i-th integer is the count of rectangles 
        containing the i-th query point.

    Examples:
        >>> solve([[1,1],[2,2]], [[1,1]])
        [2]
        >>> solve([[1,1],[2,2]], [[2,2]])
        [1]
    """
    # Sort points by x-coordinate ascending. 
    # If x is same, sort by y-coordinate ascending.
    points.sort()
    
    # Extract sorted x-coordinates for binary search
    sorted_x = [p[0] for p in points]
    
    # To efficiently count how many points have y >= qy among those with x >= qx,
    # we can pre-process the y-coordinates.
    # However, the condition is: x_i >= qx AND y_i >= qy.
    # Since points are sorted by x, for a given qx, all points from index 'idx' 
    # to len(points)-1 satisfy x_i >= qx.
    # Among these points, we need to count how many have y_i >= qy.
    
    # We use a suffix maximum or a sorted structure. 
    # But wait, the condition is simply: for all i where points[i].x >= qx, 
    # count how many points[i].y >= qy.
    
    # Let's refine:
    # 1. Sort points by x.
    # 2. For a query (qx, qy):
    #    Find the smallest index 'i' such that points[i].x >= qx using binary search.
    #    All points from index 'i' to N-1 satisfy the x-condition.
    #    We need to count how many of these points have y >= qy.
    
    # To do this efficiently for multiple queries, we can use a Fenwick tree 
    # or simply process queries offline. 
    # Alternatively, since we only need to count y >= qy in a suffix of the sorted x-array,
    # we can use a Fenwick tree on the y-coordinates.
    
    # Coordinate compression for y-coordinates to use in Fenwick Tree
    all_y = sorted(list(set(p[1] for p in points) | set(q[1] for q in queries)))
    y_map = {y: i + 1 for i, y in enumerate(all_y)}
    max_y_idx = len(all_y)
    
    # Fenwick Tree (Binary Indexed Tree) to store counts of y-coordinates
    bit = [0] * (max_y_idx + 1)

    def update(idx: int, val: int):
        while idx <= max_y_idx:
            bit[idx] += val
            idx += idx & (-idx)

    def query_bit(idx: int) -> int:
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & (-idx)
        return s

    # Sort queries by x-coordinate descending to use a sweep-line approach
    # We want to add points to the BIT as their x becomes >= qx.
    # Actually, it's easier to sort queries by x descending and points by x descending.
    
    indexed_queries = []
    for i, (qx, qy) in enumerate(queries):
        indexed_queries.append((qx, qy, i))
    
    # Sort queries by x descending
    indexed_queries.sort(key=lambda x: x[0], reverse=True)
    # Sort points by x descending
    points.sort(key=lambda x: x[0], reverse=True)
    
    results = [0] * len(queries)
    point_idx = 0
    n = len(points)
    
    for qx, qy, original_idx in indexed_queries:
        # Add all points whose x >= qx into the BIT
        while point_idx < n and points[point_idx][0] >= qx:
            update(y_map[points[point_idx][1]], 1)
            point_idx += 1
        
        # Count points in BIT where y >= qy
        # This is (total points added so far) - (points with y < qy)
        total_added = point_idx
        count_y_less_than_qy = query_bit(y_map[qy] - 1)
        results[original_idx] = total_added - count_y_less_than_qy
        
    return results
