METADATA = {
    "id": 233,
    "name": "Number of Digit One",
    "slug": "number-of-digit-one",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "digit-dp"],
    "difficulty": "hard",
    "time_complexity": "O(log10(n))",
    "space_complexity": "O(1)",
    "description": "Count the total number of digit 1 appearing in all non-negative integers less than or equal to n.",
}

def solve(n: int) -> int:
    """
    Calculates the total number of times the digit '1' appears in all integers from 0 to n.

    The algorithm uses a digit-by-digit counting approach. For each decimal place 
    (ones, tens, hundreds, etc.), we calculate how many times '1' appears in that 
    position by considering the prefix (digits to the left), the current digit, 
    and the suffix (digits to the right).

    Args:
        n: The upper bound integer.

    Returns:
        The total count of digit '1' occurrences.

    Examples:
        >>> solve(13)
        6
        # 1, 10, 11, 12, 13 -> '1' appears in: 1, 10, 11 (twice), 12, 13. Total = 6.
        >>> solve(0)
        0
    """
    if n <= 0:
        return 0

    total_ones = 0
    factor = 1

    # Iterate through each decimal place: 1, 10, 100, 1000...
    while factor <= n:
        # Split n into three parts based on the current factor (digit position)
        # Example: n = 1234, factor = 100
        # prefix = 12, current_digit = 3, suffix = 4
        prefix = n // (factor * 10)
        current_digit = (n // factor) % 10
        suffix = n % factor

        # Case 1: The digit at the current position is > 1
        # The digit '1' appears (prefix + 1) * factor times.
        # Example: n = 234, factor = 10. Digit is 3. 
        # '1' appears in 10-19, 110-119, 210-219.
        if current_digit > 1:
            total_ones += (prefix + 1) * factor
            
        # Case 2: The digit at the current position is exactly 1
        # The digit '1' appears (prefix * factor) + (suffix + 1) times.
        # Example: n = 123, factor = 10. Digit is 2. (Handled by Case 1)
        # Example: n = 113, factor = 10. Digit is 1.
        # '1' appears in 10-19, 110-113.
        elif current_digit == 1:
            total_ones += (prefix * factor) + (suffix + 1)
            
        # Case 3: The digit at the current position is 0
        # The digit '1' appears (prefix * factor) times.
        # Example: n = 203, factor = 10. Digit is 0.
        # '1' appears in 10-19, 110-119.
        else:
            total_ones += prefix * factor

        # Move to the next decimal place
        factor *= 10

    return total_ones
