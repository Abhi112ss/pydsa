METADATA = {
    "id": 1072,
    "name": "Flip Columns For Maximum Number of Equal Rows",
    "slug": "flip-columns-for-maximum-number-of-equal-rows",
    "category": "Matrix",
    "aliases": [],
    "tags": ["hash_map", "matrix", "bit-manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(r * c)",
    "space_complexity": "O(r)",
    "description": "Find the maximum number of rows that can be made equal by flipping columns.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Finds the maximum number of rows that can be made equal by flipping columns.
    
    Two rows can be made equal if they are identical or if one is the bitwise 
    complement of the other. We normalize each row by treating it as a 
    binary number and comparing it to its complement.

    Args:
        matrix: A 2D list of integers representing the binary matrix.

    Returns:
        The maximum number of rows that can be made equal.

    Examples:
        >>> solve([[0,0,1,1],[1,1,0,0],[1,0,1,0]])
        2
        >>> solve([[0,1],[1,0]])
        2
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Frequency map to store the count of each unique row pattern
    pattern_counts: dict[int, int] = {}

    for row in matrix:
        # Convert the row into a single integer representation
        row_value = 0
        for bit in row:
            row_value = (row_value << 1) | bit
        
        # To handle the "complement" case, we normalize the row.
        # We can do this by ensuring the row_value is always the smaller 
        # of the two possible patterns (the value and its complement).
        # The complement of a number 'x' with 'cols' bits is (2^cols - 1) ^ x.
        complement_value = ((1 << cols) - 1) ^ row_value
        
        # Use the minimum of the two patterns as the canonical key
        canonical_pattern = min(row_value, complement_value)
        
        # Increment the count for this canonical pattern
        pattern_counts[canonical_pattern] = pattern_counts.get(canonical_pattern, 0) + 1

    # The answer is the maximum frequency found in our map
    return max(pattern_counts.values()) if pattern_counts else 0
