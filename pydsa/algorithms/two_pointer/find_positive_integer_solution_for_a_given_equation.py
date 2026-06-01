METADATA = {
    "id": 1237,
    "name": "Find Positive Integer Solution for a Given Equation",
    "slug": "find-positive-integer-solution-for-a-given-equation",
    "category": "Math",
    "aliases": [],
    "tags": ["two_pointer", "binary_search", "math"],
    "difficulty": "easy",
    "time_complexity": "O(max(x, y))",
    "space_complexity": "O(1)",
    "description": "Find positive integers x, y, and z that satisfy the equation x + y + z = equation[0], x * y = equation[1], and x * z = equation[2].",
}

def solve(equation: list[int]) -> list[int]:
    """
    Finds positive integers x, y, and z that satisfy the given system of equations.

    The equations are:
    1) x + y + z = equation[0]
    2) x * y = equation[1]
    3) x * z = equation[2]

    Args:
        equation: A list of three integers [sum, xy, xz].

    Returns:
        A list of three integers [x, y, z] if a solution exists, otherwise an empty list [].

    Examples:
        >>> solve([12, 4, 6])
        [2, 2, 3]
        >>> solve([3, 2, 2])
        [1, 2, 2]
        >>> solve([10, 5, 5])
        []
    """
    target_sum = equation[0]
    target_xy = equation[1]
    target_xz = equation[2]

    # Since x, y, and z must be positive integers, and the sum is at most 1000,
    # we can iterate through possible values of x.
    # From the equations: y = target_xy / x and z = target_xz / x.
    # We must ensure x is a divisor of both target_xy and target_xz.
    
    # We iterate x from 1 up to the target_sum.
    for x in range(1, target_sum):
        # Check if x is a valid divisor for both xy and xz products
        if target_xy % x == 0 and target_xz % x == 0:
            y = target_xy // x
            z = target_xz // x
            
            # Check if the derived x, y, and z satisfy the sum equation
            if x + y + z == target_sum:
                return [x, y, z]

    return []
