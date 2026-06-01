METADATA = {
    "id": 2534,
    "name": "Time Taken to Cross the Door",
    "slug": "time_taken_to_cross_the_door",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Calculate the total time taken to cross a door given the speed and the distance of the door from the starting point.",
}

def solve(distance: int, speed: int) -> int:
    """
    Calculates the total time taken to cross the door.

    The problem asks for the time taken to reach the door and cross it.
    Based on the problem description, the total time is the distance divided 
    by the speed, rounded up to the nearest integer.

    Args:
        distance (int): The distance from the starting point to the door.
        speed (int): The speed at which the person moves.

    Returns:
        int: The total time taken to cross the door, rounded up.

    Examples:
        >>> solve(10, 3)
        4
        >>> solve(5, 5)
        1
        >>> solve(1, 10)
        1
    """
    # The time taken is distance / speed.
    # Since we need the ceiling of the division (to account for the time 
    # taken to actually cross/complete the movement), we use (a + b - 1) // b
    # which is a standard integer arithmetic trick for ceil(a / b).
    
    if speed == 0:
        raise ValueError("Speed cannot be zero.")
        
    return (distance + speed - 1) // speed
