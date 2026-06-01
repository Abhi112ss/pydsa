METADATA = {
    "id": 2579,
    "name": "Count Total Number of Colored Cells",
    "slug": "count-total-number-of-colored-cells",
    "category": "Array",
    "aliases": [],
    "tags": ["intervals", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of colored cells by counting the length of continuous colored segments.",
}

def solve(colors: list[int]) -> int:
    """
    Calculates the total number of colored cells in a row.
    
    A cell is colored if it is part of a continuous sequence of non-zero 
    integers. The length of a sequence is the number of elements in it 
    plus the two boundary cells (one on each side) if they are not already 
    part of another sequence.

    Args:
        colors: A list of integers where 0 represents an uncolored cell 
                and non-zero represents a colored cell.

    Returns:
        The total number of colored cells.

    Examples:
        >>> solve([1, 1, 0, 1, 1])
        6
        >>> solve([0, 2, 2, 0, 3, 3, 3, 0])
        8
        >>> solve([0, 0, 0])
        0
    """
    total_cells = 0
    n = len(colors)
    i = 0

    while i < n:
        # Skip uncolored cells
        if colors[i] == 0:
            i += 1
            continue
        
        # We found the start of a colored segment
        segment_start = i
        
        # Find the end of this continuous colored segment
        while i < n and colors[i] != 0:
            i += 1
        segment_end = i - 1
        
        # The number of colored cells in this segment is (end - start + 1)
        # We must also add the two boundary cells (left and right)
        # unless they are out of bounds.
        
        # Length of the current continuous block
        current_segment_length = segment_end - segment_start + 1
        
        # Add the segment length plus 2 for the boundaries
        # We use a logic that effectively counts the segment and its neighbors
        # without double counting by treating the segment as [start-1, end+1]
        total_cells += current_segment_length + 2
        
        # Adjust for boundaries: if the segment touches the edge of the array,
        # the 'neighbor' cell doesn't exist, so we subtract 1 for each edge.
        if segment_start == 0:
            total_cells -= 1
        if segment_end == n - 1:
            total_cells -= 1
            
    return total_cells
