METADATA = {
    "id": 3581,
    "name": "Count Odd Letters from Number",
    "slug": "count_odd_letters_from_number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Count the number of odd digits in a given integer.",
}

def solve(number: int) -> int:
    """
    Counts the number of odd digits present in the given integer.

    Args:
        number: The integer to analyze.

    Returns:
        The total count of odd digits (1, 3, 5, 7, 9) in the number.

    Examples:
        >>> solve(12345)
        3
        >>> solve(2468)
        0
        >>> solve(0)
        0
    """
    # Handle negative numbers by taking the absolute value
    number = abs(number)
    odd_count = 0

    # If the number is 0, the loop won't execute, returning 0 correctly
    while number > 0:
        # Extract the last digit using modulo
        digit = number % 10
        
        # Check if the digit is odd
        if digit % 2 != 0:
            odd_count += 1
            
        # Remove the last digit using integer division
        number //= 10

    return odd_count
