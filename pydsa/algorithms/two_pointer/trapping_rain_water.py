METADATA = {
    "id": 42,
    "name": "Trapping Rain Water",
    "slug": "trapping-rain-water",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "stack", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate how much water can be trapped between bars after raining.",
}

def solve(height: list[int]) -> int:
    """
    Calculates the total amount of trapped rainwater using the two-pointer approach.

    The amount of water at any index is determined by the minimum of the 
    maximum height to the left and the maximum height to the right, 
    minus the height of the current bar.

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
    left_max_height = 0
    right_max_height = 0
    total_water = 0

    while left_index < right_index:
        # We process the side with the smaller height because the water level 
        # is limited by the lower boundary.
        if height[left_index] < height[right_index]:
            if height[left_index] >= left_max_height:
                # Update the maximum height encountered from the left
                left_max_height = height[left_index]
            else:
                # If current height is less than left_max, water is trapped
                total_water += left_max_height - height[left_index]
            left_index += 1
        else:
            if height[right_index] >= right_max_height:
                # Update the maximum height encountered from the right
                right_max_height = height[right_index]
            else:
                # If current height is less than right_max, water is trapped
                total_water += right_max_height - height[right_index]
            right_index -= 1

    return total_water
