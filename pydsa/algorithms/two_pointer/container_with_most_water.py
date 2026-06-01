METADATA = {
    "id": 11,
    "name": "Container With Most Water",
    "slug": "container-with-most-water",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find two lines that together with the x-axis form a container, such that the container contains the most water.",
}

def solve(height: list[int]) -> int:
    """
    Calculates the maximum area of water a container can hold.

    The algorithm uses a two-pointer approach, starting from both ends of the 
    array and moving the pointer pointing to the shorter line inward to 
    potentially find a taller line that increases the area.

    Args:
        height: A list of integers representing the heights of vertical lines.

    Returns:
        The maximum area of water that can be contained.

    Examples:
        >>> solve([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        >>> solve([1, 1])
        1
    """
    left_index = 0
    right_index = len(height) - 1
    max_area = 0

    while left_index < right_index:
        # The height of the container is limited by the shorter of the two lines
        current_height = min(height[left_index], height[right_index])
        
        # The width is the distance between the two pointers
        current_width = right_index - left_index
        
        # Calculate current area and update max_area if current is larger
        current_area = current_height * current_width
        if current_area > max_area:
            max_area = current_area

        # Move the pointer pointing to the shorter line inward.
        # Moving the taller line would only decrease the width without 
        # any possibility of increasing the height of the container.
        if height[left_index] < height[right_index]:
            left_index += 1
        else:
            right_index -= 1

    return max_area
