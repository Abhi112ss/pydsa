METADATA = {
    "id": 1725,
    "name": "Number Of Rectangles That Can Form The Largest Square",
    "slug": "number_of_rectangles_that_can_form_the_largest_square",
    "category": "array",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find how many rectangles can form the largest possible square.",
}


def solve(rectangles: list[list[int]]) -> int:
    """Return the number of rectangles that can form the largest possible square.

    Args:
        rectangles: A list where each element is a list of two integers
            representing the length and width of a rectangle.

    Returns:
        The count of rectangles whose maximum square side length equals the
        largest such side among all rectangles.

    Examples:
        >>> solve([[5, 8], [3, 9], [5, 12], [16, 5]])
        3
        >>> solve([[2, 3], [2, 2], [2, 4]])
        2
    """
    # Map each possible square side length to its frequency.
    side_frequency: dict[int, int] = {}
    for length, width in rectangles:
        possible_side = length if length < width else width
        side_frequency[possible_side] = side_frequency.get(possible_side, 0) + 1

    # The largest square side that can be formed.
    max_side = max(side_frequency)

    # Number of rectangles that can achieve this largest side.
    return side_frequency[max_side]