METADATA = {
    "id": 853,
    "name": "Car Fleet",
    "slug": "car-fleet",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Determine the number of car fleets that will arrive at a target destination based on positions and speeds.",
}

def solve(target: int, position: list[int], speed: list[int]) -> int:
    """
    Calculates the number of car fleets that will arrive at the target.

    A car fleet is formed when a faster car catches up to a slower car ahead of it,
    causing it to slow down to the speed of the leading car.

    Args:
        target: The destination position.
        position: A list of integers representing the starting positions of cars.
        speed: A list of integers representing the speeds of the cars.

    Returns:
        The total number of car fleets that arrive at the target.

    Examples:
        >>> solve(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
        3
        >>> solve(10, [0, 2, 4], [0, 0, 0])
        3
    """
    if not position:
        return 0

    # Combine position and speed, then sort by position in descending order.
    # We process cars from the one closest to the target to the one furthest away.
    cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

    fleet_count = 0
    # time_to_reach_target stores the arrival time of the lead car of the current fleet.
    current_fleet_arrival_time = 0.0

    for pos, spd in cars:
        # Calculate time required for the current car to reach the target.
        time_to_reach = (target - pos) / spd

        # If the current car takes more time than the fleet ahead of it,
        # it cannot catch up and thus starts a new fleet.
        if time_to_reach > current_fleet_arrival_time:
            fleet_count += 1
            current_fleet_arrival_time = time_to_reach
        
        # If time_to_reach <= current_fleet_arrival_time, this car 
        # joins the existing fleet ahead of it and doesn't change the fleet's arrival time.

    return fleet_count
