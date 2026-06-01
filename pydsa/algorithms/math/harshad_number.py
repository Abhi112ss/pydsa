METADATA = {
    "id": 3099,
    "name": "Harshad Number",
    "slug": "harshad-number",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Determine if a number is divisible by the sum of its digits.",
}

def solve(n: int) -> bool:
    """
    Determines if a given integer is a Harshad number.
    
    A Harshad number is an integer that is divisible by the sum of its digits.

    Args:
        n: The integer to check.

    Returns:
        True if n is a Harshad number, False otherwise.

    Examples:
        >>> solve(18)
        True
        >>> solve(19)
        False
    """
    # Store the original number to perform the final divisibility check
    original_number = n
    digit_sum = 0
    
    # Extract digits using modulo and integer division
    temp_n = n
    while temp_n > 0:
        # Get the last digit
        digit = temp_n % 10
        digit_sum += digit
        # Remove the last digit
        temp_n //= 10
        
    # A Harshad number must be divisible by its digit sum
    # Note: The problem constraints usually imply n > 0
    return original_number % digit_sum == 0
