METADATA = {
    "id": 1344,
    "name": "Angle Between Hands of a Clock",
    "slug": "angle-between-hands-of-a-clock",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the smallest angle between the hour and minute hands of a clock given hours and minutes.",
}

def solve(hours: int, minutes: int) -> int:
    """
    Calculates the smallest angle between the hour and minute hands of a clock.

    Args:
        hours (int): The hour component (1 <= hours <= 12).
        minutes (int): The minute component (0 <= minutes <= 59).

    Returns:
        int: The smallest angle in degrees between the two hands.

    Examples:
        >>> solve(3, 30)
        75
        >>> solve(6, 15)
        157
        >>> solve(12, 0)
        0
    """
    # The clock is a circle of 360 degrees.
    # Minute hand moves 360 degrees in 60 minutes -> 6 degrees per minute.
    minute_angle = minutes * 6

    # Hour hand moves 360 degrees in 12 hours -> 30 degrees per hour.
    # Additionally, the hour hand moves as the minutes pass.
    # In 60 minutes, the hour hand moves 30 degrees -> 0.5 degrees per minute.
    # We use (hours % 12) to treat 12 o'clock as 0 degrees.
    hour_angle = (hours % 12) * 30 + (minutes * 0.5)

    # Calculate the absolute difference between the two angles.
    angle_diff = abs(hour_angle - minute_angle)

    # The problem asks for the smallest angle (the minor arc).
    # If the difference is greater than 180, subtract it from 360.
    if angle_diff > 180:
        angle_diff = 360 - angle_diff

    # Return as integer as per problem requirements.
    return int(angle_diff)
