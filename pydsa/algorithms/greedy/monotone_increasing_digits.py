METADATA = {
    "id": 738,
    "name": "Monotone Increasing Digits",
    "slug": "monotone-increasing-digits",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Find the largest number less than or equal to n that has non-decreasing digits.",
}

def solve(n: int) -> int:
    """
    Finds the largest number less than or equal to n that has non-decreasing digits.

    The algorithm works by converting the number to a list of digits. It scans 
    from right to left to find the first point where a digit is greater than 
    the digit to its right. Once found, it decrements that digit and marks 
    all subsequent digits to be turned into 9s.

    Args:
        n: The input integer.

    Returns:
        The largest integer <= n with non-decreasing digits.

    Examples:
        >>> solve(10)
        9
        >>> solve(1234)
        1234
        >>> solve(332)
        299
        >>> solve(10)
        9
    """
    # Convert number to a list of digits for easy manipulation
    digits = [int(d) for d in str(n)]
    length = len(digits)
    
    # marker tracks the position from which all digits to the right should become 9
    marker = length
    
    # Iterate from right to left to find the first decreasing pair
    for i in range(length - 1, 0, -1):
        if digits[i - 1] > digits[i]:
            # Decrement the left digit of the decreasing pair
            digits[i - 1] -= 1
            # Mark this position; everything after this index will be set to 9
            marker = i
            
    # Set all digits from the marker position to the end to 9
    for i in range(marker, length):
        digits[i] = 9
        
    # Convert the list of digits back into an integer
    result = 0
    for digit in digits:
        result = result * 10 + digit
        
    return result
