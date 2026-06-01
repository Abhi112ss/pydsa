METADATA = {
    "id": 3053,
    "name": "Classifying Triangles by Lengths",
    "slug": "classifying_triangles_by_lengths",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Classify triangles based on side lengths after verifying the triangle inequality theorem.",
}

def solve(sides: list[int]) -> str:
    """
    Classifies a triangle based on its side lengths.

    The function first sorts the sides to easily identify the longest side.
    It then checks the triangle inequality theorem (sum of two shorter sides 
    must be greater than the longest side). If valid, it classifies the 
    triangle as equilateral, isosceles, or scalene.

    Args:
        sides: A list of three integers representing the lengths of the sides.

    Returns:
        A string representing the classification: "invalid", "equilateral", 
        "isosceles", or "scalene".

    Examples:
        >>> solve([3, 3, 3])
        'equilateral'
        >>> solve([3, 4, 5])
        'scalene'
        >>> solve([1, 1, 3])
        'invalid'
    """
    # Sort sides to ensure sides[0] <= sides[1] <= sides[2]
    # This makes the triangle inequality check (a + b > c) straightforward
    sorted_sides = sorted(sides)
    a, b, c = sorted_sides[0], sorted_sides[1], sorted_sides[2]

    # Check the triangle inequality theorem
    if a + b <= c:
        return "invalid"

    # Determine classification based on number of unique side lengths
    # Using a set is an efficient way to count unique elements
    unique_sides_count = len(set(sorted_sides))

    if unique_sides_count == 1:
        return "equilateral"
    elif unique_sides_count == 2:
        return "isosceles"
    else:
        return "scalene"
