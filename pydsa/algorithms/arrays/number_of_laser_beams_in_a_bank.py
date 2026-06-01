METADATA = {
    "id": 2125,
    "name": "Number of Laser Beams in a Bank",
    "slug": "number-of-laser-beams-in-a-bank",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of laser beams between sensors in different rows of a grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the total number of laser beams in a bank.
    
    A laser beam exists between every pair of sensors in two different rows, 
    provided there are no other sensors in the rows between them.

    Args:
        grid: A 2D list of integers representing the bank where 1 is a sensor and 0 is empty.

    Returns:
        The total number of laser beams.

    Examples:
        >>> solve([[1,1,0],[0,1,1],[1,0,1]])
        4
        >>> solve([[0,0,0],[0,0,0]])
        0
    """
    total_beams = 0
    previous_row_sensor_count = 0

    for row in grid:
        # Count the number of sensors in the current row
        current_row_sensor_count = sum(row)

        # If the current row has sensors, they can form beams with the previous non-empty row
        if current_row_sensor_count > 0:
            # The number of beams is the product of sensors in the current row 
            # and the sensors in the last row that contained sensors.
            total_beams += (previous_row_sensor_count * current_row_sensor_count)
            
            # Update the previous row count to the current one for the next non-empty row
            previous_row_sensor_count = current_row_sensor_count

    return total_beams
