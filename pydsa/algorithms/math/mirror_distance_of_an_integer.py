METADATA = {
    "id": 3783,
    "name": "Mirror Distance of an Integer",
    "slug": "mirror_distance_of_an_integer",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the absolute difference between an integer and its digit-reversed counterpart.",
}

def solve(n: int) -> int:
    """
    Calculates the absolute difference between the given integer and its mirror (reversed) version.

    Args:
        n: The input integer.

    Returns:
        The absolute difference between n and its digit-reversed version.

    Examples:
        >>> solve(123)
        198  # |123 - 321| = 198
        >>> solve(10)
        9    # |10 - 01| = 9
        >>> solve(5)
        0    # |5 - 5| = 0
    """
    if n < 0:
        # Assuming the problem treats the integer as a sequence of digits 
        # and the mirror of a negative number is its positive reverse.
        # However, standard LeetCode math problems usually imply non-negative.
        # We handle the absolute value to ensure digit manipulation works.
        n = abs(n)

    original_n = n
    reversed_n = 0
    
    # Perform digit reversal using modulo and integer division
    # This avoids string conversion overhead and keeps space O(1)
    temp_n = n
    while temp_n > 0:
        last_digit = temp_n % 10
        reversed_n = (reversed_n * 10) + last_digit
        temp_n //= 10
        
    # The distance is the absolute difference between the original and the mirror
    return abs(original_n - reversed_n)
