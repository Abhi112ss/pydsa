METADATA = {
    "id": 750,
    "name": "Number Of Corner Rectangles",
    "slug": "number-of-corner-rectangles",
    "category": "Matrix",
    "aliases": [],
    "tags": ["dp", "math", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(R * C^2)",
    "space_complexity": "O(C^2)",
    "description": "Count the number of rectangles formed by four 1s in a binary matrix.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Counts the number of rectangles formed by four 1s in a binary matrix.
    
    A rectangle is defined by four cells (r1, c1), (r1, c2), (r2, c1), (r2, c2)
    where all four cells contain the value 1.

    Args:
        matrix: A 2D list of integers representing the binary matrix.

    Returns:
        The total number of corner rectangles found.

    Examples:
        >>> solve([[1,1,1],[1,1,1],[1,1,1]])
        9
        >>> solve([[1,0,1],[0,0,0],[1,0,1]])
        1
    """
    rows = len(matrix)
    cols = len(matrix[0])
    total_rectangles = 0
    
    # pair_counts[c1][c2] stores how many times we have seen 
    # a pair of 1s at columns c1 and c2 in previous rows.
    pair_counts = [[0] * cols for _ in range(cols)]

    for r in range(rows):
        # Find all pairs of columns (c1, c2) that both have a 1 in the current row.
        # We only care about c1 < c2 to avoid double counting and self-pairing.
        current_row_pairs = []
        for c1 in range(cols):
            if matrix[r][c1] == 1:
                for c2 in range(c1 + 1, cols):
                    if matrix[r][c2] == 1:
                        current_row_pairs.append((c1, c2))
        
        # For every pair found in the current row, the number of rectangles 
        # it can form is equal to the number of times this specific pair 
        # (c1, c2) has appeared in previous rows.
        for c1, c2 in current_row_pairs:
            total_rectangles += pair_counts[c1][c2]
            # Increment the count for this pair to be used by future rows.
            pair_counts[c1][c2] += 1
            
    return total_rectangles
