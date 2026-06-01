METADATA = {
    "id": 84,
    "name": "Largest Rectangle in Histogram",
    "slug": "largest-rectangle-in-histogram",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "monotonic_stack", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the area of the largest rectangle in a histogram where each bar has a width of 1.",
}

def solve(heights: list[int]) -> int:
    """
    Calculates the area of the largest rectangle in a histogram using a monotonic stack.

    The algorithm maintains a stack of indices where the heights of the bars 
    at these indices are in non-decreasing order. When a bar is encountered 
    that is shorter than the bar at the stack's top, it means we have found 
    the right boundary for the rectangle formed by the bar at the stack's top.

    Args:
        heights: A list of integers representing the heights of bars in a histogram.

    Returns:
        The area of the largest rectangle possible.

    Examples:
        >>> solve([2, 1, 5, 6, 2, 3])
        10
        >>> solve([2])
        2
        >>> solve([2, 4])
        4
    """
    # Append a zero height to the end to ensure all remaining bars in the stack 
    # are processed and popped at the end of the loop.
    heights_with_sentinel = heights + [0]
    stack: list[int] = []
    max_area: int = 0

    for current_index, current_height in enumerate(heights_with_sentinel):
        # While the current bar is shorter than the bar at the top of the stack,
        # the bar at the top of the stack has found its right boundary.
        while stack and heights_with_sentinel[stack[-1]] > current_height:
            # Height of the rectangle is the height of the bar we are popping.
            height_to_calculate = heights_with_sentinel[stack.pop()]
            
            # The width is determined by the distance between the current index 
            # (right boundary) and the new top of the stack (left boundary).
            # If stack is empty, the width extends all the way to the start.
            if not stack:
                width = current_index
            else:
                width = current_index - stack[-1] - 1
            
            max_area = max(max_area, height_to_calculate * width)
            
        stack.append(current_index)

    return max_area
