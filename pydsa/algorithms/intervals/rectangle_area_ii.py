METADATA = {
    "id": 850,
    "name": "Rectangle Area II",
    "slug": "rectangle-area-ii",
    "category": "Geometry",
    "aliases": [],
    "tags": ["segment_tree", "line_sweep", "coordinate_compression"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total area covered by a set of potentially overlapping rectangles.",
}

def solve(rectangles: list[list[int]]) -> int:
    """
    Calculates the total area covered by a set of rectangles using a line sweep algorithm.

    Args:
        rectangles: A list of rectangles where each rectangle is [x1, y1, x2, y2].

    Returns:
        The total area covered by the rectangles modulo 10^9 + 7.

    Examples:
        >>> solve([[0,0,2,2],[1,1,3,3]])
        7
        >>> solve([[0,0,1,1],[1,1,2,2]])
        2
    """
    MOD = 10**9 + 7
    
    # Events for the line sweep: (x_coordinate, type, y_bottom, y_top)
    # type 1 for entering a rectangle, -1 for leaving
    events = []
    y_coords = set()
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
        y_coords.add(y1)
        y_coords.add(y2)
    
    # Sort events by x-coordinate
    events.sort()
    
    # Coordinate compression for y-coordinates
    sorted_y = sorted(list(y_coords))
    y_map = {y: i for i, y in enumerate(sorted_y)}
    num_y = len(sorted_y)
    
    # Segment tree to track the length of y-intervals covered
    # count[v] stores how many rectangles cover the interval represented by node v
    # length[v] stores the total length of the interval covered by at least one rectangle
    count = [0] * (4 * num_y)
    length = [0.0] * (4 * num_y)

    def update(v: int, tl: int, tr: int, l: int, r: int, val: int):
        """
        Updates the segment tree for a given y-interval.
        
        Args:
            v: Current node index.
            tl: Left boundary of current node's range in sorted_y index.
            tr: Right boundary of current node's range in sorted_y index.
            l: Left boundary of the update interval.
            r: Right boundary of the update interval.
            val: +1 for adding a rectangle, -1 for removing.
        """
        if l >= r:
            return
        
        if l == tl and r == tr:
            count[v] += val
        else:
            tm = (tl + tr) // 2
            update(2 * v, tl, tm, l, min(r, tm), val)
            update(2 * v + 1, tm, tr, max(l, tm), r, val)
        
        # If count[v] > 0, the entire interval [sorted_y[tl], sorted_y[tr]] is covered
        if count[v] > 0:
            length[v] = sorted_y[tr] - sorted_y[tl]
        else:
            # Otherwise, the length is the sum of lengths of its children
            if tr - tl > 1:
                length[v] = length[2 * v] + length[2 * v + 1]
            else:
                length[v] = 0

    total_area = 0
    prev_x = events[0][0]
    
    for x, type_val, y1, y2 in events:
        # Calculate area added since the last x-coordinate
        # Area = (current_x - previous_x) * current_covered_y_length
        width = x - prev_x
        total_area += width * length[1]
        
        # Update the segment tree with the new y-interval
        update(1, 0, num_y - 1, y_map[y1], y_map[y2], type_val)
        prev_x = x
        
    return int(total_area % MOD)
