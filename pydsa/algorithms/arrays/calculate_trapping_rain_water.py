METADATA = {
    "id": 3061,
    "name": "Trapping Rain Water",
    "slug": "trapping_rain_water",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "prefix_sum", "monotonic_stack"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total amount of water trapped between bars after raining.",
}

def solve(height: list[int]) -> int:
    """
    Calculates the total amount of trapped rainwater using the two-pointer approach.

    The amount of water at any given position is determined by the minimum of the 
    maximum height to its left and the maximum height to its right, minus the 
    height of the current bar. By using two pointers moving towards each other, 
    we can maintain the necessary boundary information in O(1) space.

    Args:
        height: A list of non-negative integers representing the elevation map.

    Returns:
        The total units of water trapped.

    Examples:
        >>> solve([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        >>> solve([4,2,0,3,2,5])
        9
    """
    if not height:
        return 0

    left_index = 0
    right_index = len(height) - 1
    left_max = 0
    right_max = 0
    total_water = 0

    while left_index < right_index:
        # We process the side with the smaller boundary height because the 
        # water level is limited by the lower of the two sides.
        if height[left_index] < height[right_index]:
            if height[left_index] >= left_max:
                # Update the maximum height encountered from the left
                left_max = height[left_index]
            else:
                # The current height is less than the left_max, so water is trapped
                total_water += left_max - height[left_index]
            left_index += 1
        else:
            if height[right_index] >= right_max:
                # Update the maximum height encountered from the right
                right_max = height[right_index]
            else:
                # The current height is less than the right_max, so water is trapped
                total_water += right_max - height[right_index]
            right_index -= 1

    return total_water
