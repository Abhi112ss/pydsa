METADATA = {
    "id": 2739,
    "name": "Total Distance Traveled",
    "slug": "total-distance-traveled",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total distance traveled by summing the absolute differences between consecutive elements in an array.",
}

def solve(positions: list[int]) -> int:
    """
    Calculates the total distance traveled based on a sequence of positions.

    The total distance is the sum of the absolute differences between 
    each consecutive pair of elements in the input list.

    Args:
        positions: A list of integers representing positions at consecutive time steps.

    Returns:
        The total distance traveled as an integer.

    Examples:
        >>> solve([1, 3, 4])
        4
        >>> solve([1, 1, 1])
        0
        >>> solve([1, 5, 2, 8])
        13
    """
    total_distance = 0
    
    # Iterate through the list starting from the second element
    for index in range(1, len(positions)):
        # Calculate the absolute difference between current and previous position
        current_step_distance = abs(positions[index] - positions[index - 1])
        total_distance += current_step_distance
        
    return total_distance
