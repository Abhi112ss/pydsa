METADATA = {
    "id": 3024,
    "name": "Type of Triangle",
    "slug": "type_of_triangle",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if three given side lengths can form a triangle and, if so, whether it is equilateral, isosceles, or scalene.",
}

def solve(a: int, b: int, c: int) -> str:
    """
    Determines the type of triangle formed by three side lengths.

    Args:
        a (int): Length of the first side.
        b (int): Length of the second side.
        c (int): Length of the third side.

    Returns:
        str: "none" if no triangle can be formed, 
             "equilateral" if all sides are equal,
             "isosceles" if two sides are equal,
             "scalene" if no sides are equal.

    Examples:
        >>> solve(3, 3, 3)
        'equilateral'
        >>> solve(3, 4, 5)
        'scalene'
        >>> solve(1, 2, 1)
        'none'
    """
    # A triangle is valid if and only if the sum of any two sides 
    # is strictly greater than the third side.
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "none"

    # Check for equilateral: all three sides are equal.
    if a == b == c:
        return "equilateral"

    # Check for isosceles: at least two sides are equal.
    # Since we already checked equilateral, this implies exactly two sides are equal.
    if a == b or b == c or a == c:
        return "isosceles"

    # If it's a valid triangle and not equilateral or isosceles, it must be scalene.
    return "scalene"
