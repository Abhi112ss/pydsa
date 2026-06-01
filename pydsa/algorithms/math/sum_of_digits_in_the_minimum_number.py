METADATA = {
    "id": 1085,
    "name": "Sum of Digits in the Minimum Number",
    "slug": "sum-of-digits-in-the-minimum-number",
    "category": "Math",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log k)",
    "space_complexity": "O(log k)",
    "description": "Find the smallest non-negative integer whose digits sum up to a given integer k.",
}

def solve(k: int) -> int:
    """
    Finds the smallest non-negative integer whose digits sum up to k.

    The strategy is to use a greedy approach: to make the number as small as possible,
    we want to minimize the number of digits. To minimize the number of digits,
    we should make each digit as large as possible (i.e., 9). We place these 9s
    at the least significant positions (the end of the number).

    Args:
        k: The target sum of digits.

    Returns:
        The smallest integer whose digits sum to k.

    Examples:
        >>> solve(10)
        19
        >>> solve(27)
        999
        >>> solve(1)
        1
    """
    if k == 0:
        return 0

    digits = []
    
    # Greedily extract as many 9s as possible from the end
    while k >= 9:
        digits.append("9")
        k -= 9
    
    # If there is a remainder, it becomes the leading digit
    if k > 0:
        digits.append(str(k))
    
    # Since we appended 9s first, the 'remainder' digit is actually the 
    # most significant digit. We reverse the list to get the correct order.
    # Example: k=10 -> digits=['9', '1'] -> reversed=['1', '9'] -> 19
    digits.reverse()
    
    return int("".join(digits))
