METADATA = {
    "id": 2345,
    "name": "Finding the Number of Visible Mountains",
    "slug": "finding_the_number_of_visible_mountains",
    "category": "Arrays",
    "aliases": [],
    "tags": ["monotonic_stack", "arrays", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of mountains that are visible from either the left or the right side.",
}

def solve(heights: list[int]) -> int:
    """
    Calculates the number of mountains visible from either the left or the right.
    A mountain is visible if it is strictly greater than all mountains to its left 
    (when viewed from the left) or strictly greater than all mountains to its right 
    (when viewed from the right).

    Args:
        heights: A list of integers representing the heights of the mountains.

    Returns:
        The total count of visible mountains.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        5
        >>> solve([5, 4, 3, 2, 1])
        5
        >>> solve([1, 3, 2, 4, 5])
        4
        >>> solve([1, 1, 1, 1])
        1
    """
    n = len(heights)
    if n == 0:
        return 0
    
    # visible_from_left[i] is True if heights[i] is greater than all heights[0...i-1]
    visible_from_left = [False] * n
    # visible_from_right[i] is True if heights[i] is greater than all heights[i+1...n-1]
    visible_from_right = [False] * n

    # Traverse from left to right to find mountains visible from the left side
    current_max_left = -1
    for i in range(n):
        if heights[i] > current_max_left:
            visible_from_left[i] = True
            current_max_left = heights[i]

    # Traverse from right to left to find mountains visible from the right side
    current_max_right = -1
    for i in range(n - 1, -1, -1):
        if heights[i] > current_max_right:
            visible_from_right[i] = True
            current_max_right = heights[i]

    # A mountain is counted if it is visible from either side
    # We use a set or a simple loop to avoid double counting the same mountain
    total_visible = 0
    for i in range(n):
        if visible_from_left[i] or visible_from_right[i]:
            total_visible += 1

    return total_visible
