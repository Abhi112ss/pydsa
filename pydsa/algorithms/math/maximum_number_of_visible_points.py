METADATA = {
    "id": 1610,
    "name": "Maximum Number of Visible Points",
    "slug": "maximum-number-of-visible-points",
    "category": "Math",
    "aliases": [],
    "tags": ["sliding_window", "math", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of points visible from a given position within a specific field of view angle.",
}

import math

def solve(points: list[list[int]], position: list[int], angle: float) -> int:
    """
    Calculates the maximum number of points visible from a position within a given angle.

    Args:
        points: A list of [x, y] coordinates representing the points.
        position: A list [x, y] representing the observer's position.
        angle: The field of view angle in degrees.

    Returns:
        The maximum number of points that can be seen within the given angle.

    Examples:
        >>> solve([[2, 1], [5, 5], [1, 1]], [0, 0], 90)
        2
        >>> solve([[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]], [0, 0], 10)
        1
    """
    pos_x, pos_y = position
    angles = []
    same_position_count = 0

    # 1. Convert all points to angles relative to the observer's position
    for px, py in points:
        if px == pos_x and py == pos_y:
            # Points at the exact same position as the observer are always visible
            same_position_count += 1
        else:
            # Use atan2 to get the angle in radians (-pi to pi)
            angle_rad = math.atan2(py - pos_y, px - pos_x)
            angles.append(angle_rad)

    if not angles:
        return same_position_count

    # 2. Sort angles to prepare for the sliding window approach
    angles.sort()

    # 3. Duplicate the angles by adding 2*pi to handle the circular wrap-around
    # This allows a linear sliding window to cross the -pi/pi boundary
    n = len(angles)
    two_pi = 2 * math.pi
    for i in range(n):
        angles.append(angles[i] + two_pi)

    # Convert the field of view from degrees to radians
    fov_rad = math.radians(angle)
    
    max_visible = 0
    right = 0
    
    # 4. Sliding window to find the maximum number of points within the FOV
    for left in range(n):
        # Expand the right boundary as long as the angle difference is within FOV
        # We use a small epsilon for floating point precision safety
        while right < len(angles) and angles[right] - angles[left] <= fov_rad + 1e-9:
            right += 1
        
        # The number of points in the current window is (right - left)
        current_window_count = right - left
        if current_window_count > max_visible:
            max_visible = current_window_count

    return max_visible + same_position_count
