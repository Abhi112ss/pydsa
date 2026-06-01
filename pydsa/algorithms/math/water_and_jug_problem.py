METADATA = {
    "id": 365,
    "name": "Water and Jug Problem",
    "slug": "water-and-jug-problem",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "gcd", "number theory"],
    "difficulty": "medium",
    "time_complexity": "O(log(min(x, y)))",
    "space_complexity": "O(1)",
    "description": "Determine if a target amount of water can be measured using two jugs with capacities x and y.",
}

import math

def solve(x: int, y: int, z: int) -> bool:
    """
    Determines if it is possible to measure exactly z liters of water using 
    two jugs with capacities x and y.

    The problem is a variation of Bézout's identity. We can measure any amount 
    that is a multiple of the greatest common divisor (GCD) of x and y, 
    provided the target amount z does not exceed the total capacity of both jugs.

    Args:
        x: Capacity of the first jug.
        y: Capacity of the second jug.
        z: Target amount of water to measure.

    Returns:
        True if the target amount z can be measured, False otherwise.

    Examples:
        >>> solve(3, 5, 4)
        True
        >>> solve(2, 6, 5)
        False
        >>> solve(1, 1, 2)
        True
    """
    # If the target amount is greater than the combined capacity, it's impossible.
    if z > x + y:
        return False

    # If the target is 0, it is always possible (by doing nothing).
    if z == 0:
        return True

    # According to Bézout's identity, the equation ax + by = z has integer 
    # solutions for a and b if and only if z is a multiple of gcd(x, y).
    # In this context, a and b represent the number of times we fill/empty 
    # the jugs, which can be modeled as a linear combination.
    common_divisor = math.gcd(x, y)

    # Check if the target amount is divisible by the greatest common divisor.
    return z % common_divisor == 0
