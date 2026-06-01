METADATA = {
    "id": 699,
    "name": "Falling Squares",
    "slug": "falling-squares",
    "category": "Intervals",
    "aliases": [],
    "tags": ["segment_tree", "interval", "coordinate compression"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Simulate falling squares and find the maximum height reached at any point.",
}

def solve(positions: list[list[int]]) -> int:
    """
    Simulates the falling of squares and tracks the maximum height.

    Args:
        positions: A list of lists where each sublist contains [left, right, side].
                   left and right define the horizontal interval, side is the vertical height.

    Returns:
        The maximum height reached by any square during the simulation.

    Examples:
        >>> solve([[1, 2, 45], [8, 10, 30], [1, 10, 20]])
        65
        >>> solve([[1, 2, 1], [1, 2, 1], [1, 2, 1]])
        3
    """
    # intervals stores tuples of (left, right, current_height)
    # We use this to track the vertical stack of squares at specific horizontal ranges.
    intervals: list[tuple[int, int, int]] = []
    max_height = 0

    for left, right, side in positions:
        current_base_height = 0
        
        # Find the maximum height currently occupied within the [left, right) range
        # to determine where the new square will land.
        for i_left, i_right, i_height in intervals:
            # Check if the new square's interval overlaps with an existing interval
            if left < i_right and right > i_left:
                current_base_height = max(current_base_height, i_height)
        
        # The new height of the square after it lands
        new_height = current_base_height + side
        intervals.append((left, right, new_height))
        
        # Update the global maximum height encountered so far
        max_height = max(max_height, new_height)

    return max_height
