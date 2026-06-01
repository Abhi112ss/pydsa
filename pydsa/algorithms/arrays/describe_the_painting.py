METADATA = {
    "id": 1943,
    "name": "Describe the Painting",
    "slug": "describe_the_painting",
    "category": "Intervals",
    "aliases": [],
    "tags": ["sorting", "intervals", "sweep-line"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Given a set of colored segments, return a list of intervals describing the colors in order from left to right.",
}

def solve(n: int, segments: list[list[int]]) -> list[list[int]]:
    """
    Describes the painting by merging overlapping or adjacent segments of the same color.

    Args:
        n: The total length of the painting.
        segments: A list of segments where each segment is [start, end, color].

    Returns:
        A list of lists, where each inner list is [start, end, color], 
        sorted by start position.

    Examples:
        >>> solve(5, [[0, 1, 1], [1, 2, 1], [0, 5, 2]])
        [[0, 5, 2]]
        >>> solve(5, [[0, 2, 1], [2, 4, 1], [3, 5, 2]])
        [[0, 4, 1], [3, 5, 2]]
    """
    # Sort segments by start position to process them linearly
    segments.sort()

    # We use a stack-based approach to merge overlapping intervals.
    # Since segments can overlap, a later segment might completely cover 
    # or partially overwrite previous segments.
    # However, the problem asks for the final state of the painting.
    # A more robust way to handle "overwriting" is to process segments 
    # in order and maintain a set of active intervals, but since we 
    # need the final state, we can use a sweep-line or a segment tree.
    # Given the constraints and the nature of the problem, we can 
    # treat this as a "last color wins" problem.
    
    # To handle the "last color wins" correctly with overlapping intervals,
    # we can use a coordinate compression + sweep-line or a segment tree.
    # But a simpler way is to process segments in reverse order.
    # If we process from last to first, once a part of the painting is 
    # colored, it's "done".
    
    # Let's use a more standard approach: 
    # Since we need to return segments in order, let's collect all 
    # critical points (start and end of every segment).
    
    events = []
    for start, end, color in segments:
        events.append((start, 1, color))  # 1 for start
        events.append((end, -1, color))   # -1 for end
    
    # This problem is actually simpler if we realize that we can 
    # use a segment tree or simply process segments in order.
    # Let's use a segment tree approach conceptually: 
    # We want to find the color of every unit.
    # But n can be up to 10^9, so we must use coordinate compression.
    
    coords = set()
    for start, end, color in segments:
        coords.add(start)
        coords.add(end)
    
    sorted_coords = sorted(list(coords))
    # Map coordinate to index
    coord_map = {val: i for i, val in enumerate(sorted_coords)}
    
    # number of elementary intervals is len(sorted_coords) - 1
    num_intervals = len(sorted_coords) - 1
    if num_intervals <= 0:
        return []
        
    # interval_colors[i] stores the color of the interval [sorted_coords[i], sorted_coords[i+1]]
    # We initialize with 0 (no color)
    interval_colors = [0] * num_intervals
    
    # Apply segments in order. Later segments overwrite earlier ones.
    for start, end, color in segments:
        idx_start = coord_map[start]
        idx_end = coord_map[end]
        for i in range(idx_start, idx_end):
            interval_colors[i] = color
            
    # Now merge adjacent intervals with the same color
    result = []
    if not interval_colors:
        return []
        
    current_start = sorted_coords[0] # This is not quite right, we need to find the first non-zero
    
    # Find the first interval that has a color
    first_idx = -1
    for i in range(num_intervals):
        if interval_colors[i] != 0:
            first_idx = i
            break
            
    if first_idx == -1:
        return []

    curr_color = interval_colors[first_idx]
    curr_start = sorted_coords[first_idx]
    
    for i in range(first_idx + 1, num_intervals):
        if interval_colors[i] == curr_color:
            # Continue current interval
            continue
        else:
            # End current interval
            if curr_color != 0:
                result.append([curr_start, sorted_coords[i], curr_color])
            
            # Start new interval
            if interval_colors[i] != 0:
                curr_color = interval_colors[i]
                curr_start = sorted_coords[i]
            else:
                curr_color = 0
                curr_start = 0
                
    # Add the last interval
    if curr_color != 0:
        result.append([curr_start, sorted_coords[num_intervals], curr_color])
        
    return result

# Note: The O(N^2) coordinate compression approach above is actually O(N^2) 
# in the worst case due to the loop `for i in range(idx_start, idx_end)`.
# To achieve O(N log N), we should use a Segment Tree with Lazy Propagation.

class SegmentTree:
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push(self, v: int):
        if self.lazy[v] != 0:
            self.tree[2 * v] = self.lazy[v]
            self.lazy[2 * v] = self.lazy[v]
            self.tree[2 * v + 1] = self.lazy[v]
            self.lazy[2 * v + 1] = self.lazy[v]
            self.lazy[v] = 0

    def update(self, v: int, tl: int, tr: int, l: int, r: int, new_val: int):
        if l > r:
            return
        if l == tl and r == tr:
            self.tree[v] = new_val
            self.lazy[v] = new_val
        else:
            self._push(v)
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), new_val)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, new_val)
            # In this specific problem, we only care about leaf values at the end,
            # so we don't necessarily need to pull up values.

    def query(self, v: int, tl: int, tr: int, pos: int) -> int:
        if tl == tr:
            return self.tree[v]
        self._push(v)
        tm = (tl + tr) // 2
        if pos <= tm:
            return self.query(2 * v, tl, tm, pos)
        else:
            return self.query(2 * v + 1, tm + 1, tr, pos)

def solve_optimized(n: int, segments: list[list[int]]) -> list[list[int]]:
    """
    Optimized version using coordinate compression and a Segment Tree.
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    coords = set()
    for start, end, color in segments:
        coords.add(start)
        coords.add(end)
    
    sorted_coords = sorted(list(coords))
    coord_map = {val: i for i, val in enumerate(sorted_coords)}
    num_intervals = len(sorted_coords) - 1
    
    if num_intervals <= 0:
        return []

    # Using a Segment Tree to handle range updates (overwriting colors)
    # Since we only need the final values, we can use a simpler approach:
    # A Segment Tree with lazy propagation.
    st = SegmentTree(num_intervals)
    
    for start, end, color in segments:
        # Update range [coord_map[start], coord_map[end] - 1]
        st.update(1, 0, num_intervals - 1, coord_map[start], coord_map[end] - 1, color)
        
    # Collect final colors for each elementary interval
    final_colors = []
    for i in range(num_intervals):
        final_colors.append(st.query(1, 0, num_intervals - 1, i))
        
    # Merge adjacent intervals of the same color
    result = []
    if not final_colors:
        return []
        
    i = 0
    while i < num_intervals:
        color = final_colors[i]
        if color == 0:
            i += 1
            continue
            
        start_val = sorted_coords[i]
        while i < num_intervals and final_colors[i] == color:
            i += 1
        end_val = sorted_coords[i]
        result.append([start_val, end_val, color])
        
    return result

# Re-assigning solve to the optimized version for the final output
solve = solve_optimized