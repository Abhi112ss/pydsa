METADATA = {
    "id": 1504,
    "name": "Count Submatrices With All Ones",
    "slug": "count-submatrices-with-all-ones",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["matrix", "monotonic stack", "dynamic programming"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n)",
    "description": "Count the number of submatrices that consist entirely of ones.",
}

def solve(matrix: list[list[int]]) -> int:
    """
    Counts the total number of submatrices containing only ones.

    The algorithm treats each row as the base of a histogram where the height 
    of each column is the number of consecutive ones ending at that row. 
    For each row, we use a monotonic stack to efficiently calculate the 
    number of submatrices ending at that specific row in O(n) time.

    Args:
        matrix: A 2D list of integers (0 or 1).

    Returns:
        The total count of submatrices containing only ones.

    Examples:
        >>> solve([[1,0,1],[1,1,0],[1,1,0]])
        13
        >>> solve([[0]])
        0
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    
    # heights[j] stores the number of consecutive 1s ending at the current row for column j
    heights = [0] * cols
    total_submatrices = 0

    for r in range(rows):
        # Update heights for the current row (histogram approach)
        for c in range(cols):
            if matrix[r][c] == 1:
                heights[c] += 1
            else:
                heights[c] = 0
        
        # count_at_row[c] stores the number of submatrices whose bottom-right corner is (r, c)
        # We use a monotonic stack to find the nearest column to the left with a smaller height
        count_at_row = [0] * cols
        stack = []  # Stores indices of columns in increasing order of heights

        for c in range(cols):
            # Pop elements from stack that are taller than or equal to current height
            while stack and heights[stack[-1]] >= heights[c]:
                stack.pop()
            
            if stack:
                # If stack is not empty, the nearest smaller height is at index 'prev_idx'
                # Submatrices ending at 'c' can be split into:
                # 1. Those limited by the height of the current column 'c' spanning from 'prev_idx + 1' to 'c'
                # 2. Those that are identical to the submatrices ending at 'prev_idx'
                prev_idx = stack[-1]
                width = c - prev_idx
                count_at_row[c] = (heights[c] * width) + count_at_row[prev_idx]
            else:
                # If no smaller height exists to the left, all columns from 0 to c 
                # can form submatrices of height 'heights[c]'
                count_at_row[c] = heights[c] * (c + 1)
            
            stack.append(c)
            total_submatrices += count_at_row[c]

    return total_submatrices
