METADATA = {
    "id": 861,
    "name": "Score After Flipping Matrix",
    "slug": "score-after-flipping-matrix",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "matrix", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(R * C)",
    "space_complexity": "O(1)",
    "description": "Maximize the sum of a binary matrix by flipping rows and columns, where the sum is calculated as the sum of values of each row interpreted as a binary number.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Calculates the maximum possible score of a binary matrix after any number of row and column flips.
    
    The score is defined as the sum of the values of each row interpreted as a binary number.
    To maximize this, we follow a greedy approach:
    1. Ensure the first column is all 1s by flipping rows.
    2. For the remaining columns, flip the column if it contains more 0s than 1s.

    Args:
        matrix: A 2D list of integers (0 or 1).

    Returns:
        The maximum possible score.

    Examples:
        >>> solve([[0, 0, 1], [1, 0, 1], [1, 1, 0]])
        8
        >>> solve([[0, 1], [1, 0]])
        3
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Ensure the first column is all 1s.
    # If a cell in the first column is 0, flip the entire row.
    for r in range(rows):
        if matrix[r][0] == 0:
            for c in range(cols):
                matrix[r][c] = 1 - matrix[r][c]

    # Step 2: For each column from index 1 to cols-1, 
    # flip the column if the number of 0s is greater than the number of 1s.
    for c in range(1, cols):
        count_ones = 0
        for r in range(rows):
            if matrix[r][c] == 1:
                count_ones += 1
        
        # If 0s outnumber 1s, flip the column
        if count_ones < (rows / 2):
            for r in range(rows):
                matrix[r][c] = 1 - matrix[r][c]

    # Step 3: Calculate the final score.
    # Each row is treated as a binary number.
    total_score = 0
    for r in range(rows):
        row_value = 0
        for c in range(cols):
            # Shift left and add the current bit
            row_value = (row_value << 1) | matrix[r][c]
        total_score += row_value

    return total_score
