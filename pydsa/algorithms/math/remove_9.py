METADATA = {
    "id": 660,
    "name": "Remove 9",
    "slug": "remove_9",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "base_conversion"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Remove all occurrences of the digit 9 from a number and find the largest possible number that can be formed.",
}

def solve(n: int) -> int:
    """
    Removes all occurrences of the digit 9 from a number and returns the 
    largest possible number that can be formed by the remaining digits.

    The problem is equivalent to treating the number as if it were in base 9,
    where the digit '9' is skipped, effectively shifting the value.

    Args:
        n: The input integer.

    Returns:
        The largest integer formed by removing all 9s.

    Examples:
        >>> solve(19)
        1
        >>> solve(109)
        10
        >>> solve(999)
        0
    """
    if n == 0:
        return 0

    result = 0
    multiplier = 1

    # We process the number digit by digit from right to left.
    # Since we want to remove '9', we are essentially performing a 
    # base conversion logic where the digit 9 is skipped.
    while n > 0:
        digit = n % 10
        
        # If the digit is not 9, we include it in our new number.
        # We place it at the current 'multiplier' position.
        if digit != 9:
            result += digit * multiplier
            multiplier *= 10
            
        n //= 10

    return result
