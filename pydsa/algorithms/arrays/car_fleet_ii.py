METADATA = {
    "id": 1776,
    "name": "Car Fleet II",
    "slug": "car-fleet-ii",
    "category": "Stack",
    "aliases": [],
    "tags": ["monotonic_stack", "array", "monotonic_queue"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the time each car arrives at its destination, considering that cars cannot pass each other and will form fleets.",
}

def solve(target: int, position: list[int], speed: list[int]) -> list[int]:
    """
    Calculates the time each car reaches its destination, accounting for car fleets.

    Args:
        target: The target position all cars are driving towards.
        position: A list of integers representing the starting position of each car.
        speed: A list of integers representing the speed of each car.

    Returns:
        A list of floats representing the time each car reaches the target.

    Examples:
        >>> solve(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
        [1.0, 1.0, 12.0, 7.0, 3.0]
    """
    n = len(position)
    # Combine position and speed, then sort by position in descending order.
    # We process cars from closest to target to furthest from target.
    cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
    
    # arrival_times[i] will store the time the i-th car (in sorted order) reaches target.
    arrival_times = [0.0] * n
    # monotonic_stack stores indices of cars that could potentially be the "leader" 
    # for subsequent cars.
    stack = []

    for i in range(n):
        curr_pos, curr_speed = cars[i]
        # Time it would take for this car to reach target if no one was in front.
        time_to_reach = (target - curr_pos) / curr_speed
        
        # We look for the first car ahead (already in stack) that this car 
        # will catch up to. A car catches up if its time_to_reach is <= 
        # the time the car in front reaches the target.
        # However, the car in front might itself be part of a fleet.
        # We use a monotonic stack to find the nearest car ahead that has 
        # a strictly greater arrival time.
        while stack and arrival_times[stack[-1]] <= time_to_reach:
            stack.pop()
            
        if not stack:
            # No car ahead is slower; this car reaches target at its own time.
            arrival_times[i] = time_to_reach
        else:
            # This car catches up to the car at stack[-1].
            # Its arrival time is constrained by the arrival time of the car it catches.
            arrival_times[i] = arrival_times[stack[-1]]
            
        stack.append(i)

    # The problem asks for arrival times in the original order of positions.
    # We need to map the sorted results back to the original input order.
    # Create a mapping from original position to its calculated arrival time.
    result_map = {}
    for i in range(n):
        result_map[cars[i][0]] = arrival_times[i]
        
    return [result_map[p] for p in position]
