METADATA = {
    "id": 2481,
    "name": "Minimum Cuts to Divide a Circle",
    "slug": "minimum-cuts-to-divide-a-circle",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of cuts needed to divide a circle into at least n regions.",
}

def solve(n: int) -> int:
    """
    Calculates the minimum number of cuts required to divide a circle into at least n regions.

    The maximum number of regions R that can be created by k cuts is given by the 
    Lazy Caterer's Sequence formula: R = (k^2 + k + 2) / 2.
    We need to find the smallest integer k such that (k^2 + k + 2) / 2 >= n.

    Args:
        n: The target number of regions.

    Returns:
        The minimum number of cuts required.

    Examples:
        >>> solve(1)
        0
        >>> solve(2)
        1
        >>> solve(4)
        2
        >>> solve(10)
        4
    """
    if n <= 1:
        return 0

    # We solve the quadratic inequality: (k^2 + k + 2) / 2 >= n
    # k^2 + k + (2 - 2n) >= 0
    # Using the quadratic formula for k^2 + k + (2 - 2n) = 0:
    # k = (-b + sqrt(b^2 - 4ac)) / 2a
    # k = (-1 + sqrt(1 - 4(1)(2 - 2n))) / 2
    # k = (-1 + sqrt(1 - 8 + 8n)) / 2
    # k = (-1 + sqrt(8n - 7)) / 2

    # Calculate the discriminant part
    discriminant = 8 * n - 7
    
    # Calculate the positive root for k
    # We use math.isqrt or float math; since n can be up to 10^9, 
    # float precision is sufficient for the square root.
    import math
    
    k_float = (-1 + math.sqrt(discriminant)) / 2
    
    # Since we need the smallest integer k that satisfies the inequality,
    # we take the ceiling of the calculated k.
    # However, due to floating point precision, we use math.ceil with a small epsilon 
    # or simply check the integer boundary.
    
    k_result = math.ceil(k_float)
    
    # Double check the result to handle potential floating point inaccuracies
    # (k^2 + k + 2) // 2 should be >= n
    if (k_result * k_result + k_result + 2) // 2 < n:
        k_result += 1
        
    return k_result
