METADATA = {
    "id": 1227,
    "name": "Airplane Seat Assignment Probability",
    "slug": "airplane-seat-assignment-probability",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "probability", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine the probability that the last passenger sits in their assigned seat given specific boarding rules.",
}

def solve(n: int) -> float:
    """
    Calculates the probability that the last passenger sits in their assigned seat.

    The problem follows a specific pattern:
    - If n = 1, the passenger always sits in their own seat (probability 1.0).
    - If n > 1, the probability is always 0.5. This is because for any passenger 
      who is forced to take a different seat, they either take the first passenger's 
      seat or the last passenger's seat. Once the last passenger's seat is taken, 
      the outcome is decided. Due to symmetry, this happens with 50% probability.

    Args:
        n (int): The total number of passengers and seats.

    Returns:
        float: The probability that the last passenger sits in their assigned seat.

    Examples:
        >>> solve(1)
        1.0
        >>> solve(2)
        0.5
        >>> solve(10)
        0.5
    """
    # Base case: If there is only one passenger, they must sit in their own seat.
    if n == 1:
        return 1.0
    
    # For n > 1, the symmetry of the problem dictates that the last passenger 
    # has a 50% chance of landing in their assigned seat.
    return 0.5
