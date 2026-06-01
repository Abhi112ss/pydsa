METADATA = {
    "id": 2821,
    "name": "Delay the Resolution of Each Promise",
    "slug": "delay-the-resolution-of-each-promise",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the resolution time for each promise based on its own delay and the resolution time of the preceding promise.",
}

def solve(delay: list[int]) -> list[int]:
    """
    Calculates the resolution time for each promise in a sequence.

    The resolution time of a promise is defined as the maximum of its own delay 
    and the resolution time of the previous promise plus its own delay.
    Mathematically: resolution[i] = max(delay[i], resolution[i-1] + delay[i])
    Since delay[i] is always positive, this simplifies to:
    resolution[i] = resolution[i-1] + delay[i] for i > 0, and resolution[0] = delay[0].
    Actually, the problem states: resolution[i] = max(delay[i], resolution[i-1] + delay[i]).
    Wait, if delay[i] is always positive, resolution[i-1] + delay[i] will always be 
    greater than or equal to delay[i]. Thus, it is a prefix sum.

    Args:
        delay: A list of integers representing the delay of each promise.

    Returns:
        A list of integers representing the resolution time of each promise.

    Examples:
        >>> solve([1, 3, 5, 2])
        [1, 4, 9, 11]
        >>> solve([10, 10, 10])
        [10, 20, 30]
    """
    if not delay:
        return []

    n = len(delay)
    resolution_times = [0] * n
    
    # The first promise's resolution time is just its own delay
    resolution_times[0] = delay[0]
    
    # Iterate through the remaining promises
    for i in range(1, n):
        # The resolution time is the previous resolution time plus the current delay.
        # Because delay[i] > 0, max(delay[i], resolution_times[i-1] + delay[i]) 
        # is always resolution_times[i-1] + delay[i].
        resolution_times[i] = resolution_times[i - 1] + delay[i]
        
    return resolution_times
