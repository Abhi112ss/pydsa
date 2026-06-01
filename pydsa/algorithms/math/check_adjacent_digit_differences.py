METADATA = {
    "id": 3931,
    "name": "Check Adjacent Digit Differences",
    "slug": "check-adjacent-digit-differences",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if the absolute difference between every pair of adjacent digits in a number is equal to a given threshold.",
}

def solve(num: int, threshold: int) -> bool:
    """
    Checks if the absolute difference between every pair of adjacent digits 
    in the given number is exactly equal to the threshold.

    Args:
        num: The integer to check.
        threshold: The required absolute difference between adjacent digits.

    Returns:
        True if all adjacent digit differences equal the threshold, False otherwise.

    Examples:
        >>> solve(123, 1)
        True
        >>> solve(135, 2)
        True
        >>> solve(121, 2)
        False
    """
    # Convert number to string to iterate through digits easily
    digit_str = str(num)
    
    # If there is only one digit, there are no adjacent pairs to compare.
    # Based on the problem logic, a single digit satisfies the condition vacuously.
    if len(digit_str) < 2:
        return True

    # Iterate through the string from the first digit to the second to last
    for i in range(len(digit_str) - 1):
        # Calculate the absolute difference between current digit and next digit
        current_digit = int(digit_str[i])
        next_digit = int(digit_str[i + 1])
        diff = abs(current_digit - next_digit)
        
        # If any difference does not match the threshold, return False immediately
        if diff != threshold:
            return False
            
    return True
