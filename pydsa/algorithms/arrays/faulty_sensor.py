METADATA = {
    "id": 1826,
    "name": "Faulty Sensor",
    "slug": "faulty_sensor",
    "category": "Array",
    "aliases": [],
    "tags": ["array_manipulation", "greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of sensor readings that need to be adjusted to satisfy a specific pattern or constraint.",
}

def solve(readings: list[int], threshold: int) -> int:
    """
    Calculates the minimum number of sensor readings that need to be adjusted 
    to ensure no two adjacent readings differ by more than a given threshold.

    Args:
        readings: A list of integers representing sensor data.
        threshold: The maximum allowed difference between adjacent readings.

    Returns:
        The minimum number of adjustments required.

    Examples:
        >>> solve([1, 10, 2, 11], 2)
        2
        >>> solve([1, 2, 3, 4], 1)
        0
    """
    if not readings:
        return 0

    n = len(readings)
    adjustments = 0
    
    # We iterate through the readings and check the constraint between 
    # the current reading and the previous one.
    # If the constraint is violated, we must adjust the current reading.
    # To minimize future violations, we greedily adjust the current reading 
    # to be within the threshold of the previous one.
    
    # Note: In a real-world scenario, 'adjusting' might mean changing the value.
    # If the problem implies we can change a value to ANY value to satisfy 
    # the condition, the optimal strategy is to change the current value 
    # to match the previous value (or within threshold) so it doesn't 
    # trigger a violation with the NEXT element.
    
    last_valid_value = readings[0]
    
    for i in range(1, n):
        current_value = readings[i]
        
        # Check if the difference between current and previous valid reading 
        # exceeds the allowed threshold.
        if abs(current_value - last_valid_value) > threshold:
            # We must adjust this reading. 
            # Increment the count of adjustments.
            adjustments += 1
            
            # To be greedy, we set the current value to be the same as 
            # the last_valid_value. This ensures the current adjustment 
            # satisfies the constraint with the previous element AND 
            # provides the best chance for the next element to satisfy 
            # the constraint with this one.
            last_valid_value = last_valid_value
        else:
            # The constraint is satisfied, so we update the last_valid_value
            # to the current reading.
            last_valid_value = current_value
            
    return adjustments
