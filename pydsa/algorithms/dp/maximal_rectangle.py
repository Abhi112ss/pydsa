METADATA = {
    "id": 85,
    "name": "Maximal Rectangle",
    "slug": "maximal-rectangle",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["stack", "dp", "matrix", "histogram"],
    "difficulty": "hard",
    "time_complexity": "O(rows * cols)",
    "space_complexity": "O(cols)",
    "description": "Find the largest rectangle containing only 1's in a 2D binary matrix.",
}

def solve(matrix: list[list[str]]) -> int:
    """
    Finds the area of the largest rectangle containing only '1's in a 2D binary matrix.

    The algorithm treats each row as the base of a histogram. For each row, we 
    calculate the height of consecutive '1's ending at that row. We then solve 
    the 'Largest Rectangle in Histogram' problem for each row's heights.

    Args:
        matrix: A 2D list of strings representing the binary matrix.

    Returns:
        The area of the largest rectangle found.

    Examples:
        >>> solve([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
        6
        >>> solve([["0"]])
        0
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    # heights array stores the height of consecutive 1s for the current row
    heights = [0] * cols
    max_area = 0

    for row in range(rows):
        for col in range(cols):
            # If current cell is '1', increment height; otherwise, reset to 0
            if matrix[row][col] == "1":
                heights[col] += 1
            else:
                heights[col] = 0
        
        # Calculate the largest rectangle in the histogram formed by the current row
        max_area = max(max_area, _largest_rectangle_in_histogram(heights))

    return max_area

def _largest_rectangle_in_histogram(heights: list[int]) -> int:
    """
    Helper function to find the largest rectangle area in a histogram using a monotonic stack.

    Args:
        heights: A list of non-negative integers representing bar heights.

    Returns:
        The area of the largest rectangle.
    """
    stack = []  # Stores indices of the heights
    max_area = 0
    # Append a 0 height to ensure all bars are popped from the stack at the end
    extended_heights = heights + [0]

    for i, h in enumerate(extended_heights):
        # Maintain a monotonic increasing stack
        while stack and extended_heights[stack[-1]] >= h:
            height = extended_heights[stack.pop()]
            # If stack is empty, width is the current index; 
            # otherwise, width is the distance between current index and new top
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area
