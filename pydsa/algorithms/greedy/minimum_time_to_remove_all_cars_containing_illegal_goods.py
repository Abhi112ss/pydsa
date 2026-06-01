METADATA = {
    "id": 2167,
    "name": "Minimum Time to Remove All Cars Containing Illegal Goods",
    "slug": "minimum-time-to-remove-all-cars-containing-illegal-goods",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "array", "two-pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum time to remove all illegal cars by processing contiguous segments of illegal cars independently.",
}

def solve(cars: list[int], removal_time: int) -> int:
    """
    Calculates the minimum time required to remove all cars marked with 1.

    The strategy is to identify contiguous segments of illegal cars (1s). 
    For each segment of length 'k', the time taken to clear it is 
    k * removal_time. Since segments are separated by legal cars (0s), 
    we can process each segment independently.

    Args:
        cars: A list of integers where 1 represents an illegal car and 0 represents a legal car.
        removal_time: The time taken to remove a single illegal car.

    Returns:
        The total minimum time to remove all illegal cars.

    Examples:
        >>> solve([1, 1, 0, 1, 1, 1], 2)
        10
        >>> solve([0, 0, 0], 5)
        0
        >>> solve([1, 0, 1, 0, 1], 1)
        3
    """
    total_time = 0
    current_segment_length = 0

    for car in cars:
        if car == 1:
            # Increment the count of consecutive illegal cars found
            current_segment_length += 1
        else:
            # When a legal car is encountered, calculate time for the previous segment
            if current_segment_length > 0:
                total_time += current_segment_length * removal_time
                current_segment_length = 0
    
    # Final check to add time for a segment that might end at the last index
    if current_segment_length > 0:
        total_time += current_segment_length * removal_time

    return total_time
